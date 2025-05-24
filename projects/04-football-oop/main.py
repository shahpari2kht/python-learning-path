import random

names = [
    'Hossein', 'Maziar', 'Akbar', 'Nima', 'Mehdi', 'Farhad', 'Mohammad',
    'Khashayar', 'Milad', 'Mostafa', 'Amin', 'Saeed', 'Pouya', 'Pouria',
    'Reza', 'Ali', 'Behzad', 'Soheil', 'Behrooz', 'Shahrooz', 'Saman', 'Mohsen'
]

class Human:
    def __init__(self, name):
        self.name = name

class Footballist(Human):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def __str__(self):
        return f"{self.name} {self.team}"

def main():
    random.shuffle(names)
    team_A = [Footballist(name, 'A') for name in names[:11]]
    team_B = [Footballist(name, 'B') for name in names[11:]]
    
    print("Team A players:")
    for player in team_A:
        print(player)
    print("\nTeam B players:")
    for player in team_B:
        print(player)

if __name__ == '__main__':
    main()
