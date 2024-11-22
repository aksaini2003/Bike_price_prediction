import streamlit as st

# Title of the app
st.title("Model Input Sliders with Right-Side Layout")

# Divide the page into two columns
col1, col2 = st.columns([2, 1])  # Left column (wider) and right column (narrower)

# Add content to the right column
with col2:
    st.header("Input Parameters")
    input1 = st.slider("Input 1", 0, 100, 50)
    input2 = st.slider("Input 2", 0, 100, 50)
    input3 = st.slider("Input 3", 0, 100, 50)
    input4 = st.slider("Input 4", 0, 100, 50)
    input5 = st.slider("Input 5", 0, 100, 50)

# Add content to the left column
with col1:
    st.subheader("Model Inputs Overview")
    st.write(f"Input 1: {input1}")
    st.write(f"Input 2: {input2}")
    st.write(f"Input 3: {input3}")
    st.write(f"Input 4: {input4}")
    st.write(f"Input 5: {input5}")
