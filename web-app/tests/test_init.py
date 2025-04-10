import pytest
from app import create_app  # Import from app/__init__.py
from bson.objectid import ObjectId
from flask import url_for
from flask_login import current_user
from app.auth import auth, User, load_user  # Adjust according to your project structure
from app.extensions import bcrypt, db, login_manager

def test_create_app(monkeypatch):
    """
    Test that the create_app function initializes the app
    with the correct configuration and registers required blueprints.
    """
    # Set environment variables for testing
    test_mongo_uri = "mongodb://localhost:27017/testdb"
    test_secret_key = "testsecret"
    monkeypatch.setenv("MONGO_URI", test_mongo_uri)
    monkeypatch.setenv("SECRET_KEY", test_secret_key)

    # Create the app
    app = create_app()

    # Check configuration values
    assert app.config["MONGO_URI"] == test_mongo_uri, "MONGO_URI should match the test value"
    assert app.secret_key == test_secret_key, "Secret key should match the test value"

    # Check that the blueprints are registered
    # We convert to a list to make it easier to check membership
    registered_blueprints = list(app.blueprints.keys())
    assert "main" in registered_blueprints, "Main blueprint is not registered"
    assert "auth" in registered_blueprints, "Auth blueprint is not registered"

class FakeCollection:
    def __init__(self):
        self.users = {}

    def find_one(self, query):
        if "username" in query:
            username = query["username"]
            for user in self.users.values():
                if user.get("username") == username:
                    return user
            return None
        if "_id" in query:
            user_id = str(query["_id"])
            return self.users.get(user_id)
        return None

    def insert_one(self, data):
        new_id = ObjectId()
        data["_id"] = new_id
        self.users[str(new_id)] = data
        # Return a dummy object with an inserted_id attribute.
        return type("InsertResult", (), {"inserted_id": new_id})()


# --- Fixtures to create our app and client for testing ---

@pytest.fixture
def app(monkeypatch):
    """
    Create a test instance of the Flask app.
    Overwrite the real db.users with a FakeCollection.
    """
    # Make sure our fake collection is used
    monkeypatch.setattr(db, "users", FakeCollection())

    from app import create_app  # Import the application factory from app/__init__.py
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    """
    Create a test client for our application.
    """
    return app.test_client()


# --- Extended Tests for auth routes and user loader ---

def test_get_register(client):
    """
    Test the GET /register endpoint returns the registration form.
    """
    response = client.get("/register")
    assert response.status_code == 200
    # Check for an expected snippet of text in the registration page.
    # (Adjust the text snippet based on your actual rendered template.)
    assert b"register" in response.data.lower()


def test_get_login(client):
    """
    Test the GET /login endpoint returns the login form.
    """
    response = client.get("/login")
    assert response.status_code == 200
    # Check for some text that indicates the login form is rendered.
    assert b"login" in response.data.lower()


def test_load_user_function(client):
    """
    Test that load_user returns a valid User instance for a valid user ID.
    """
    # Insert a dummy user into the fake collection.
    user_data = {
        "username": "testuser",
        "password": bcrypt.generate_password_hash("password").decode("utf-8")
    }
    result = db.users.insert_one(user_data)
    user_id = str(result.inserted_id)

    loaded_user = load_user(user_id)
    assert loaded_user is not None
    assert loaded_user.username == "testuser"


def test_login_nonexistent_user(client):
    """
    Test that logging in with a non-existent user flashes an error.
    """
    response = client.post(
        "/login",
        data={"username": "nonexistent", "password": "nopass"},
        follow_redirects=True
    )
    # The login page should be rendered again with an error message.
    assert response.status_code == 200
    assert b"invalid credentials" in response.data.lower()

def test_login_and_logout_cycle(client):
    """
    Test the complete cycle of registration, login and logout.
    """
    # --- Register a new user ---
    register_response = client.post(
        "/register",
        data={"username": "cycleuser", "password": "cyclepass"},
        follow_redirects=True
    )
    # After registration, user is redirected to the login page.
    assert b"login" in register_response.data.lower()

    # --- Log in with the newly registered user ---
    login_response = client.post(
        "/login",
        data={"username": "cycleuser", "password": "cyclepass"},
        follow_redirects=True
    )
    # Expect a redirection to main.home; here we look for specific text from home page.
    # Adjust the text assertion based on what your home page returns.
    assert b"home" in login_response.data.lower() or b"welcome" in login_response.data.lower()

    # --- Log out and confirm redirection to home ---
    logout_response = client.get("/logout", follow_redirects=True)
    assert logout_response.status_code == 200
    assert b"home" in logout_response.data.lower()
