import numpy as np


def path_finder(travel_cities): # function for finding the path of the traveller
    optimal_path = []
    optimal_length = float('inf')

    for path_start, start in enumerate(travel_cities): # determining the start of the path
        path = [path_start]
        length = 0

        i_next, next, distance = get_closest(start, travel_cities, path) # checking for the distance to the next point
        length += distance # calculating the total lenth
        path.append(i_next) # adding the next distance to current path

        while len(path) < travel_cities.shape[0]:
            i_next, next, distance = get_closest(next, travel_cities, path) # getting the next closest point to move to
            length += distance
            path.append(i_next)

        # print(path)

        if length < optimal_length:  # checking if the length obtained is less than the optimal length
            optimal_length = length
            optimal_path = path

    return optimal_path, optimal_length


def get_closest(travel_city, travel_cities, visited):  # getting the closest point to move to
    best_distance = float('inf')

    for i, c in enumerate(travel_cities):

        if i not in visited:  # to check if the city is already visited
            distance = squared_distance(travel_city, c)

            if distance < best_distance:
                closest_city = c
                india_closest_city = i
                best_distance = distance # getting the point with shortest distance

    return india_closest_city, closest_city, best_distance


def squared_distance(c1, c2):  # checking for points on the map 
    t1 = c2[0] - c1[0]
    t2 = c2[1] - c1[1]

    return t1 * 2 + t2 * 2