def user_chooses(filename):
    """Asks a user what they want to do """

    print """What would you like to do? 
            1. See all the ratings in alphabetical order. 
            2. Add a new resturant and rating. 
            3. Quit."""

    user_choice = raw_input("Select 1, 2, or 3: ")
    if user_choice == "1":
        just_print(filename)
    elif user_choice == "2":
        rating_restaurants(filename)
    else:
        exit()


def just_print(filename):
    """print list without input"""

    open_file = open(filename)

    restaurant_ratings = {}

    for line in open_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        restaurant_ratings[restaurant] = rating

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "%s is rated %s" % (restaurant, rating)

    open_file.close()


def rating_restaurants(filename):
    """Sorts rated restaurants in alphabetical order"""

    open_file = open(filename)

    restaurant_ratings = {}

    restaurant_name = raw_input("What's the restaurant's name?")
    restaurant_score = int(raw_input("What's the restaurant's score?"))

    for line in open_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        restaurant_ratings[restaurant] = rating

    restaurant_ratings[restaurant_name] = restaurant_score    

    for restaurant, rating in sorted(restaurant_ratings.items()):
            print "%s is rated %s" % (restaurant, rating)

    open_file.close()

#rating_restaurants("scores.txt")
user_chooses("scores.txt")        