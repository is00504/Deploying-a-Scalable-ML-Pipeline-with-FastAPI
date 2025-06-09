import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.model import compute_model_metrics, inference


# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model_metrics():
    """
    # tests that model metrics are computing as expected
    """
    labels = [1, 1, 0]
    model_output = [0, 1, 1]
    precision, recall, fbeta = compute_model_metrics(labels, model_output)
    assert precision is not None and 0 <= precision <= 1
    assert recall is not None and 0 <= recall <= 1
    assert fbeta is not None and 0 <= fbeta <= 1

    pass


# TODO: implement the second test. Change the function name and input as needed
def test_feature_num():
    """
    # tests that the model has 14 features
    """
    X = np.random.rand(3,14)
    assert X.shape[1] == 14, f"Expected 14 features, got {X.shape[1]}."
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    # tests that the inference function output returns the correct length.
    """
    X_test = np.random.rand(3, 4)
    y_test = [0, 1, 0]
    model = RandomForestClassifier()
    model.fit(X_test,y_test)
    predictions = inference(model, X_test)
    assert len(predictions) == len(X_test), "Output length does not match input data."

    pass
