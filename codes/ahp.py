import streamlit as st
import numpy as np
import pandas as pd

from codes.utils.general import styler
from config.static import SUB_CATEGORIES


def ahp_view():
    styler('ahp')

    st.title("AHP Matrix Input")
    st.write("Enter your opinions for each code smell in proportion to each other:")

    sub_categories = SUB_CATEGORIES

    matrix = np.ones((5, 5))
    col1, col2 = st.columns(2)

    with col1:
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

    for i in range(5):
        for j in range(i):
            matrix[i][j] = 1 / matrix[j][i]

    with col2:
        df = pd.DataFrame(matrix, columns=sub_categories, index=sub_categories)
        table_html = df.to_html(classes="custom-dataframe", index=False)
        st.markdown(table_html, unsafe_allow_html=True)

        st.button("Submit", key="submit_button")
