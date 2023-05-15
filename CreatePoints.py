from math import sin, cos, pi, log1p


# This is only used for generation of gaussian distribution.
import random as rd
# Our random value generator.

from rng import random_value
import AwardPoints
from createCsv import create
from getCoefficient import GenerateCoeff as gen

from DartBoard import *

def distribute(number_of_players, max_number_of_rounds, shots_per_round):
    points = []
    coords = generate_circle_array()  # Create circle.
    shotCoords = []

    #sigma is the "accuracy parameter", ideal ranges are 1 to 5
    sigma_begin = 1.1
    sigma_current = sigma_begin
    
    # One round has (shots_per_round) throws * 10 rounds in a match.
    for n in range(number_of_players):
        number_of_rounds = 1
        while number_of_rounds <= int(max_number_of_rounds):
            offset = False
            for y in range(shots_per_round):
                
                rand_coord = random_value(len(coords)-1)  # Pick random index of coords.
                gauss_samplex = generate_gauss(sigma_current)
                gauss_sampley = generate_gauss(sigma_current)

                coefficientx = gen() #20% chance for an offset, this can either help or sabotage
                coefficienty = gen()
                if(coefficientx != 0 or coefficienty != 0 ):
                    offset = True
                else:
                    offset = False
                value = coords[rand_coord]  # The value to multiply.

                # Move the point towards the centre, add offset
                x_cord = value[0] * gauss_samplex
                y_cord = value[1] * gauss_sampley
                x_cord += coefficientx
                y_cord += coefficienty
                
                # Compression for more randomness. , 10% for each cord to land in a very specific area
                if random_value(10) >= 9:
                    y_cord = cord_compression(y_cord)
                    points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))
                    shotCoords.append([x_cord,y_cord])
                    continue

                if random_value(10) >= 9:
                    x_cord = cord_compression(y_cord)
                    points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))
                    shotCoords.append([x_cord,y_cord])
                    continue

                shotCoords.append([x_cord,y_cord])
                points.append(AwardPoints.calculate_points(xCord=x_cord, yCord=y_cord))

            number_of_rounds += 1
        create(rounds=max_number_of_rounds, offset=offset,
                sigma_current=sigma_current, shots_per_round=shots_per_round,
                  points=points, player_index=n + 1)
        
        if (True):
            dartBoard = DartBoard(player = n + 1, shots = shotCoords, maxRounds = max_number_of_rounds, maxShots = shots_per_round)
            dartBoard.run()
        
        sigma_current += 0.2
        shotCoords.clear()
        points.clear()
    


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
    #match is 3 throws/8 rounds, we are doing 8 throws/3 rounds which is the same
    distribute(number_of_players=6,shots_per_round=8,max_number_of_rounds=3)
