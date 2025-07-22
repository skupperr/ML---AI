import streamlit as st
import time

# for 60 seconds in the session, the data will be available without the need to fetch every time the page reloads

@st.cache_data(ttl=60)
def fetch_data():
    # simulate a slow data fetching process
    time.sleep(5)
    return {"data": "this is a cached data"}

st.write("fetching data")
data  = fetch_data()
st.write(data)