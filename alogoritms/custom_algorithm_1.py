import tensorflow as tf
from base import BaseAlgorithm

class CustomAlgorithm1(BaseAlgorithm):
    def train(self, model, data):
        X_train, y_train = data
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=10, batch_size=32)

    def evaluate(self, model, data):
        X_test, y_test = data
        _, accuracy = model.evaluate(X_test, y_test)
        return accuracy
