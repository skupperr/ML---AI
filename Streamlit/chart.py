import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualization with Streamlit")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.dataframe(chart_data, use_container_width=True)

# Area chart
st.subheader("Area Chart")
st.area_chart(chart_data, use_container_width=True)

# Bar chart 
st.subheader("Bar Chart")
st.bar_chart(chart_data, use_container_width=True)

# Line chart
st.subheader("Line Chart")
st.line_chart(chart_data, use_container_width=True)

# scatter plot
st.subheader("Scatter Plot")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})
st.scatter_chart(scatter_data, use_container_width=True)

# Histogram
st.subheader("Histogram")
hist_data = pd.DataFrame(
    np.random.randn(100, 1),
    columns=["x"]
)
st.bar_chart(hist_data, use_container_width=True)

# Map
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data, use_container_width=True)

# Pie chart
st.subheader("Pie Chart")
pie_data = pd.Series([1, 2, 8, 4], index=["A", "B", "C", "D"])
fig, ax = plt.subplots()
ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title("Pie Chart Example")
st.pyplot(fig, use_container_width=True)
