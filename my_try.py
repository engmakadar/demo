import streamlit as st
import os
import plotly.express as px
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


st.set_page_config(page_icon= ':bar_chart:', page_title='EDA Web based', layout='wide', initial_sidebar_state='auto')

st.markdown('### :bar_chart:   Development Web App for Data Analytical with Mechine Learning :earth_africa:')
st.markdown('---')

file_uploader = st.file_uploader(":file_folder: Upload your file", type=['csv', 'txt', 'xls', 'xlsx'])


#RAW Matrix

st.markdown("Matrix")
colu, colu2, colu3, colu4, colu5 = st.columns((5))
colu.metric("Tempreture", "71.8 °F", "1.2 °F")
colu2.metric("Wind", "64.2 mph", "-8%")
colu3.metric("Humidity", "37.0 °C", "2.4 °C")
colu4.metric("Raining", "92.3 °F", "3.2 °F")
colu5.metric("Humidity", "86%", "-12%")


if file_uploader is not None:
    filename = file_uploader.name
    st.write(filename)
    df = pd.read_csv(filename, encoding='ISO-8859-1')
else:
    os.chdir('/Users/mkhashi/Desktop/Training/demo1')
    df = pd.read_csv('superstore.csv', encoding='ISO-8859-1')


col, col1, col2 = st.columns((3))
df['Order Date'] = pd.to_datetime(df['Order Date'])

starting_date = pd.to_datetime(df['Order Date'].min())
end_date = pd.to_datetime(df['Order Date'].max())

with col1:
    date1 = pd.to_datetime(st.date_input('Starting Date', starting_date))
with col2:
    date2 = pd.to_datetime(st.date_input('Ending Date', end_date))
    
with col:
    names = st.selectbox('Date of the release Year',( 2009, 2010, 2011, 2012))

df = df[(df['Order Date']>= date1) & (df['Order Date']<= date2)].copy()


# st.sidebar.header('Choose your Filter')
# region = st.sidebar.multiselect("Pick your Region", df['Region'].unique())


with st.sidebar:
    st.header("Input `Features`")
    region = st.sidebar.multiselect("Pick your Region", df['Region'].unique())
    gender = st.selectbox('Gender', ('Male', 'Female', 'Not Prefer'))
    bill_leng = st.slider('Bill Length (mm)',3.61,3.25, 59.6,43.6)
    data_cap = st.slider('Data for Movement Process', 75,23,3,43)
    

if not region:
    df3 = df.copy()
else:
    df3= df[df['Region'].isin(region)]

    

category_df = df3.groupby(by=['State'], as_index = False)['Sales'].sum()


with col1:
    # st.subheader("Category with Sales Prices")
    st.markdown(':chart: Departmental state along with Sales Prices')
    fig = px.bar(category_df, x='State', y='Sales', text = ['${:,.5f}'.format(x) for x in category_df['Sales']],
             template ='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 500)


with col2:
    # st.header("Region wise Sales")
    st.markdown(':city_sunrise: Reginal state by their jiho ')
    fig = px.pie(df3, values='Sales', names='Region', hole=0.5)
    fig.update_traces(text = df3['Region'], textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with col:
    # st.subheader("Category with Sales Prices")
    st.markdown(':sparkle: Departmental states with line charts compared to Sales ')
    fig = px.line(category_df, x='State', y='Sales', text = ['${:,.5f}'.format(x) for x in category_df['Sales']],
             template ='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 500)
    
    
    

with col:
    # st.subheader("Category with Sales Prices")
    st.markdown(':chart: Departmental state along with Sales Prices')
    fig = px.bar(category_df, x='State', y='Sales', text = ['${:,.5f}'.format(x) for x in category_df['Sales']],
             template ='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 500)


with col2:
    # st.subheader("Category with Sales Prices")
    st.markdown(':sparkle: Departmental states with line charts compared to Sales ')
    fig = px.line(category_df, x='State', y='Sales', text = ['${:,.5f}'.format(x) for x in category_df['Sales']],
             template ='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 500) 
    
with col1:
    # st.header("Region wise Sales")
    st.markdown(':city_sunrise: Reginal state by their jiho ')
    fig = px.pie(df3, values='Sales', names='Region', hole=0.5)
    fig.update_traces(text = df3['Region'], textposition='outside')
    st.plotly_chart(fig, use_container_width=True)    
    


with st.expander('Data visusalization'):
    st.scatter_chart(data=df, x='City', y='Sales', color='#1E90FF')

with st.expander('Data Visualization by capturing the AI/ML Pionts'):
    st.bar_chart(data=df, x='State', y='Sales')

