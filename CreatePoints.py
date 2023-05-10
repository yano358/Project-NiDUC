from math import sin, cos, pi, log1p
from matplotlib import pyplot as plt
# This is only used for generation of gaussian distribution.

import random as rd
# Our random value generator.

from rng import random_value
import AwardPoints
from createCsv import create
# Legacy comments
# Test params below, 'sg' ideal ranges -> >1 to 4:
# 'sg' is an inverse of sigma. It allows us to have the logic of a bigger number -> more accurate machine
# This will create a distribution of points on a circle based on the "sg"


def distribute(number_of_players, max_number_of_rounds, shots_per_round):
    coefficient = 5  # TO CHANGE LATER
    points = []
    coords = generate_circle_array()  # Create circle.
    sigma_begin = 1.3
    sigma_current = sigma_begin

    # One round has (shots_per_round) throws * 10 rounds in a match.
    for n in range(number_of_players):
        number_of_rounds = 0
        while number_of_rounds <= int(max_number_of_rounds):
            for y in range(shots_per_round):
                rand_coord = random_value(len(coords)-1)  # Pick random index of coords.
                gauss_sample = generate_gauss(sigma_current)

                value = coords[rand_coord]  # The value to multiply.

                # Move the point towards the centre.
                x_cord = value[0] * gauss_sample
                y_cord = value[1] * gauss_sample

                # Compression for more randomness.
                if random_value(10) >= 8:
                    y_cord = cord_compression(y_cord)
                    points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))
                    continue
                if random_value(10) >= 8:
                    x_cord = cord_compression(y_cord)
                    points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))
                    continue
                points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))
            number_of_rounds += 1
        create(rounds=max_number_of_rounds, coefficient=coefficient, sigma_current=sigma_current, shots_per_round=shots_per_round, points=points, player_index=n + 1)
        coefficient += 2
        sigma_current += 0.2
        points.clear()
    print(len(points))
    print(points)


# Generates coordinates of a circle.
def generate_circle_array():
    radius = 5
    coords = []

    theta = 0
    resolution = 0.05  # Sets the amount of coords generated for the circle, lower means more coords.
    while theta < 2 * pi:
        coords.append((radius * cos(theta), radius * sin(theta)))
        theta += resolution
    return coords


# Generate gaussian distribution with mean 0 and stddev of sg^-1.
def generate_gauss(sg):
    sample = rd.gauss(0.0, 1/sg)
    while sample > 1 or sample < -1:
        sample = rd.gauss(0.0, sg)
    return sample


# This function will compress a coordinate in order to add more randomness to the simulation.
def cord_compression(cord_to_compress):
    compressed = 2.9 * log1p(0.1 * cord_to_compress + 1)
    return compressed


if __name__ == "__main__":
    distribute(6, 10, 24)
