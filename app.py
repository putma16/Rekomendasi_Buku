import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('books_list.csv')
doc_sim_df = pd.read_csv('similarity.csv')

books_list = df['Title'].values

def books_recommender(books_title, books=books_list, doc_sims=doc_sim_df):
    # find book id
    books_idx = np.where(books == books_title)[0][0]
    
    # get book similarities
    books_similarities = doc_sims.iloc[books_idx].values
    # get top 5 similar book IDs
    similar_books_idxs = np.argsort(-books_similarities)[1:6]
    # get top 5 books
    similar_books = books[similar_books_idxs]
    # return the top 5 books
    return similar_books

   
st.title('Sistem Rekomendasi Buku 📚')
st.header('Berbasis Kemiripan Menggunakan Cosine Similarity', divider='blue')

user_input = st.selectbox('Pilih Judul Buku', books_list)

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    try:
        st.session_state.output = books_recommender(user_input, books_list, doc_sim_df)
    except: 
        st.session_state.output = 'Buku yang anda inginkan belum tersedia'
    
st.button('Submit', on_click=btn_action)
st.write(st.session_state.output)
