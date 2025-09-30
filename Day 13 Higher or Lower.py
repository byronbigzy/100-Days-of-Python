import random
import os

data = [
    {
    'name': 'Cristiano Ronaldo',
    'follower': 665,
    'description': 'Professional Footballer',
    'country': 'Portugal'
    },
    {
    'name': 'Lionel Messi',
    'follower': 506,
    'description': 'Professional Footballer',
    'country': 'Argentina'
    },
    {
    'name': 'Selena Gomez',
    'follower': 417,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Dwayne Johnson',
    'follower': 392,
    'description': 'Actor and Wrestler',
    'country': 'United States'
    },
    {
    'name': 'Kylie Jenner',
    'follower': 392,
    'description': 'Media Personality/Businesswoman',
    'country': 'United States'
    },
    {
    'name': 'Ariana Grande',
    'follower': 374,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Kim Kardashian',
    'follower': 355,
    'description': 'Media Personality/Businesswoman',
    'country': 'United States'
    },
    {
    'name': 'Beyoncé',
    'follower': 309,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Khloé Kardashian',
    'follower': 301,
    'description': 'Media Personality',
    'country': 'United States'
    },
    {
    'name': 'Justin Bieber',
    'follower': 293,
    'description': 'Musician',
    'country': 'Canada'
    },
    {
    'name': 'Virat Kohli',
    'follower': 273,
    'description': 'Professional Cricketer',
    'country': 'India'
    },
    {
    'name': 'Neymar',
    'follower': 231,
    'description': 'Professional Footballer',
    'country': 'Brazil'
    },
    {
    'name': 'Miley Cyrus',
    'follower': 212,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Real Madrid CF',
    'follower': 177,
    'description': 'Football Club',
    'country': 'Spain'
    },
    {
    'name': 'Zendaya',
    'follower': 177,
    'description': 'Actress and Singer',
    'country': 'United States'
    },
    {
    'name': 'Kevin Hart',
    'follower': 176,
    'description': 'Comedian and Actor',
    'country': 'United States'
    },
    {
    'name': 'Cardi B',
    'follower': 163,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'LeBron James',
    'follower': 158,
    'description': 'Basketball Player',
    'country': 'United States'
    },
    {
    'name': 'Demi Lovato',
    'follower': 153,
    'description': 'Musician and Actress',
    'country': 'United States'
    },
    {
    'name': 'Rihanna',
    'follower': 149,
    'description': 'Musician and Businesswoman',
    'country': 'Barbados'
    },
    {
    'name': 'Chris Brown',
    'follower': 144,
    'description': 'Musician',
    'country': 'United States'
    },
    {
    'name': 'FC Barcelona',
    'follower': 143,
    'description': 'Football Club',
    'country': 'Spain'
    },
    {
    'name': 'Drake',
    'follower': 142,
    'description': 'Musician',
    'country': 'Canada/United States'
    },
    {
    'name': 'Ellen DeGeneres',
    'follower': 135,
    'description': 'Former Comedian/TV Host',
    'country': 'United States'
    },
    {
    'name': 'Kylian Mbappé',
    'follower': 126,
    'description': 'Professional Footballer',
    'country': 'France'
    },
    {
    'name': 'Billie Eilish',
    'follower': 124,
    'description': 'Musician',
    'country': 'United States'
    },
    {
    'name': 'UEFA Champions League',
    'follower': 121,
    'description': 'Club Football Competition',
    'country': 'Europe'
    },
    {
    'name': 'Gal Gadot',
    'follower': 107,
    'description': 'Actress',
    'country': 'Israel'
    },
    {
    'name': 'Lisa (BLACKPINK)',
    'follower': 106,
    'description': 'Musician (K-Pop Idol)',
    'country': 'Thailand'
    },
    {
    'name': 'Vin Diesel',
    'follower': 103,
    'description': 'Actor',
    'country': 'United States'
    },
    {
    'name': 'Narendra Modi',
    'follower': 97,
    'description': 'Prime Minister of India',
    'country': 'India'
    },
    {
    'name': 'NASA',
    'follower': 96.2,
    'description': 'Space Agency',
    'country': 'United States'
    },
    {
    'name': 'Shraddha Kapoor',
    'follower': 93.9,
    'description': 'Actress',
    'country': 'India'
    },
    {
    'name': 'Shakira',
    'follower': 93.2,
    'description': 'Musician',
    'country': 'Colombia'
    },
    {
    'name': 'Priyanka Chopra Jonas',
    'follower': 92.5,
    'description': 'Actress',
    'country': 'India'
    },
    {
    'name': 'NBA',
    'follower': 90.8,
    'description': 'Basketball League',
    'country': 'United States/Canada'
    },
    {
    'name': 'Snoop Dogg',
    'follower': 88.6,
    'description': 'Musician',
    'country': 'United States'
    },
    {
    'name': 'Jennie (BLACKPINK)',
    'follower': 88.2,
    'description': 'Musician',
    'country': 'South Korea'
    },
    {
    'name': 'David Beckham',
    'follower': 88.2,
    'description': 'Former Footballer',
    'country': 'United Kingdom'
    },
    {
    'name': 'Dua Lipa',
    'follower': 88,
    'description': 'Musician',
    'country': 'United Kingdom'
    },
    {
    'name': 'Alia Bhatt',
    'follower': 86.5,
    'description': 'Actress',
    'country': 'India'
    }
]

title_art = '''
  _   _ _       _                              _                           
 | | | (_) __ _| |__   ___ _ __    ___  _ __  | |    _____      _____ _ __ 
 | |_| | |/ _` | '_ \ / _ \ '__|  / _ \| '__| | |   / _ \ \ /\ / / _ \ '__|
 |  _  | | (_| | | | |  __/ |    | (_) | |    | |__| (_) \ V  V /  __/ |   
 |_| |_|_|\__, |_| |_|\___|_|     \___/|_|    |_____\___/ \_/\_/ \___|_|   
          |___/                                                            
'''

vs_art =  '''
\  \/ /  ___/
 \   /\___ \ 
  \_//____  >
          \/     
'''          

continuing = True

def formatUser(user):
    if (user['description'][0].lower == "a") or (user['description'][0].lower == "e") or (user['description'][0].lower == "i") or (user['description'][0].lower == "o") or (user['description'][0].lower == "u") :
        article = "an"
    else:
        article = "a"

    sentence = (f"{user['name']}, {article} {user['description']}, from {user['country']}.")
    return sentence

def compareFollowers(user1, user2):
    followers1 = user1['follower']
    followers2 = user2['follower']
    
    if followers1 > followers2:
        return user1
    else:
        return user2
    
    # Edge case: What if they're equal?

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Select 2 Random Starting Choices
user1 = random.choice(data)

def randomChoice():
    user2 = random.choice(data)
    # If same person is chosen for both, reroll user2
    while user1 == user2:
        user2 = random.choice(data)
    return user2

points = 0

while continuing:
    clearTerminal()
    print(title_art)

    a = user1 
    b = randomChoice()

    if points > 0:
        print(f"Correct!, You now have {points} points.")

    print("A: ", formatUser(a))
    print(vs_art)
    print("B: ", formatUser(b))

    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    choices = {'a': a, 'b': b}

    answer = compareFollowers(a, b)

    if player_choice in choices:
        if choices[player_choice] == answer:
            points += 1
            print("Correct")
            user1 = answer
        else:
            continuing = False
            clearTerminal()
            print(title_art)
            print(f"Sorry, that's wrong. Final score: {points}")
    else:
        print("Invalid choice, Type 'A' or 'B': ")