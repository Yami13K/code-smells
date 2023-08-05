from sklearn.cluster import KMeans

from codes.utils.clustering import *
from codes.utils.general import styler
from config.static import WARNING

from pycaret.clustering import *


def clusterize(scores_df):
    def reset():
        button_placeholder.empty()
        clusters_input.empty()
        title.title("Clustering Metrics Visualisation")

    if scores_df is not None:
        spinner = st.spinner("Visualising...")

        styler("clustering")

        _, col = st.columns([1, 13])
        with col:
            title = st.empty()

        title.title("Select Maintenance Specificity")

        _, text_col, _ = st.columns([4, 1.5, 5])

        with text_col:
            clusters_input = st.empty()
            cluster_num = clusters_input.number_input(
                " clustering num", min_value=2, max_value=10, value=3
            )
        _, button_col = st.columns([10, 20])

        with button_col:
            button_placeholder = st.empty()

        button = button_placeholder.button("Show Metrics!")
        if button:
            reset()

            with spinner:
                clusterize_pycaret(scores_df, cluster_num)
                result, centroids = kmeans(scores_df, cluster_num)
                custom_distribution_plot(result)
                centroids_plot(result, centroids)
            # st.balloons()

            _, button_col = st.columns([13, 20])
            with button_col:
                if st.button("Reset", key="reset_button"):
                    clusterize(scores_df)

    else:
        st.warning(WARNING)


def clusterize_pycaret(scores_df, num):
    exp_clu = setup(data=scores_df, session_id=123, preprocess=False, normalize=False)
    kmeans = create_model("kmeans", num_clusters=num)
    result = assign_model(kmeans)
    plot_model(kmeans, "elbow", display_format="streamlit")
    plot_model(kmeans, "silhouette", display_format="streamlit")
