### Description

This framework is designed to facilitate the implementation of custom machine-learning algorithms with modular components. It allows users to build, train, and evaluate custom models and automate algorithms using a flexible and extensible architecture and use directly to call functions.

### Tech Stack

- **Programming Language**: Python
- **Machine Learning Library**: TensorFlow

### Features

- Modular components for building custom ML algorithms
- Easy integration with TensorFlow for training and evaluation
- Extensible architecture for adding new algorithms and components
  

### Directory Structure

```
Ml-framework/
│
├── algorithms/
│   ├── base.py
│   ├── custom_algorithm_1.py
│   └── custom_algorithm_2.py
│
├── data/
│   └── data_loader.py
│
├── models/
│   ├── base_model.py
│   ├── custom_model_1.py
│   └── custom_model_2.py
│
├── utils/
│   ├── metrics.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

### Usage

1. **Data Loading**:
    Place your data in the `data/` directory. Modify the `data_loader.py` script to load and preprocess your data.

2. **Implement Custom Algorithms**:
    Implement your custom algorithms in the `algorithms/` directory. Use `base.py` as a template for your custom algorithm classes.

3. **Implement Custom Models**:
    Implement your custom models in the `models/` directory. Use `base_model.py` as a template for your custom model classes.

4. **Training and Evaluation**:
    Use the `main.py` script to train and evaluate your models. Here's an example of how to use the framework:

### Extending the Framework

To add a new custom algorithm or model, follow these steps:

1. **Add a new algorithm**:
    - Create a new file in the `algorithms/` directory (e.g., `custom_algorithm_3.py`).
    - Implement your algorithm class by extending the base class in `base.py`.

2. **Add a new model**:
    - Create a new file in the `models/` directory (e.g., `custom_model_3.py`).
    - Implement your model class by extending the base class in `base_model.py`.

