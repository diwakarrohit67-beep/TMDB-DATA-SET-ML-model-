import streamlit as st
import pickle
import pandas as pd
from streamlit import title

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1]) [1:6]


    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender')


selected_movie_name = st.selectbox(
    'How many movies do you like?',
    (movies['title'].values)
)

if st.button('Recommend Movies'):
    recommendations = recommend(selected_movie_name)
    for r in recommendations:
        st.write(r)
















