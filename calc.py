import pandas as pd
import numpy as np

def calculate_sse_element(data, centroids, cluster_column):
    data['Distancia_Quadrada'] = 0.0
    
    for cluster_label, centroid in centroids.items():
        cluster_data = data[data[cluster_column] == cluster_label] # Filtra os dados do cluster atual
        distances = np.sum((cluster_data.drop(columns=[cluster_column, 'Distancia_Quadrada']) - centroid) ** 2, axis=1) # distancia quadrada de cada ponto ao centroide
        data.loc[data[cluster_column] == cluster_label, 'Distancia_Quadrada'] = distances
    return data

def main():
    data = pd.read_csv('arquivo.csv')
    cluster_column = 'Cluster'
    centroids = {
        1: np.array([147, 42, 17, 57]),  # Centroide do Cluster 1
        2: np.array([190, 100, 38, 105])   # Centroide do Cluster 2
    }
    result = calculate_sse_element(data, centroids, cluster_column)
    print(result)

if __name__ == "__main__":
    main()