import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('books_list.csv')
doc_sim_df = pd.read_csv('similarity.csv')

books_list = df['Title'].values
#st.write(books_list.shape)

def books_recommender(books_title, books=books_list, doc_sims=doc_sim_df):
    # find movie id
    #st.write(books_title.shape)
    books_idx = np.where(books == books_title)[0][0]
    
    # get movie similarities
    books_similarities = doc_sims.iloc[books_idx].values
    # get top 5 similar movie IDs
    similar_books_idxs = np.argsort(-books_similarities)[1:6]
    # get top 5 movies
    similar_books = books[similar_books_idxs]
    # return the top 5 movies
    return similar_books

   
st.title('Sistem Rekomendasi Buku 📚')
st.header('Berbasis Kemiripan Menggunakan Cosine Similiarity',divider='blue')

user_input = st.text_input('Judul Buku', '', placeholder='Masukan judul buku')
user_input = user_input.lower()


if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    
    try:
        st.session_state.output = books_recommender(user_input.lower(), books_list, doc_sim_df)
    except: 
        st.session_state.output = 'Buku yang anda inginkan belum tersedia'
    
st.button('Submit', on_click=btn_action)
st.write(st.session_state.output)