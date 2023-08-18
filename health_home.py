import streamlit as st
import pandas
st.title('Healthcare')
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
"""
)


Module = ["Module 1", "Module 2", "Module 3", "Module 4"]
selected_Module = st.selectbox("Select Module:", Module)

st.write("You selected:", selected_Module)


# Apply custom CSS styling using HTML
custom_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
    }
    .custom-container {
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Create a container with custom styling
st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
st.title("Custom Styled UI with Streamlit")
st.write("This is a custom-styled container.")
st.button("Click me")
st.markdown("</div>", unsafe_allow_html=True)
