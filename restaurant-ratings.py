def rating_restaurants(filename):
    """Sorts rated restaurants in alphabetical order"""

    open_file = open(filename)

    restaurant_ratings = {}

    for line in open_file:
        line = line.rstrip()
        line = line.split(':')
        restaurant_ratings[line[0]] = line[1]

    for restaurant, rating in sorted(restaurant_ratings.items()):
            print "%s is rated %s" % (restaurant, rating)

rating_restaurants("scores.txt")
