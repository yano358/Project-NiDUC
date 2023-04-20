from math import atan2, sqrt, pi


pts = {
    1:13,
    2:4,
    3:18,
    4:1,
    5:20,
    6:5,
    7:12,
    8:9,
    9:14,
    10:11,
    11:8,
    12:16,
    13:7,
    14:19,
    15:3,
    16:17,
    17:2,
    18:15,
    19:10,
    20:6
}

#given coordinates of where the shot landed, returns the points for that singular shot
def calculatePoints(xCord, yCord):
    angle = calcAngle(xCord,yCord)
    #calculates which area would the shot land in
    for i in range(9,360,18):
        if angle > (i % 360) and angle <= ((i + 18)%360):
            area = 1 + (i - 9) / 18
    #checks for amount of points in area shot landed in
    points = pts(area)
        
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
