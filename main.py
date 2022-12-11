import streamlit as st
import pandas as pd
import plotly.express as px

# reading given data
data = pd.read_csv("b_depressed.csv")

st.title('DSBA project')
st.subheader('Healthy and depressed people')
st.write('Table with a short info.')
st.write(data.head())
st.write('This table shows statistics of various life factors of healthy and sick people.')
st.write('')

# printing of mean, median and standard of age, number of children and education level of people with depression
st.subheader('Mean, median and standard deviation of the age, number of children and education level of respondents')
st.write(data[["Age", "Number_children", "education_level"]].describe().loc[['mean', '50%', 'std']])
st.write('')

# data cleanup
data.dropna()

# 1st simple plot - histogram
st.subheader('3 simple plots to give an idea of what the data looks like')
st.subheader('Histogram')
st.write('This graph shows the level of education among interviewees.')
fig = px.histogram(data, x="education_level")
st.plotly_chart(fig)
st.write('As we can see, the most people have 10th level of education.')
st.write('')

# 2nd simple plot - scatter chart
st.subheader('Scatter chart')
st.write('This chart shows living expenses of respondents.')
fig = px.scatter(data, x="living_expenses", y="Survey_id")
st.plotly_chart(fig)
st.write('This scatter graph has a strange line on itself. I believe that it is necessary to clear the graph from this line, for a more accurate analysis.')

# There is a strange line, let's delete it
data['living_expenses'] = pd.to_numeric(data['living_expenses'])
data = data.loc[data['living_expenses'] != 26692283]

fig = px.scatter(data, x="living_expenses", y="Survey_id")
st.plotly_chart(fig)
st.write('Now it is clear. We can clearly see the living expenses of respondents. It also should be mentioned that less people spend more money.')
st.write('')

# 3rd simple plot - pie chart
st.subheader('Pie chart')
fig = px.pie(data, names='total_members')
st.plotly_chart(fig)
st.write('This chart shows how many members are in the families of respondents.')
st.write('As it can be seen from this chart only 0.438% of interviewees have 11 members in their families.')
st.write('It also should be mentioned that the difference between people who have 4 and 5 members is only 0.1%.')
st.write('')

# 1st complex plot - bar chart
st.subheader('Detailed overview')
st.subheader('Bar chart')
st.write('As it can be seen from this chart, the most depresive group is group of people who have 5 members in their families.') 
st.write('We can also observe a strange fact that people with 11 members of famile are never depressed.')
fig = px.bar(data, x='total_members', y='depressed')
st.plotly_chart(fig)
st.write('')

# 2nd complex plot - violin chart
st.subheader('Violin chart')
st.write('Analyzing this chart, we can find that the most depressed people are among women of the middle age of 25 years.')
st.write('Also, we can find out that most men get depressed around the age of 40.') 
st.write('Also, regardless of gender, fewer people suffer from depression with age.')
fig = px.violin(data, x="sex", y="Age", color="depressed")
st.plotly_chart(fig)
st.write('Reference Information')
st.write('If gender is 0, then it is male; if gender is 1, then it is female. If depressed is 0, then a person not suffering from depression; if depressed is 1, then a person suffering  from depression')
