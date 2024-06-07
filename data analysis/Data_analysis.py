import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv', encoding='latin1')

# Visualization 1: Number of Movies/Shows per Year on Netflix (Bar Chart)
df['release_year'].value_counts().sort_index().plot(kind='bar', figsize=(12, 6))
plt.title('Number of Movies/Shows per Year on Netflix')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Visualization 2: Distribution of Content Types (Pie Chart)
content_types = df['type'].value_counts()
content_types.plot.pie(autopct='%1.1f%%', figsize=(8, 8))
plt.title('Distribution of Content Types on Netflix')
plt.ylabel('')
plt.show()

top_countries = df['country'].value_counts().head(10)
print('Top 10 Countries with the Most Content:')
print(top_countries)

def clean_duration(duration):
    duration = duration.str.replace(' min', '').str.replace(' Seasons', '').str.replace(' Season', '')
    duration = pd.to_numeric(duration, errors='coerce')
    return duration

movies = df[df['type'] == 'Movie'].copy()
shows = df[df['type'] == 'TV Show'].copy()

movies['duration'] = clean_duration(movies['duration'])
shows['duration'] = clean_duration(shows['duration'])

average_movie_duration = movies['duration'].mean()
average_show_duration = shows['duration'].mean()

print('Average Movie Duration:', average_movie_duration)
print('Average TV Show Duration:', average_show_duration)

# Visualization 3: Content Duration Distribution (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(movies['duration'].dropna(), bins=20, edgecolor='black', alpha=0.5, label='Movies')
plt.hist(shows['duration'].dropna(), bins=20, edgecolor='black', alpha=0.5, label='TV Shows')
plt.title('Content Duration Distribution')
plt.xlabel('Duration (minutes for movies, seasons for TV shows)')
plt.ylabel('Count')
plt.legend()
plt.show()

# Visualization 4: Rating Analysis of Movies (Bar Chart)
rating_counts = movies['rating'].value_counts(normalize=True) * 100
rating_counts.plot(kind='bar', figsize=(10, 6))
plt.title('Rating Analysis of Movies')
plt.xlabel('Rating')
plt.ylabel('Percentage')
plt.show()
