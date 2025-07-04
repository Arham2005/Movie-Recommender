# import streamlit as st
# import pandas as pd
# import requests
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
# st.title("🎥 Movie Recommendation System")

# # Load dataset
# @st.cache_data
# def load_data():
#     df = pd.read_csv("tmdb_5000_movies.csv")
#     df = df[['title', 'overview']]
#     df.dropna(inplace=True)
#     return df

# movies = load_data()

# # Vectorize overview text
# @st.cache_resource
# def compute_similarity(df):
#     tfidf = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf.fit_transform(df['overview'])
#     similarity = cosine_similarity(tfidf_matrix)
#     return similarity

# similarity = compute_similarity(movies)

# # Fetch poster from TMDB
# def get_poster(movie_name):
#     try:
#         api_key = "<<YOUR_TMDB_API_KEY>>"  # <-- Replace this with your API key
#         url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}"
#         response = requests.get(url)
#         data = response.json()
#         if data["results"]:
#             poster_path = data["results"][0]["poster_path"]
#             full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
#             return full_path
#     except:
#         pass
#     return "https://via.placeholder.com/300x450?text=No+Poster"

# # Recommend similar movies
# def recommend(movie_title):
#     idx = movies[movies['title'] == movie_title].index[0]
#     scores = list(enumerate(similarity[idx]))
#     sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
#     recommended_movies = [movies.iloc[i[0]]['title'] for i in sorted_scores]
#     posters = [get_poster(title) for title in recommended_movies]
#     return recommended_movies, posters

# # UI
# selected_movie = st.selectbox("Select a Movie", movies['title'].values)

# if st.button("Recommend"):
#     names, images = recommend(selected_movie)
#     st.subheader("🎬 Recommended Movies:")

#     cols = st.columns(5)
#     for idx in range(5):
#         with cols[idx]:
#             st.image(images[idx], caption=names[idx], use_column_width=True)

# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# http://www.omdbapi.com/?i=tt3896198&apikey=b9305253

# st.set_page_config(page_title="🎥 Movie Recommender (Offline)", layout="centered")
# st.title("🎬 Movie Recommendation System (Offline)")

# # --- Load Dataset ---
# @st.cache_data
# def load_data():
#     df = pd.read_csv("tmdb_5000_movies.csv")
#     df = df[['title', 'overview']].dropna()
#     return df

# movies = load_data()

# # --- Vectorize Overviews ---
# @st.cache_resource
# def compute_similarity(df):
#     tfidf = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf.fit_transform(df['overview'])
#     similarity = cosine_similarity(tfidf_matrix)
#     return similarity

# similarity = compute_similarity(movies)

# # --- Recommend Function ---
# def recommend(movie_title):
#     idx = movies[movies['title'] == movie_title].index[0]
#     scores = list(enumerate(similarity[idx]))
#     sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
#     recommendations = [movies.iloc[i[0]]['title'] for i in sorted_scores]
#     return recommendations

# # --- UI ---
# selected_movie = st.selectbox("Select a Movie", movies['title'].values)

# if st.button("Recommend"):
#     st.subheader("📋 Recommended Movies:")
#     for movie in recommend(selected_movie):
#         st.write("🎬", movie)


# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import requests

# st.set_page_config(page_title="🎬 Movie Recommender (OMDb)", layout="wide")
# st.title("🎬 Movie Recommendation System with Posters (OMDb API)")

# # 🔑 Enter your OMDb API key here
# OMDB_API_KEY = "b9305253"  # Replace with your real key


# # ✅ Load the movie data
# @st.cache_data
# def load_data():
#     df = pd.read_csv("tmdb_5000_movies.csv")
#     df = df[['title', 'overview']].dropna()
#     return df

# movies = load_data()


# # ✅ Compute similarity
# @st.cache_resource
# def compute_similarity(df):
#     tfidf = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = tfidf.fit_transform(df['overview'])
#     similarity = cosine_similarity(tfidf_matrix)
#     return similarity

# similarity = compute_similarity(movies)


# # ✅ Recommend movies
# def recommend(movie_title):
#     idx = movies[movies['title'] == movie_title].index[0]
#     scores = list(enumerate(similarity[idx]))
#     sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
#     recommended = [(movies.iloc[i[0]]['title']) for i in sorted_scores]
#     return recommended


# # ✅ Fetch poster using OMDb
# def get_poster_omdb(movie_title):
#     url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
#     try:
#         response = requests.get(url)
#         data = response.json()
#         poster = data.get("Poster")
#         if poster and poster != "N/A":
#             return poster
#     except:
#         pass
#     # Return a default placeholder if no poster is found
#     return "https://via.placeholder.com/300x450?text=No+Poster"


# # 🎛️ UI
# selected_movie = st.selectbox("🎞️ Select a Movie", sorted(movies['title'].unique()))


# if st.button("🔍 Recommend"):
#     recommended_movies = recommend(selected_movie)
#     st.subheader("🎯 Top 5 Similar Movies")

#     cols = st.columns(5)
#     for i, movie in enumerate(recommended_movies):
#         poster = get_poster_omdb(movie)
#         plex_link = f"https://watch.plex.tv/search?q={movie}"

#         with cols[i]:
#             st.markdown(f"""
#                 <a href="{plex_link}" target="_blank">
#                     <img src="{poster}" width="100%" style="border-radius: 10px;" />
#                 </a>
#                 <div style="text-align:center">
#                     <strong>{movie}</strong>
#                 </div>
#             """, unsafe_allow_html=True)

# ==================================================================================================================================================================================

# ==== FOR YOUTUBE =====
# if st.button("🔍 Recommend"):
#     recommended_movies = recommend(selected_movie)
#     st.subheader("🎯 Top 5 Similar Movies")

#     cols = st.columns(5)
#     for i, movie in enumerate(recommended_movies):
#         poster = get_poster_omdb(movie)
# #        yt_link = f"https://www.youtube.com/results?search_query={movie}+full+movie"
#         plex_link = f"https://watch.plex.tv/search?q={movie}"

#         with cols[i]:
#             # ✅ Clickable movie poster linked to YouTube
#             st.markdown(f"""
#                 <a href="{yt_link}" target="_blank">
#                     <img src="{poster}" width="100%" style="border-radius: 10px;" />
#                 </a>
#                 <div style="text-align:center">
#                     <strong>{movie}</strong>
#                 </div>
#             """, unsafe_allow_html=True)


# if st.button("🔍 Recommend"):
#     recommended_movies = recommend(selected_movie)
#     st.subheader("🎯 Top 5 Similar Movies")

#     cols = st.columns(5)
#     for i, movie in enumerate(recommended_movies):
#         poster = get_poster_omdb(movie)
#         with cols[i]:
            
# #             st.image(poster, caption=movie, use_container_width=True)
#             # Make the image clickable (link to YouTube search)
#             yt_link = f"https://www.youtube.com/results?search_query={movie}+full+movie"
#             st.markdown(f"""
#             <a href="{yt_link}" target="_blank">
#                 <img src="{info['poster']}" width="100%" style="border-radius: 10px;" />
#             </a>
#             <p style="text-align:center"><strong>{movie}</strong></p>
#             """, unsafe_allow_html=True)


import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from urllib.parse import quote  # ✅ For safe URLs

# 🌟 Page config
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation App")

# 🔑 OMDb API Key
OMDB_API_KEY = "b9305253"  # Replace with your real key if needed

# ✅ Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("tmdb_5000_movies.csv")
    df = df[['title', 'overview']].dropna()
    return df

movies = load_data()

# ✅ Compute cosine similarity
@st.cache_resource
def compute_similarity(df):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['overview'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

similarity = compute_similarity(movies)

# ✅ Recommend similar movies
def recommend(movie_title):
    idx = movies[movies['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended = [movies.iloc[i[0]]['title'] for i in sorted_scores]
    return recommended

# ✅ Fetch poster from OMDb
def get_poster_omdb(movie_title):
    url = f"http://www.omdbapi.com/?t={quote(movie_title)}&apikey={OMDB_API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        poster = data.get("Poster")
        if poster and poster != "N/A":
            return poster
    except:
        pass
    return "https://via.placeholder.com/300x450?text=No+Poster"

# 🎛️ UI: Movie select box
selected_movie = st.selectbox("🎞️ Select a Movie", sorted(movies['title'].unique()))

# 🎬 On button click
if st.button("🔍 Recommend"):
    recommended_movies = recommend(selected_movie)
    st.subheader("🎯 Top 5 Similar Movies")

    cols = st.columns(5)

    for i, movie in enumerate(recommended_movies):
        poster = get_poster_omdb(movie)
        encoded_title = quote(movie)
        plex_link = f"https://www.google.com/search?q=site:plex.tv+{encoded_title}"

        with cols[i]:
            st.markdown(f"""
                <a href="{plex_link}" target="_blank">
                    <img src="{poster}" width="100%" style="border-radius: 10px;" />
                </a>
                <div style="text-align:center">
                    <strong>{movie}</strong><br>
                    <a href="{plex_link}" target="_blank">🎬 Search on Plex</a>
                </div>
                """, unsafe_allow_html=True)

