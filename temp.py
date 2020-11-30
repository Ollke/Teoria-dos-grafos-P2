import pandas as pd

DataMovies = pd.read_csv("ml-latest-small/movies.csv", sep=",")

MoviesTitle = DataMovies["title"].values
MoviesId = DataMovies["movieId"].values
MoviesGenres = DataMovies["genres"].values

Movies = {}
recommended = []

for i in range(len(MoviesTitle)):
    Movies[MoviesId[i]] = [MoviesTitle[i], MoviesGenres[i].split("|"), 6]


DataRatings = pd.read_csv("ml-latest-small/ratings.csv", sep=",")

RatingsUserId = DataRatings["userId"].values
RatingsMoviesId = DataRatings["movieId"].values
RatingsList = DataRatings["rating"].values

Ratings = {}
users = {}

for i in RatingsUserId:
    Ratings[i] = []
    users[i] = []

for i in range(len(RatingsUserId)):
    Ratings[RatingsUserId[i]].append([RatingsMoviesId[i],RatingsList[i]])

adj = int(input("Digite o numero de conexoes que cada usuario pode ter (recomendado 50):"))

for i in Ratings.keys():
    for j in Ratings.keys():
        if len(users[i])>adj:
            break

        if i != j:
            for k in Ratings[i]:
                if j not in users[i]:
                        for z in Ratings[j]:
                            if k[0] == z[0] and z[1] == k[1]:
                                users[i].append(j)
                                break

