# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

import sys
arguments = sys.argv


def command():

    if len(arguments) == 1:
        print("fav_animals [animal] [animal]")
    elif len(arguments) > 1 :
        copy_the_arguments_to_file()


def copy_the_arguments_to_file():
    try:
        with open("favourites.txt", "a+") as f:
        
            for i in range(len(arguments)):
                if arguments[i] not in f:
                    f.write(str(arguments[i] + "\n"))
    except Exception:
        print("File write error!")


command()