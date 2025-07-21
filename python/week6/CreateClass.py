class Collection:
    
    def __init__(self, movielist, gamelist):
        self.movielist = []
        self.gamelist = []
        self.favGame = ""
        self.favMovie = ""

        self.movielist = movielist
        self.gamelist = gamelist

    def Addmovies(self, movie):
        if movie in self.movielist:
            self.movielist.append(movie)
        else:
           print("Movie is already in collection")


    def Addgame(self, game):
        if game in self.gamelist:
            print("Game is already in collection")
        else:
            self.gamelist.append(game)
    

    def Removegame(self, game):
        if game in self.gamelist:
            self.gamelist.remove(game)
        else:
            print("Game not found")



    def Removegame(self, movie):
        if movie in self.movielist:
            self.movielist.remove(movie)
        else:
            print("Movie not found")

    def DisplayGames(self):
        for game in self.gamelist:
            print(game)
    
    def DisplayMovies(self):
        for movie in self.movielist:
            print(movie)

    def DisplayFavGame(self):
        print(f'Fav Game:{self.favGame}')
    
    def DisplayFavMovie(self):
        print(f'Fav Movie:{self.favMovie}')

    def DisplayColletion(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovies()
        self.DisplayFavMovie()

    def SetFavMovie(self, movie):
        if movie not in self.movielist:
            self.Addmovies(movie)
        self.favMovie = movie

    def SetFavGame(self, game):
        if game not in self.gamelist:
            self.Addgame(game)
        self.favGame = game
