import streamlit as st
import pandas as pd
import plotly.express as px
st.sidebar.title("Studying Job Ads")

counts = pd.read_csv("counts.csv")
counts = counts.rename(columns={'index':'skill'})
# create the bar plot for the "keywords" column
st.subheader("Job Ad Keywords")
st.sidebar.success("Desenvolvido por Rafael Belokurows")
fig = px.bar(counts, x='pct', y=counts['skill'],text=counts['pct'].apply(lambda x: f'{x:,.2%}'), orientation='h')

# Customize the layout
fig.update_layout(
    title='Keyword Distribution in Job Ads',
    xaxis_title='Percstreamlit run appentage',
    yaxis_title='Keywords',
    margin=dict(l=100, r=20, t=70, b=70),
    xaxis_tickformat=".2%",
    width=700
)
fig.update_traces(hovertemplate='%{x:,.2%}')
# Show the plot
st.plotly_chart(fig)

st.write(counts.sort_values('pct',ascending=False).to_html(), unsafe_allow_html=True)
#Continuar análise de salário
#

# create the bar plot for the "place" column
#st.subheader("Job Ad Locations")
##place_value_counts = df["place"].value_counts()
#place_fig = px.bar(place_value_counts, x=place_value_counts.index, y=place_value_counts.values)
##place_fig.update_layout(xaxis_title="Location", yaxis_title="Count")
#st.plotly_chart(place_fig)

# create the bar plot for the "salary" column
#st.subheader("Job Ad Salaries")
#salary_value_counts = df["salary"].value_counts()
#salary_fig = px.bar(salary_value_counts, x=salary_value_counts.index, y=salary_value_counts.values)
#salary_fig.update_layout(xaxis_title="Salary", yaxis_title="Count")
#st.plotly_chart(salary_fig)