import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# full csv
df = pd.read_csv("C:/Users/andre/Documents/Strive_repository/IMDB_challenge/data_imdb_action_new.csv")
st.title("Top 100 IMDB action movies")
st.write(df)

# Actor csv
df_actor = pd.read_csv("C:/Users/andre/Documents/Strive_repository/IMDB_challenge/data_imdb_actors_name.csv")
st.title("Best Actors")
st.write(df_actor)

df_min_max_scaled = df.copy()

column = 'Rating'
column1 = 'Duration'

df_min_max_scaled[column, column1] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min()) / (df_min_max_scaled[column1] - df_min_max_scaled[column1].min()) / (df_min_max_scaled[column1].max() - df_min_max_scaled[column1].min())

st.header("Ratings of movies by year")
st.bar_chart(df[['Release', 'Rating']].groupby('Release').mean())

st.header("Best directors in Action Movies")
st.bar_chart(df['Director'].value_counts().nlargest(5))

st.header("Best Actor in Action Movies")
st.bar_chart(df["Stars"].value_counts().nlargest(10))



st.write("line chart")
st.line_chart(df[["Title"]])

st.write("area chart")
st.area_chart(df["Rating"])




fig, ax = plt.subplots()
df.hist(
    bins=8,
    column="Rating",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
st.write(fig)