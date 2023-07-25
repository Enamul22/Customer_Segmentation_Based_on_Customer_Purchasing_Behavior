import sys
from dataclasses import dataclass
import pandas as pd
import os

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    data_file_path=os.path.join('data', 'Customer Segmentation/notebook/data/online_retail_II.xlsx')  # replace with your data file name

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def preprocess_data(self, data):
        # Remove canceled orders
        data = data[data['Quantity'] > 0]

        # Remove rows where customer ID is NA
        data.dropna(subset=['CustomerID'], inplace=True)

        # Calculate total spend per invoice
        data['TotalSum'] = data['Quantity'] * data['Price']

        # Transform the InvoiceDate to datetime type
        data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

        return data

    def calculate_rfm(self, data):
        snapshot_date = data['InvoiceDate'].max() + pd.DateOffset(days=1)  # latest date in the data plus one day
        rfm = data.groupby(['CustomerID']).agg({
            'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
            'InvoiceNo': 'count',  # Frequency
            'TotalSum': 'sum'})  # Monetary Value

        rfm.rename(columns = {'InvoiceDate': 'Recency',
                              'InvoiceNo': 'Frequency',
                              'TotalSum': 'MonetaryValue'}, inplace=True)
        return rfm

    def initiate_data_transformation(self):
        try:
            # Load data
            data = pd.read_csv(self.data_transformation_config.data_file_path)

            # Preprocess data
            data = self.preprocess_data(data)

            # Calculate RFM values
            rfm = self.calculate_rfm(data)

            return rfm
        except Exception as e:
            raise CustomException(e, sys)
