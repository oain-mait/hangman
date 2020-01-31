# use a json file to get list of movies from IMDb top 100
import unidecode
import json
import random

display = ''
entered_value = set()  # the set is used to keep track of all the input user has entered so they are not penalized twice

with open("movies.json", "r") as read_file:
    data = json.load(read_file)
movies = []  # list that stores titles of movies

for movie in data:
    if all(x.isalpha() or x.isspace() for x in movie['title']):
        movies.append(movie['title'])  # get titles of movies only with alphabets in them

for movie in movies:
    movie = unidecode.unidecode(movie)  # remove any french accent characters


def user_input():
    return input("Enter the letter: ")


def update_display(character, index):
    global display
    for i in index:
        display = display[:i] + character + display[i+1:]  # displays the movie titles with hidden characters


def main():
    global display
    print("Hangman: Win or Hang")
    print("Category: IMDb TOP 100")
    lives = int(input("Enter number of lives: "))  # user sets difficulty
    current_movie = random.choice(movies)
    current_movie = current_movie.upper()
    unsolved = {}
    for index, character in enumerate(current_movie):
        unsolved.setdefault(character, []).append(index)
        # create a dict where each letter is the key and their location is the value(list/individual)
    if ' ' in unsolved:
        del unsolved[' ']  # removes any instances of blank spaces from the dictionary
    display = current_movie  # display is used to show the movie with hidden characters
    for c in display:
        if c in unsolved:
            display = display.replace(c, '*')  # display is initialized with all hidden characters
    print(display)

    while lives > 0:
        print("Lives left: %d" % lives)
        x = input("Enter a letter: ").upper()  # converts all input to uppercase for easier comparisons
        if not x.isalpha():
            continue  # type check for input, if its not an alphabet, the loop is rerun
        if x in entered_value:
            print(display)
            print("Entered Values: %s" % entered_value)
            continue
        entered_value.add(x)  # valid user input is tracked
        if x in unsolved:
            update_display(x, unsolved[x])  # both the input adn the index is passed to the function
            del unsolved[x]  # if the user inputs the correct value, it is removed from the dictionary
        else:
            lives -= 1
        if not unsolved:
            print("You Won!")
            return 0
        print(display)
        print("Entered Values: %s" % entered_value)
    print("You Neck is no more!!!!")
    print("Write answer was: %s" % current_movie)


main()
