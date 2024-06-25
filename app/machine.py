from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import joblib
from joblib import Memory
import os
import datetime
from datetime import datetime


class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Random Forest Classifier"
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       

    def __call__(self, feature_basis: DataFrame):
        prediction, *_ = self.model.predict(feature_basis)
        proba, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(proba)
    
    def save(self, filepath):
        # properly save the machine learning model to the specififed filepath using joblib
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        # properly load a saved machine learning model from the specified filepath using joblib
        model_info = joblib.load(filepath)
    
        return model_info
    
        # use "model.joblib" incase filepath doesnt work
    
    def info(self):

        # return a string with the name of the base model and the timestamp of when it was initialized
        
        return f"current prediction for {self.name} at {self.timestamp}."

# The Best Model: RandomForestClassifier.
# I created a RandomForestClassifier with 100 trees. The reason the random forest has more accurate predictions is that it prevents overfitting.
# It does so by creating multiple independent decision tress that are unlinkely to make the same mistakes.
# It helps ensure the model is more geralizable. Overrall it performs better with more categorical data than numeric.
