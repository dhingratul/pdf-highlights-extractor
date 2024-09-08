import streamlit as st
import os
from core import extract_highlights_from_file

st.title("PDF Highlight Extractor")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    # # Extract highlights
    highlights = extract_highlights_from_file(os.path.join("uploads", uploaded_file.name))
    # highlights = extract_highlights_from_doc(uploaded_file)

    # Display highlights
    st.markdown("## Extracted Highlights:")
    for highlight in highlights:
        st.markdown(f"- {highlight}")

    # # Download button
    # st.download_button(
    #     label="Download Highlights",
    #     data=highlights,
    #     file_name="highlights.txt",
    #     mime="text/plain",
    # )

# # Run the app
# if __name__ == "__main__":
#     app()
