import streamlit as st
import numpy as np
import pandas as pd

from config.static import SUB_CATEGORIES


def ahp_view():
    #     st.dataframe(df)
    with open("static/ahp.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

    # Page title and description
    st.title("AHP Matrix Input")
    st.write("Enter your opinions for each code smell in proportion to each other:")

    # Initialize sub-categories and the AHP matrix
    sub_categories = SUB_CATEGORIES

    matrix = np.ones((5, 5))
    # Create layout with columns
    col1, col2 = st.columns(2)

    # Left column for selections
    with col1:
        # Create collapsible sections (expanders) for each sub-category
        for i in range(5):
            expander = st.expander(sub_categories[i], expanded=False)
            with expander:
                for j in range(i, 5):
                    if i == j:
                        matrix[i][j] = 1.0
                    else:
                        matrix[i][j] = st.number_input(
                            f"{sub_categories[i]} / {sub_categories[j]}",
                            min_value=0.1,
                            max_value=10.0,
                            step=0.1,
                            key=f"{i}-{j}",
                        )

    # Fill the lower triangular part of the matrix with reciprocal values
    for i in range(5):
        for j in range(i):
            matrix[i][j] = 1 / matrix[j][i]

    # Display the matrix for verification
    with col2:
        df = pd.DataFrame(matrix, columns=sub_categories, index=sub_categories)
        # st.dataframe(df.style.set_table_styles([{'selector': '.row_heading', 'props': 'background-color: #f0f0f0; font-weight: bold;'}, {'selector': '.data', 'props': 'background-color: #ffffff;'}]))
        # Convert the DataFrame to an HTML table
        table_html = df.to_html(classes="custom-dataframe", index=False)
        # Display the DataFrame with custom styling
        st.markdown(table_html, unsafe_allow_html=True)

        st.button("Submit", key="submit_button")



if __name__ == "__main__":
    ahp_view()
