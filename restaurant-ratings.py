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

rating_restaurants("scores.txt")
