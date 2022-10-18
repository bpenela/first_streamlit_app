import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector

#Variables
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruityvice_response = rq.get('https://fruityvice.com/api/fruit/' + 'kiwi')

st.title('Bruno & Di Restaurant')

st.header(' Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# Item picker
fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Choosen Items
if (len(fruits_to_show) > 0):
  st.dataframe(fruits_to_show)

st.header('Fruityvice Fruit Advice')
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
fruityvice_response = rq.get('https://fruityvice.com/api/fruit/' + fruit_choice)
st.write('The user entered ', fruit_choice)

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)
