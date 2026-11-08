from sklearn.cluster import KMeans

X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [8, 8],
    [9, 8],
    [8, 9]
]

model = KMeans(n_clusters=2, random_state=0, n_init=10)

model.fit(X)

print("Cluster labels:", model.labels_)

print("Centroids:")
print(model.cluster_centers_)