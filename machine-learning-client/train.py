import os
import numpy as np
import pandas as pd
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from model import create_cnn  # your model definition
from model_utils import to_cat  # your helper for one-hot encoding

def preprocess_data():
    """
    Load and preprocess the Sign Language MNIST data.
    Reads both training and test CSV files, reshapes the images,
    converts the labels using to_cat, and splits a validation set.
    """
    # Load training data from CSV
    pddata_train = pd.read_csv('data/sign_mnist_train.csv')
    data_train = pddata_train.values
    data_train_X = data_train[:, 1:]  # All columns except the first (labels)
    data_train_X = data_train_X.reshape((data_train_X.shape[0], 28, 28, 1))
    data_train_y = data_train[:, :1].reshape(-1)
    data_train_y = to_cat(data_train_y, 26)  # convert to one-hot encoding

    # Split a small portion as validation (e.g., 10% for validation)
    test_size = 0.1
    test_ind = int(test_size * data_train_X.shape[0])
    # Use the first 10% as validation and the rest as training
    train_X = data_train_X[test_ind:]
    train_y = data_train_y[test_ind:]
    val_X = data_train_X[:test_ind]
    val_y = data_train_y[:test_ind]

    # Load test data from CSV
    pddata_test = pd.read_csv('data/sign_mnist_test.csv')
    data_test = pddata_test.values
    data_test_X = data_test[:, 1:]
    data_test_X = data_test_X.reshape((data_test_X.shape[0], 28, 28, 1))
    data_test_y = data_test[:, :1].reshape(-1)
    data_test_y = to_cat(data_test_y, 26)

    return train_X, train_y, val_X, val_y, data_test_X, data_test_y

def run_model(lr, batch_size, epochs, reg, X_train, y_train, X_test, y_test):
    """
    Builds, trains, saves, and evaluates the CNN model.
    """
    # Build the CNN model using the create_cnn() function (from model.py)
    model = create_cnn((28, 28, 1), Adam(lr), reg)
    
    # Set up early stopping to prevent overfitting
    early_stop = EarlyStopping(monitor="loss", patience=10, restore_best_weights=True, verbose=1)
    
    # Train the model
    history = model.fit(
        X_train, y_train,
        batch_size=batch_size,
        epochs=epochs,
        callbacks=[early_stop],
        verbose=1
    )

    # Save the trained model in a directory named 'model'
    os.makedirs("model", exist_ok=True)
    model_save_path = os.path.join("model", "asl_cnn.h5")
    model.save(model_save_path)
    print(f"Trained model saved to {model_save_path}")
    
    # Evaluate on the test set (and/or training set)
    test_accuracy = model.evaluate(X_test, y_test, verbose=0)[1]
    train_accuracy = model.evaluate(X_train, y_train, verbose=0)[1]
    
    return history, test_accuracy, train_accuracy

if __name__ == "__main__":
    # Preprocess the data
    train_X, train_y, val_X, val_y, test_X, test_y = preprocess_data()
    
    # In this example, we use the training data (excluding validation) for training.
    # You could also choose to merge the training and validation sets or use validation data for callbacks.
    # Hyperparameters (adjust as needed)
    learning_rate = 0.001
    batch_size = 32
    epochs = 50
    reg = None  # or set a regularizer like tf.keras.regularizers.l2(0.001)
    
    # Train the model and evaluate it on test data
    history, test_acc, train_acc = run_model(learning_rate, batch_size, epochs, reg, train_X, train_y, test_X, test_y)
    
    print(f"Training Accuracy: {train_acc:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")
