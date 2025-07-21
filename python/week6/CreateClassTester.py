import CreateClass

movies = ("All American", "Up Shaws", "Shameless", "On my Block", "Stanger Things")
games = ("NCAA", "Call of Duty", "GTA", "UFC", "WatchDogs")
myCollection = CreateClass.Collection(movies, games)

myCollection.SetFavGame("NCAA")
myCollection.SetFavMovie("All American")
myCollection.DisplayColletion()