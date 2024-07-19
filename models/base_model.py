# models/base_model.py
class BaseModel:
    def __init__(self):
        pass

    def build_model(self):
        raise NotImplementedError

    def compile_model(self):
        raise NotImplementedError

    def fit(self, *args, **kwargs):
        raise NotImplementedError

    def evaluate(self, *args, **kwargs):
        raise NotImplementedError

    def predict(self, *args, **kwargs):
        raise NotImplementedError
