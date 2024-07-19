# models/tensorflow_models.py
import tensorflow as tf
from .base_model.py import BaseModel

class TensorFlowModel(BaseModel):
    def build_model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

    def compile_model(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def fit(self, X_train, y_train, *args, **kwargs):
        self.model.fit(X_train, y_train, *args, **kwargs)

    def evaluate(self, X_test, y_test, *args, **kwargs):
        return self.model.evaluate(X_test, y_test, *args, **kwargs)

    def predict(self, X, *args, **kwargs):
        return self.model.predict(X, *args, **kwargs)
