from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dropout, Dense
from tensorflow.keras.initializers import GlorotNormal

# For data augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
)

# Modify your create_cnn function (in your model.py) to incorporate BatchNormalization, for example:
def create_cnn(input_shape, optimizer, regularizer):
    model = Sequential()
    model.add(Input(shape=input_shape))
    model.add(Conv2D(8, 3, activation='selu', padding='same', kernel_initializer=GlorotNormal(seed=42)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Conv2D(4, 2, activation='selu', padding='same', kernel_initializer=GlorotNormal(seed=42)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(2))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(26, activation='softmax', kernel_regularizer=regularizer, kernel_initializer=GlorotNormal(seed=42)))
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model
