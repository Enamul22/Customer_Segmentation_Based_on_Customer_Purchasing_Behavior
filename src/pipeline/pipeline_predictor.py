import sys
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, rfm):
        try:
            # Load the model
            model_path = os.path.join("models", "kmeans.pkl")
            model = load_object(file_path=model_path)

            # Normalize the data
            scaler = StandardScaler()
            rfm_normalized = scaler.fit_transform(rfm)

            # Make predictions
            preds = model.predict(rfm_normalized)

            return preds
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, Recency, Frequency, MonetaryValue):
        self.Recency = Recency
        self.Frequency = Frequency
        self.MonetaryValue = MonetaryValue

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Recency": [self.Recency],
                "Frequency": [self.Frequency],
                "MonetaryValue": [self.MonetaryValue],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
