import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Iris Dataset Explorer')

# Load the Iris dataset
data = sns.load_dataset('iris')

st.header('Raw Data')
st.dataframe(data)

st.header('Summary Statistics')
st.write(data.describe())

st.header('Species Count')
st.bar_chart(data['species'].value_counts())

st.header('Pairplot')
fig = sns.pairplot(data, hue='species')
st.pyplot(fig)

st.header('Custom Scatter Plot')
x_axis = st.selectbox('X Axis', data.columns[:-1])
y_axis = st.selectbox('Y Axis', data.columns[:-1], index=1)
fig2, ax = plt.subplots()
sns.scatterplot(data=data, x=x_axis, y=y_axis, hue='species', ax=ax)
st.pyplot(fig2) 