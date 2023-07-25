import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score
import pickle
import os

def train_model(rfm, n_clusters=3):
    # Normalize the data
    scaler = StandardScaler()
    rfm_normalized = scaler.fit_transform(rfm)

    # Train the model
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(rfm_normalized)

    # Evaluate the model
    silhouette_avg = silhouette_score(rfm_normalized, kmeans.labels_)
    print("For n_clusters =", n_clusters,
          "The average silhouette_score is :", silhouette_avg)

    # Save the model
    model_file_path = os.path.join("models", "kmeans.pkl")
    with open(model_file_path, 'wb') as file:
        pickle.dump(kmeans, file)
    
    return kmeans
