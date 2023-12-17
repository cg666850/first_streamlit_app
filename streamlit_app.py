import streamlit
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, spinch & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Stream-Range egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
