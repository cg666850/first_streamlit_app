import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry oatmeal')
streamlit.text('🥗Kale, spinch & Rocket smoothie')
streamlit.text('🐔Hard-Boiled Stream-Range egg')
streamlit.text('🥑🍞Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# create the repeatable code block called function
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized
   
   #new section to get fruitvise response
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice=streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function=get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)

except URLError as e:
   streamlit.error()

#streamlit.write('The user entered ', fruit_choice)



#import requests



# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")


# streamlit.text("Hello from Snowflake:")

streamlit.header("View Our fruits List - Add your Favorites!")

#snowflake_related functions:
def get_fruit_load_list():
      with my_cnx.cursor() as my_cur:
           my_cur.execute("select * from fruit_load_list")
           return my_cur.fetchall()

#add button to load the fruit
if streamlit.button('Get Fruit load list'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     streamlit.dataframe(my_data_rows)



#allow end user to add the list
def insert_row_snowflake(new_fruit):
      with my_cnx.cursor() as my_cur:
            my_cur.execute("insert into fruit_load_list values('"+new_fruit+"')")
            return "Thanks for adding"+ new_fruit
      
add_my_fruit = streamlit.text_input('What fruit would you like add yo list?')
if streamlit.button('Add a fruit to the list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function=insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)

streamlit.stop()





