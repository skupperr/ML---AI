import streamlit as st

# Sidebar
st.sidebar.title("Sidebar Text")
st.sidebar.write("We can use Button, anything in here")

sidebar_input = st.sidebar.text_input("Enter your text in the sidebar", placeholder="Name:")

if(sidebar_input):
    st.write(f"You've written: {sidebar_input}")


# Tab
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in tab 1")
with tab2:
    st.write("You are in tab 2")
with tab3:
    st.write("You are in tab 3")


# Columns layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Content fot column 1")

with col2:
    st.header("Column 2")
    st.write("Content fot column 2")

with col3:
    st.header("Column 2")
    st.write("Content fot column 3")


# Container
with st.container(border=True):
    st.write("This is inside of a container")
    st.write("This is inside of a container")
    st.write("This is inside of a container")


# Dynamic text
x = st.empty()
x.write("It's useful for dynamic content. It can be changed later with a button for example")

if(st.button("Update placeholder")):
    x.write("Text is changed")


# Expander
with st.expander("Expand for details"):
    st.write("Hello")
    st.write("Hello")


# Tooltip
st.write("Hover over the button get a tool tip")
st.button("Button with Tooltip", help="Hello")