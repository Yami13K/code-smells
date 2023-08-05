import streamlit as st

from codes.utils.general import styler


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
            st.write("Selected Metrics:")
            st.write(selected_metrics)
        else:
            st.error("Error: All fields should have values!")


if __name__ == "__main__":
    ck_mapper_view()
