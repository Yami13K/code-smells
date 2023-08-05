import streamlit as st

from codes.utils.ahp import load_json_matrix, save_matrix_json
from codes.utils.general import styler, toast
from config.paths import MAPPING_DICT_PATH


def ck_mapper_view():
    styler('mapper')

    criteria = [
        "Modularity",
        "Analyzability",
        "Testability",
        "Reusability",
        "Modifiability",
    ]
    metrics = ["WMC", "DIT", "NOC", "CBO", "RFC", "LCOM"]

    # Dictionary to store selected metrics for each criterion
    selected_metrics = {}

    for criterion in criteria:
        st.subheader(criterion)

        # Select metrics for the current criterion
        selected_metrics[criterion] = st.multiselect(
            f"Select metrics for {criterion}", metrics, default=[]
        )

    # Submit button
    if st.button("Submit"):
        # Check if all criteria have selected metrics
        if all(selected_metrics.values()):
            toast('Map Dictionary')
            st.write("Selected Metrics:")
            save_matrix_json(selected_metrics, MAPPING_DICT_PATH)
            st.write(selected_metrics)
        else:
            st.error("Error: All fields should have values!")


if __name__ == "__main__":
    ck_mapper_view()
