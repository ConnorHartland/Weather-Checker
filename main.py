import requests
import sys
from location import Location   

def main():
    positiveRep = ['yes', 'y', 'Yes', 'Y']
    loop = True

    userLoc = input("Would you like to enter your own city? ")
    if userLoc in positiveRep:
        loop = False
        userLoc = input("Where would you like to check the weather? ")
        print(Location(userLoc))

    while loop:
        locations = ['London', 'Dublin', 'New York', 'San Jose', 'Los Angeles', 'Rome', 'Orange County']
        locations.sort()
        for location in locations:
            if ' ' in location:
                split = location.split()
                ','.join(split)
            print(Location(location))
            print('\n')
        break

    

if __name__ == "__main__":
    main()
