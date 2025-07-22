import streamlit as st

# when a button is clicked, the script is rerun from the top, and the counter variable is reset to 0.
# This is a common issue in Streamlit applications where the state of variables is not preserved across reruns.
# The problem with this code is that the counter variable is reset to 0 every time the script runs.


counter = 0
st.write(f"Counter: {counter}")

if st.button("Increment", key="btn1"):
    counter += 1
    st.write(f"Counter incremented to: {counter}")
else:
    st.write("Counter not incremented")

st.divider()

# To fix this, we can use Streamlit's session state to store the counter variable. This way, the value of the counter will persist across reruns of the script.

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment", key="btn2"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to: {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")