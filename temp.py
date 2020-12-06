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
usersGraph = {}

for i in RatingsUserId:
    Ratings[i] = []
    usersGraph[i] = []

for i in range(len(RatingsUserId)):
    Ratings[RatingsUserId[i]].append([RatingsMoviesId[i],RatingsList[i]])

for i in range(len(RatingsList)):
    if Movies[RatingsMoviesId[i]][2] == 6:
        Movies[RatingsMoviesId[i]][2] = RatingsList[i]
    else:
        Movies[RatingsMoviesId[i]][2] = (Movies[RatingsMoviesId[i]][2] + RatingsList[i])/2


adj = int(input("Digite o numero de conexoes que cada usuario pode ter (recomendado 50):"))



for i in Ratings.keys():
    for j in Ratings.keys():
        if len(usersGraph[i])>adj:
            break

        if i != j:

            for k in Ratings[i]:
                if j in usersGraph[i]:
                    break
                else:
                    for z in Ratings[j]:
                        if k[0] == z[0] and z[1] == k[1]:
                            usersGraph[i].append(j)
                            break

