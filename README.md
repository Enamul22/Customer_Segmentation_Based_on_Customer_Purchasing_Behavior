# Customer_Segmentation_Based_on_Purchasing_Behavior

# Customer Segmentation Based on Purchasing Behavior

## Introduction

This repository contains code and resources for a customer segmentation project using the Online Retail II dataset. The aim of the project is to segment customers into different groups based on their purchasing behavior (Recency, Frequency, and Monetary value - RFM).

## Data

The data used in this project is the [Online Retail II Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) from the UCI Machine Learning Repository. This dataset contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011. The company mainly sells unique all-occasion gift-ware.

## Methodology

1. **Data Preprocessing**: The data is preprocessed by removing canceled orders, removing rows with missing `CustomerID`, and calculating total spend per invoice.

2. **Feature Engineering**: RFM features are calculated for each customer. Recency is calculated as the number of days between the customer's latest order and the end of the period under study. Frequency is the number of purchases made by the customer, and Monetary Value is the total spend by the customer.

3. **Modeling**: A KMeans clustering model is trained on the RFM data to segment the customers into different groups. The number of clusters is set based on the silhouette score.

## Results

The KMeans clustering model groups the customers into X different segments. (Provide a brief overview of the characteristics of each segment).

## Discussion

Discuss the implications of the customer segmentation. How could this information be used to improve business outcomes?

## Setup and Usage

Explain how to setup and run your project. Include information about necessary packages, how to install them, and how to run the project.

## Future Work

Discuss any planned improvements or additions to the project.

## License

Include any information about the license for your project.
