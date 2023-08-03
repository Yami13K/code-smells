
from sklearn.cluster import KMeans

from codes.utils.clustering import *
from config.static import WARNING


def clusterize(scores_df):
    def reset():
        button_placeholder.empty()
        clusters_input.empty()
        title.title("Clustering Metrics Visualisation")

    if scores_df is not None:
        spinner = st.spinner("Clustering...")

        with open("static/clustering.css", "r") as css_file:
            st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

        _, col = st.columns([1, 13])
        with col:
            title = st.empty()

        title.title("Select Maintenance Specificity")

        _, text_col, _ = st.columns([4, 1.5, 5])

        with text_col:
            clusters_input = st.empty()
            cluster_num = clusters_input.number_input(
                ' clustering num',min_value=2, max_value=10, value=3
            )
        _, button_col = st.columns([10, 20])

        with button_col:
            button_placeholder = st.empty()

        button = button_placeholder.button("Show Metrics!")
        if button:
            reset()
            _, text_col, _ = st.columns([4, 2.5, 5])
            with text_col:
                with spinner:
                    result, centroids = kmeans(scores_df, cluster_num)
            st.balloons()

            centroids_plot(result, centroids)
            custom_distribution_plot(result)
            elbow_plot(scores_df)
            data = np.array(scores_df['Score']).reshape(-1,1)
            label = np.array(scores_df['Cluster'])
            plot_silhouette(data, label)

            _, button_col = st.columns([13, 20])
            # reset_button_style = """
            #     background-color: #f44336; /* Red color */
            #     color: white;
            #     padding: 0.5rem 1rem;
            #     border: none;
            #     border-radius: 0.25rem;
            #     cursor: pointer;
            #     transition: background-color 0.3s ease;
            #     font-size: 1rem;
            #     font-weight: bold;
            #     text-align: center;
            #     text-decoration: none;
            #     display: inline-block;
            #     margin: 0.2rem;
            # """

            # Apply the style to the reset button using the 'style' parameter
            with button_col:
                if st.button("Reset", key="reset_button"):
                    clusterize(scores_df)




    else:
        st.warning(WARNING)
