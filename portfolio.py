import streamlit as st

# Page configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Header
st.title("Hello, I'm Aashish! 👋")
st.subheader("A Data Scientist passionate about Machine Learning ")

# About Me Section
st.header("About Me")
st.write("""
Hi, I'm [Your Name]. I'm a [Your Role/Profession] with expertise in [Your Expertise].
I enjoy working on projects involving [Your Interests/Fields of Work].
""")

# Skills Section
st.header("Skills")
st.write("- **Programming:** Python, C++, Java, etc.")
st.write("- **Frameworks:** Django, Flask, Streamlit")
st.write("- **Other Skills:** Data Analysis, Machine Learning, Web Development")

# Projects Section
st.header("Projects")
project1 = """
- **Project Name 1**: Description of project 1.
  - [GitHub Repository](https://github.com/your-repo) | [Live Demo](https://your-app-url)
"""
st.write(project1)

project2 = """
- **Project Name 2**: Description of project 2.
  - [GitHub Repository](https://github.com/your-repo) | [Live Demo](https://your-app-url)
"""
st.write(project2)

# Experience Section
st.header("Experience")
st.write("**[Job Title]**, [Company Name] ([Start Date] - [End Date])")
st.write("- Bullet point 1 about your role")
st.write("- Bullet point 2 about your role")

# Contact Section
st.header("Contact Me")
st.write("Feel free to connect with me via:")
st.write("- **Email**: your.email@example.com")
st.write("- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)")
