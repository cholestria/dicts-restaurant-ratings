def create_dictionary():
    """Creates a dictionary of restauants and scores"""

    open_file = open("scores.txt")

    restaurant_ratings = {}

    for line in open_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        restaurant_ratings[restaurant] = (rating)

    return restaurant_ratings

    # open_file.close()


def user_chooses():
    """Asks a user what they want to do """

    print """What would you like to do?
        1. See all the ratings in alphabetical order.
        2. Add a new resturant and rating.
        3. Quit."""

    return (raw_input("Select 1, 2, or 3: "))


def adding_restaurants(restaurant_ratings):
    """allows user to add and rate a restaurant"""

    restaurant = raw_input("What's the restaurant's name?")
    rating = int(raw_input("What's the restaurant's rating?"))

    restaurant_ratings[restaurant] = rating


def print_scores(restaurant_ratings):
    """Prints sorted dictionary"""

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "%s is rated %s" % (restaurant, rating)

restaurant_ratings = create_dictionary()


while True:
    user_choice = user_chooses()

    if user_choice == "1":
        print_scores(restaurant_ratings)
    elif user_choice == "2":
        adding_restaurants(restaurant_ratings)
    else:
        exit()
