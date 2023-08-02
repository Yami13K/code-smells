from pycaret.clustering import *

import streamlit as st
from codes.utils.general import custom_distribution_plot, title_plot, toggle_button
from config.static import SESSION_STATE


def clusterize(scores_df):
	exp_clu = setup(data=scores_df, session_id=123, preprocess=False, normalize=False)
	kmeans = create_model("kmeans", num_clusters=4)
	result = assign_model(kmeans)
	cluster = st.button('Clusterize')
	if cluster:
		title_plot(kmeans, 'silhouette')
		title_plot(kmeans, 'elbow')
		title_plot(kmeans, 'distribution')


