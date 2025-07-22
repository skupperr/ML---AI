import streamlit as st

# When a button is pressed the script is rerun. If we use callback function, when the button is pressed, first the function gets executed and then script reruns from the top 

if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def next_step(name):
    st.session_state.step = 2
    st.session_state.info["name"] = name

def previous_step():
    st.session_state.step = 1


if(st.session_state.step == 1):
    st.write("Please enter your name.")
    name = st.text_input("Name", key="name", value=st.session_state.info.get("name", ""))

    st.button("Next", on_click= next_step, args=(name, ))

if(st.session_state.step == 2):
    st.header("Part 2: Review")
    st.subheader("Please review your information.")
    st.write(f"**Name:** {st.session_state.info['name']}")

    if st.button("Submit"):
        st.success("Information submitted successfully!")
        st.balloons()
        st.session_state.info = {}
    
    st.button("Back", on_click=previous_step)
