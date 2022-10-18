import streamlit as st
import pandas as pd
import requests as rq
import snowflake.connector
from urllib.error import URLError

#Variables
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
fruityvice_response = rq.get('https://fruityvice.com/api/fruit/' + 'kiwi')

#Functions
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = rq.get('https://fruityvice.com/api/fruit/' + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

def insert_rows_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+ add_my_fruit +"');")
    return ('Thanks for adding '+ add_my_fruit)


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
    back_from_funcion = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_funcion)
    
except URLError as e:
  st.error()

st.header('The fruit load list contains:')
if :
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add')
if st.button ('Add  a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_function =  insert_rows_snowflake(add_my_fruit)
    st.text(back_from_function)


