import time

import streamlit as st

from codes.utils.general import styler


def git_url_view():
    styler('git')

    st.title("GitHub Repo URL Submission")
    # Create two columns layout
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed

    # Add a text input field
    github_repo_url = col1.text_input("Enter GitHub Repo URL", "")

    # Add a submit button in the second column
    submit = col2.button("Submit")

    if submit:
        if github_repo_url:
            success_message = st.success(f"Successfully Submitted: {github_repo_url.split('/')[-1]}")
            time.sleep(3)  # Display success message for 3 seconds
            success_message.empty()  # Clear the success message
        else:
            st.warning("Please enter a GitHub repo URL.")

if __name__ == "__main__":
    git_url_view()
