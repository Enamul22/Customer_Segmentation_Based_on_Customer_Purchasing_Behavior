# Customer_Segmentation_Based_on_Purchasing_Behavior

## Introduction

This repository contains code and resources for a customer segmentation project using the Online Retail II dataset. The aim of the project is to segment customers into different groups based on their purchasing behavior (Recency, Frequency, and Monetary value - RFM) and make business decision based on their purchasing behavior. 

## Data

The data used in this project is the [Online Retail II Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) from the UCI Machine Learning Repository. This dataset contains all the transactions occurring for a UK-based and registered, non-store online retail between 01/12/2009 and 09/12/2011. The company mainly sells unique all-occasion gift-ware.

## Methodology

1. **Data Preprocessing**: The data is preprocessed by removing canceled orders, removing rows with missing `CustomerID`, and calculating total spend per invoice.

2. **Feature Engineering**: RFM features are calculated for each customer. Recency is calculated as the number of days between the customer's latest order and the end of the period under study. Frequency is the number of purchases made by the customer, and Monetary Value is the total spend by the customer.

3. **Modeling**: A KMeans clustering model is trained on the RFM data to segment the customers into different groups. The number of clusters is set based on the silhouette score.

## Results

The KMeans clustering model groups the customers into 5 different segments.

Cluster 0 (3130 customers): These customers have a low recency (43.3), high frequency (80.5), and high monetary value (265.1), which suggests that they are regular and loyal customers. They've made a purchase quite recently, they make purchases frequently, and they tend to spend a decent amount of money. These customers are very valuable, and it would be beneficial to keep them engaged with loyalty programs, personalized offers, and excellent customer service.

Cluster 1 (1062 customers): These customers have high recency (245.2), low frequency (27.8), and low monetary value (137.0). These customers haven't made a purchase in quite a while, and when they did, they didn't make purchases often and didn't spend a lot. They could be customers who have stopped shopping. It might be worth reaching out to these customers with re-engagement campaigns or surveys to discover why they stopped shopping.

Cluster 2 (6 customers): These customers have a moderate recency (138.8), low frequency (27.5), and very high monetary value (27446.7). This small group of customers don't make purchases often, but when they do, they spend a lot of money. These could be bulk buyers or wholesale customers. It might be beneficial to reach out to these customers and build strong relationships with personalized service, as they could contribute significantly to the revenue due to their high spend.

Cluster 3 (179 customers): These customers have very low recency (17.3), high frequency (624.3), and high monetary value (2061.3). These are very active customers who make purchases frequently and spend a lot. They have made purchases very recently. These are high-value customers that should be retained. They could be targeted with loyalty programs and personalized marketing.

Cluster 4 (4 customers): These customers have extremely low recency (2.8), very high frequency (4323.2), and very high monetary value (24149.8). These customers make purchases extremely frequently and spend a lot of money. They have made purchases very recently. This is a very small but extremely valuable group of customers. Given their high frequency and spend, they could be corporate customers or super consumers. It would be worth building strong relationships with these customers and providing them with exceptional service.

## Setup and Usage

I set up my own vertual envorinment (venv) in vs code. I installed required packages inside venv. For the deployment of this project I used flask inside the app.py file. I build a simple graphical user interface using html to predict the segmentation.
