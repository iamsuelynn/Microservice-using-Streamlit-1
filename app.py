import streamlit as st
import pandas as pd
import gcsfs
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq
import os

def main():
    
    st.title("Welcome to Sue Book Store :star:")
    st.subheader("Glad you make it here, we were expecting you :smile:")
    
    Menu_Items = ["View all Books", "Search for Books by Ratings"]
    Menu_Choices = st.sidebar.selectbox('Select the Options', Menu_Items )
    
    client = bigquery.Client()
    table_id = 'Books.books_title_author'
    sql = "SELECT * FROM `sue-gcp-learning-env.Books.books_title_author`"
    books_table = client.query(sql).to_dataframe()
    
    if Menu_Choices == "View all Books":
    
        st.write("Below are All the Books Available")
        st.table(books_table)
        
    elif Menu_Choices == "Search for Books by Ratings":
        
        st.write("Determine the ratings you would like to view:") 
        ratings =  st.slider('Slide & Pick',0.0, 10.0, (2.0, 7.0))
        st.write(ratings) 
        filtered_table = books_table[books_table['book_ratings'].between(ratings[0],ratings[1])]
        st.table(filtered_table)


if __name__ == "__main__":
    main()
