import streamlit
streamlit.title('Hello streamlit')
streamlit.header('sample streamlit')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.text('text streamlit')
streamlit.text('textA streamlit')
streamlit.text('textB streamlit')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
