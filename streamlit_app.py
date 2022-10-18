import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

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
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error('Please select a fruit to get information')
   else:
    fruityvice_response = rq.get('https://fruityvice.com/api/fruit/' + fruit_choice)
    st.write('The user entered ', fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)

except URLError as e:
  st.error(=

           st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add')
if (add_my_fruit != ''):
  my_cur.execute("insert into fruit_load_list values ('"+ add_my_fruit +"');")
  st.write('Thanks for adding ', add_my_fruit)
