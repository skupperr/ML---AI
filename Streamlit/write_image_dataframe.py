import streamlit as st
import os
import pandas as pd

st.write("Hello, Streamlit! 12345678")
"Hello world"
st.write({"key": "value"})
st.write([1, 2, 3])
st.write(True)
st.write(123)

x = False
if x:
    st.write("x is True")
else:
    st.write("x is False")


st.title("Super Simple Title") 
st.header("This is a header") 
st.subheader('Subheader') 
st.markdown("**This** is _Markdown_") 
st.caption("small text") 

code_example = """
def greet (name): 
    print('hello', name) 
"""
st.code(code_example, language="python") 
st.divider()


### Image 
st.image("img/1.png", caption="Valorant", width=500)


### Pandas dataframe
st.subheader("Dataframe")
df = pd.read_csv("img/data.csv")
st.dataframe(df)


### Edit dataframe
st.subheader("Edit dataframe")
st.data_editor(df, num_rows="dynamic", use_container_width=True, hide_index=True, key="data_editor")


### Static table
st.subheader("Static table")
st.table(df)


# Metrics Section 
st.subheader("Metrics") 
st.metric (label="Total Rows", value=len(df)) 
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))




# Every time a button is pressed, the script reruns from the top.
pressed = st.button("Press me", key="button1")
print("First:", pressed)

pressed2 = st.button("Press me", key="button2")
print("Second:", pressed2)