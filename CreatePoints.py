from math import sin, cos, pi, log1p
from matplotlib import pyplot as plt

#this is only used for generation of gaussian distribution
import random as rd

#our random value generator
from rng import random_value
import AwardPoints

#test params below, sg ideal ranges-> >1 to 4:
#sg is an inverse of sigma so we can have the logic of bigger number -> more accurate machine
sg = 0.2

#This will create a distribution of points on a circle based on the "sg"
def distribute():
    points = []
    coords = generateCircleArray() #create circle
    #one round has 3 throws * 8 rounds in a match
    for y in range(24):
        randCoord = random_value(len(coords)-1) #pick random index of coords
        gaussSample = generateGauss()

        value = coords[randCoord] #value to multiply

        #move the point toward the center
        xCord = value[0]*gaussSample
        yCord = value[1]*gaussSample

        #compression for mor randomness
        if(random_value(10) >= 8):
            yCord = cordCompression(yCord)
            plt.plot(xCord,yCord,marker="o",markersize=5,markeredgecolor="black",markerfacecolor="black")
            continue
        if(random_value(10)>= 8):
            xCord = cordCompression(yCord)
            plt.plot(xCord,yCord,marker="o",markersize=5,markeredgecolor="yellow",markerfacecolor="yellow")
            continue
        
        #add to graph
        plt.plot(xCord, yCord, marker="o", markersize=5, markeredgecolor="blue", markerfacecolor="green")

        #points.append(AwardPoints.calculatePoints(xCord=xCord,yCord=yCord))

    #plot circle
    for x in range(len(coords)):
        plt.plot((coords[x][0]), coords[x][1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
    plt.show()

#generates coordinates of a circle
def generateCircleArray():
    radius = 5
    coords = []

    theta = 0
    resolution = 0.05 #sets the amount of coords generated for the circle, lower means more coords
    while theta < 2*pi:
        coords.append((radius*cos(theta), radius*sin(theta)))
        theta+=resolution
    return coords

#generate gaussian distribution with mean 0 and stddev of sg^-1
def generateGauss():
    sample = rd.gauss(0.0,1/sg)
    while sample > 1 or sample < -1:
        sample = rd.gauss(0.0,sg)
    return sample

#this function will compress a coordinate in order to add more randomness to the simulation
def cordCompression(cordToCompress):
    compressed = 2.9*log1p(0.1*cordToCompress+1)
    return compressed

if __name__ == "__main__":
    distribute()