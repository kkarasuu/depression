import streamlit as st
import pandas as pd
import plotly.express as px

# reading given data
data = pd.read_csv("b_depressed.csv")

st.title('Mid-term report')
st.subheader('Credit cards holders analys')
st.write('Table short info')
st.write(data.head())
st.write('This chart shows numbers of existing customers of specific age')

# printing of mean, median and standard of age, number of children and education level of people with depression
print(data[["Age", "Number_children", "education_level"]].describe().loc[['mean', '50%', 'std']])

# data cleanup
data.dropna()

# 1st simple plot - histogram
fig = px.histogram(data, x="education_level")
st.plotly_chart(fig)

# 2nd simple plot - scatter chart
fig = px.scatter(data, x="living_expenses", y="Survey_id")
st.plotly_chart(fig)

# There is a strange line, let's delete it
data['living_expenses'] = pd.to_numeric(data['living_expenses'])
data = data.loc[data['living_expenses'] != 26692283]

fig = px.scatter(data, x="living_expenses", y="Survey_id")
st.plotly_chart(fig)

# 3rd simple plot - pie chart
fig = px.pie(data, names='total_members')
st.plotly_chart(fig)

# 1st complex plot - bar chart
fig = px.bar(data, x='total_members', y='depressed')
st.plotly_chart(fig)

# 2nd complex plot - violin chart
fig = px.violin(data, x="sex", y="Age", color="depressed")
st.plotly_chart(fig)
