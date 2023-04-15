from math import atan2, sqrt, pi


#given coordinates of where the shot landed, returns the points for that singular shot
def calculatePoints(xCord, yCord):
    angle = calcAngle(xCord,yCord)
    #calculates which area would the shot land in
    for i in range(9,360,18):
        if angle > (i % 360) and angle <= ((i + 18)%360):
            area = 1 + (i - 9) / 18
    #checks for amount of points in area shot landed in
    match area: 
        case 1:
            points = 13
        case 2:
            points = 4
        case 3:
            points = 18
        case 4:
            points = 1
        case 5:
            points = 20
        case 6:
            points = 5
        case 7:
            points = 12
        case 8:
            points = 9
        case 9:
            points = 14
        case 10:
            points = 11
        case 11:
            points = 8
        case 12:
            points = 16
        case 13:
            points = 7
        case 14:
            points = 19
        case 15:
            points = 3
        case 16:
            points = 17
        case 17:
            points = 2
        case 18:
            points = 15
        case 19:
            points = 10
        case 20:
            points = 6
        
    #calculates the modifier of points, 0 if the shot was beyond the radius
    line_length = sqrt(xCord*xCord + yCord * yCord)
    if line_length <= 0.5:
        points = 50
        point_mod = 1

    elif line_length <= 3.0 :
        point_mod = 1

    elif line_length <= 3.25:
        point_mod = 3

    elif line_length <= 4.75:
        point_mod = 1

    elif line_length <= 5.0:
        point_mod = 2
    
    else:
        point_mod = 0

    return points * point_mod

#returns angle of a line between the point and (0,0)
def calcAngle(xCord, yCord):
    return (270 - atan2(0 - xCord, 0 - yCord) * 180 / pi) % 360
