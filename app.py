import streamlit as st
import pickle
import pandas as pd

games_dict = pickle.load(open('games_dict.pkl','rb'))
euclidean_similarity = pickle.load(open('euclidean_similarity.pkl','rb'))

games = pd.DataFrame(games_dict)


def recommend(game):
    index = games[games['game_title2'] == game].index[0]
    distances = sorted(list(enumerate(euclidean_similarity[index])), reverse=False, key=lambda x: x[1])[1:6]

    recommended_games = []
    for i in distances:
        recommended_games.append(games.iloc[i[0]].game_title2)
    return recommended_games

st.title('Game Video Recommender System')

selected_game_name = st.selectbox(
    'What game should I base my recommendations on?',
    games['game_title2'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_game_name)
    for i in recommendations:
        st.write(i)
