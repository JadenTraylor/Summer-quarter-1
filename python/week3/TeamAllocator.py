import random

players =["Ja'Den", "Max", "Braylen", 
          "Jeffery", "Xavier", "Avery",
          "Carl", "Walter", "Darren",
          "EJ", "Nahum", "Joaquin", 
          "Marshawn", "Isaiah", "Kenlon",
          "Nishad", "Kauri", "Kriss",
          "Joseph", "Semaj", "Tay", 
          "Taqari", "Jarmauri", "Devon"]


def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players) // 2]
    teamCaptin1 = team1[random.randrange(0,12)]
   
    print("Team1:")
    print("Team 1 Captain:" + teamCaptin1)
    for players in team1:
        print(players)

PickTeams(players)



def PickTeams(players):
    random.shuffle(players)
    team2 = players[:len(players) // 2]
    teamCaptin2 = team2[random.randrange(0,12)]
   
    print("Team2:")
    print("Team 2 Captain:" + teamCaptin2)
    for players in team2:
     print(players)

PickTeams(players)