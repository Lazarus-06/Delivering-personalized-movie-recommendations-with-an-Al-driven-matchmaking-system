
import pandas as pd
import streamlit as st

# Load dataset
df = pd.read_csv("dataset.csv")
df['UserPreferences'] = df['UserPreferences'].str.lower()
df['MovieGenre'] = df['MovieGenre'].str.lower()
df['UserGender'] = df['UserGender'].str.lower()

# Genre options
all_genres = set()
for prefs in df['UserPreferences']:
    all_genres.update([genre.strip() for genre in prefs.split(',')])
genre_options = sorted(all_genres)

# Streamlit UI
st.title("🎬 Movie Recommender")

gender = st.selectbox("Select Gender", ["Any", "Male", "Female"])
selected_genres = st.multiselect("Select Preferred Genres", genre_options)

if st.button("Recommend Movie"):
    if not selected_genres:
        st.warning("Please select at least one genre.")
    else:
        recommendations = []
        for _, row in df.iterrows():
            if gender.lower() == "any" or row['UserGender'] == gender.lower():
                if any(genre in row['MovieGenre'] for genre in selected_genres):
                    recommendations.append(row['MovieTitle'])

        if recommendations:
            st.success("Recommended Movie(s):")
            for movie in set(recommendations):
                st.write(f"- {movie}")
        else:
            st.info("No matching movies found.")
