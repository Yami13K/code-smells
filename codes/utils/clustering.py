import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples, silhouette_score


def kmeans(scores_df, cluster_num):
    # Assuming 'scores_df' is a Pandas DataFrame containing the 1D data in the 'Score' column
    data = scores_df[["Score"]].values

    # Create and fit K-means model
    kmeans = KMeans(n_clusters=cluster_num)
    kmeans.fit(data)

    # Get cluster assignments for the data points
    cluster_labels = kmeans.labels_

    # Cluster centers
    centroids = kmeans.cluster_centers_

    # Print cluster assignments for each data point
    scores_df["Cluster"] = cluster_labels

    return scores_df, centroids


def custom_distribution_plot(results):
    # Get the cluster results
    cluster_labels = results["Cluster"].values

    # Count the occurrences of each cluster label
    cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

    # Create a bar plot using Plotly Express
    fig = px.bar(
        x=cluster_counts.index,
        y=cluster_counts.values,
        labels={"x": "Cluster", "y": "Count"},
        title="Distribution of Clusters",
        text=cluster_counts.values,
        color=cluster_counts.index,  # Use cluster index for color mapping
        color_discrete_sequence=px.colors.qualitative.D3,  # Choose a colorscale
    )

    # Set the position of x-axis labels
    fig.update_xaxes(
        tickmode="array", tickvals=cluster_counts.index, ticktext=cluster_counts.index
    )

    # Add a grid to the plot
    fig.update_layout(yaxis_gridcolor="lightgray", xaxis_gridcolor="lightgray")
    fig.update_layout(title_x=0.4)
    # Show the plot using Streamlit
    st.plotly_chart(fig)


def elbow_plot(data, max_clusters=10):
    distortions = []

    for i in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=i, random_state=0)
        kmeans.fit(data)
        distortions.append(kmeans.inertia_)

    plt.figure(figsize=(8, 6))
    plt.plot(range(1, max_clusters + 1), distortions, marker="o")
    plt.title("Elbow Plot")
    plt.xlabel("Number of Clusters")
    plt.ylabel("Distortion")
    st.pyplot(plt)


def centroids_plot(result, centroids):
    # Get cluster labels for each data point
    # result['Cluster'] = result['Cluster'].str.replace('Cluster ', '')
    # Plot the clustered data
    plt.scatter(result['Score'], [0] * len(result), c=result['Cluster'].astype(int), cmap='viridis', s=50)
    plt.scatter(centroids, np.zeros(len(centroids)), c='red', marker='x', s=200,
                label='Cluster Centers')
    plt.xlabel('Score')
    plt.title('Clustered Data in 1D Space')
    plt.legend()
    st.pyplot(plt)


def plot_silhouette(data, labels):
    """
    Calculate the silhouette score and create a silhouette plot for a given clustering.

    Parameters:
    - data: The data points to be clustered.
    - labels: The cluster labels for each data point.
    """
    silhouette_avg = silhouette_score(data, labels)
    sample_silhouette_values = silhouette_samples(data, labels)

    fig, ax = plt.subplots(figsize=(8, 6))
    y_lower = 10

    for i in range(np.max(labels) + 1):
        ith_cluster_silhouette_values = sample_silhouette_values[labels == i]
        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = plt.cm.nipy_spectral(float(i) / np.max(labels))
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                         0, ith_cluster_silhouette_values,
                         facecolor=color, edgecolor=color, alpha=0.7)

        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
        y_lower = y_upper + 10

    ax.set_xlabel("Silhouette Coefficient")
    ax.set_ylabel("Cluster")
    ax.set_title("Silhouette Plot")
    ax.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax.set_yticks([])

    st.pyplot(plt)

