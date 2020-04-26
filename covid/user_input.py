import pandas as pd
import utils
from sklearn import tree, model_selection
import importlib

moduleName = ("predict_logistic_regression")
importlib.import_module(moduleName)

gender = input("Enter your sex (male or female): ")
age = input("Enter your age: ")
userFeatures = [gender, age]

generalized_tree_.predict(userFeatures)