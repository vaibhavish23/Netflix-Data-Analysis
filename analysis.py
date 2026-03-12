import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("netflix_titles.csv")

print("Dataset Preview:")
print(data.head())

# --------------------------------
# 1. Movies vs TV Shows
# --------------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=data)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("movies_vs_tvshows.png")
plt.show()

# --------------------------------
# 2. Content released by year
# --------------------------------
year_data = data["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_data.index, year_data.values)

plt.title("Netflix Content Released Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")

plt.savefig("content_by_year.png")
plt.show()

# --------------------------------
# 3. Top 10 Countries Producing Content
# --------------------------------
country_data = data["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
country_data.plot(kind="bar")

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.savefig("top_countries.png")
plt.show()

# --------------------------------
# 4. Ratings Distribution
# --------------------------------
plt.figure(figsize=(10,5))
sns.countplot(x="rating", data=data)

plt.title("Distribution of Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.savefig("ratings_distribution.png")
plt.show()