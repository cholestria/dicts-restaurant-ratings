def rating_restaurants(filename):
    """Sorts rated restaurants in alphabetical order"""

    open_file = open(filename)

    restaurant_ratings = {}

    for line in open_file:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        restaurant_ratings[restaurant] = rating

    for restaurant, rating in sorted(restaurant_ratings.items()):
            print "%s is rated %s" % (restaurant, rating)

rating_restaurants("scores.txt")
