import plotly.express as px
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def custom_distribution_plot(results):
    st.title('Clustering Metrics Visualisation')

    # Get the cluster results
    cluster_labels = results['Cluster'].values

    # Count the occurrences of each cluster label
    cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()

    # Create a bar plot using Plotly Express
    fig = px.bar(
        x=cluster_counts.index,
        y=cluster_counts.values,
        labels={'x': 'Cluster', 'y': 'Count'},
        title='Distribution of Clusters',
        text=cluster_counts.values,
        color=cluster_counts.index,  # Use cluster index for color mapping
        color_discrete_sequence=px.colors.qualitative.D3 # Choose a colorscale
    )

    # Set the position of x-axis labels
    fig.update_xaxes(tickmode='array', tickvals=cluster_counts.index, ticktext=cluster_counts.index)

    # Add a grid to the plot
    fig.update_layout(yaxis_gridcolor='lightgray', xaxis_gridcolor='lightgray')
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
    plt.plot(range(1, max_clusters + 1), distortions, marker='o')
    plt.title('Elbow Plot')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Distortion')
    st.pyplot(plt)
