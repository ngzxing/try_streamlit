import streamlit as st
import mysql.connector
import pandas as pd

def query_data(query, cnx):
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_data = pd.DataFrame(result, columns=cursor.column_names)
    cursor.close()
    return result_data

st.title('Testing MySQL with Python')

# setting up connection to MySQL
cnn = mysql.connector.connect(user='root', password='12345')

st.sidebar.title('Tables')
st.sidebar.write('Select a table to view')
with st.sidebar:
    choice = st.selectbox('Select a table',['brands','categories','customers','order_items','orders','products','staffs','stocks','stores'])

st.write('Showing the', choice, 'table')
query = 'SELECT * FROM bikestore.' + choice
result = query_data(query, cnn)

st.dataframe(result, width=2000)

q = st.text_area('SQL Query', '''''' )
if q != '':
    st.dataframe(query_data(q, cnn), width=2000)