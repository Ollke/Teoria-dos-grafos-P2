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

adj = int(input("Digite o numero maximo de conexoes que o usuario pode ter (recomendado 50): "))

def userFilmes():
    user = []

    print("Digite a sua lista de filmes(quanto mais melhor)")
    while True:
        aux = int(input("\nDigite o ID do filme: "))
        aux1 = int(input("Digite a nota para o filme: "))

        if (aux1 > 5 or aux1*-1 > 0):

            print("Nota invalida")

        else:

            user.append([aux, aux1])

            if int(input("\nDigite 0 para continuar: ")) != 0:
                break

    return user


def MontarGrafo(user, Ratings, usersGraph, adj):
    for i in user:
        for j in Ratings.keys():
            if len(usersGraph["user"]) > adj:
                break
            for k in Ratings[j]:
                if i[0] == k[0] and i[1] == k[1]:
                    usersGraph["user"].append(j)
                    usersGraph[j].append("user")
                    break

    return usersGraph


while True:
    usersGraph["user"] = []
    user = userFilmes()
    usersGraph = MontarGrafo(user, Ratings, usersGraph, adj)

    if len(usersGraph["user"]) < 5:
        print("\ndados insuficientes, por favor refaça a sua lista de filmes")

    else:
        break

for i in usersGraph["user"]:
    for z in user:
        genres = Movies[z[0]][1]
        for g in genres:
            for r in Ratings[i]:
                if r[1] > 3 and g in Movies[r[0]][1]:
                    if Movies[r[0]][2] > 4:
                        aux = True
                        for k in user:
                            if k[0] == r[0]:
                                aux = False
                                break

                        if aux and r[0] not in recommended:
                            recommended.append(r[0])

    for j in Ratings[i]:
        if j[1] > 3:
            if Movies[j[0]][2] > 4:
                aux = True
                for k in user:
                    if k[0] == j[0]:
                        aux = False
                        break

                if aux and j[0] not in recommended:
                    recommended.append(j[0])

for i in usersGraph["user"]:
    for j in Ratings[i]:
        if j[1] > 3:
            if Movies[j[0]][2] > 4:
                aux = True
                for k in user:
                    if k[0] == j[0]:
                        aux = False
                        break

                if aux and j[0] not in recommended:
                    recommended.append(j[0])


print("\nRecomendações:")

for i in recommended:
    print("\n==============================")
    print(f"{Movies[i][0]} Nota media: %.2f" % Movies[i][2])
    print("==============================\n")

    if int(input("Digite 0 para parar:")) == 0:
        break