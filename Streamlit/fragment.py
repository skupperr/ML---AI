import streamlit as st

# When we press a button or toggle and interact with checkbox, the whole script reruns
# But if we use fragment, only the fragmented part reruns


# In this function, when we interact with toggle, only the script inside the function reruns
@st.fragment()
def toggle_and_text():
    with st.container(border=True):
        st.toggle("Toggle")
        st.text_area("Enter text")
        print("Toggling")


# In this function, when we interact with checkbox, only the script inside the function reruns
@st.fragment()
def filter_and_file():
    with st.container(border=True):
        st.checkbox("Filter")
        st.file_uploader("Upload file")
        st.selectbox("Choose option", ['Option 1', 'Option 2', 'Option 3'])
        st.slider("Select Values", 0, 100, 50)
        st.text_input("Enter text")
        print("filtering")



toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)

# since this button isn't included in fragmented function, pressing this will result in rerunning of the entire script
cols[1].button("Update")
filter_and_file()