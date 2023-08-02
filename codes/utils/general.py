import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from pycaret.clustering import plot_model


def softmax(x):
    # Numerical stability: subtract the maximum value from each element
    # to avoid large exponential values that might cause overflow.
    max_x = np.max(x)
    x_exp = np.exp(x - max_x)
    sum_x_exp = np.sum(x_exp)
    softmax_output = x_exp / sum_x_exp
    return softmax_output


class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


def toggle_button(
    session_state: SessionState,
    session_var: str,
    title: str,
    data,
    button_text: str = "Toggle",
):
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
    col1.title(title)

    # Add a button to show/hide the DataFrame
    if col2.button(button_text, key=session_var):
        if not hasattr(session_state, session_var):
            setattr(session_state, session_var, True)  # Initialize state variable

        setattr(session_state, session_var, not getattr(session_state, session_var))

    # Display DataFrame based on button state
    if hasattr(session_state, session_var) and getattr(session_state, session_var):
        if isinstance(data, pd.DataFrame):
            st.dataframe(data)
        else:
            st.pyplot(data)


def title_plot(results, plot: str):
    st.title(plot.capitalize() + 'Plot')
    # Create the plot using plot_model from PyCaret
    plot_model(results, plot=plot)


def custom_distribution_plot(results):
    st.title('Custom Distribution Plot')

    # Get the cluster results
    cluster_labels = results['Cluster'].values

    # Create a histogram of cluster assignments
    plt.hist(cluster_labels, bins=np.arange(0.5, len(np.unique(cluster_labels)) + 1.5) - 0.5, alpha=0.7)

    plt.xlabel('Cluster')
    plt.ylabel('Count')
    plt.title('Distribution of Clusters')
    plt.xticks(np.unique(cluster_labels))
    plt.grid(True)

    # Display the plot using Streamlit
    st.pyplot(plt.gcf())