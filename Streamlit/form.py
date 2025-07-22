import streamlit as st
from datetime import datetime

st.title("Form")

form_info = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
}

with st.form(key="form"):
    form_info["name"] = st.text_input("Name")
    form_info["height"] = st.number_input("Height (cm)", min_value=0, max_value=300, value=170)
    form_info["gender"] = st.selectbox("Gender", ['Male', 'Female'])
    form_info["dob"] = st.date_input("Date of Birth", max_value= datetime.now(), min_value = datetime(1900, 1, 1))
    
    
    submit_button = st.form_submit_button(label="Submit")

    if(submit_button):
        if not all(form_info.values()):
            st.error("Please fill all the fields")
        else:
            st.balloons()
            st.success("Form submitted successfully")

            for key, values in form_info.items():
                st.write(f"{key}: {values}")