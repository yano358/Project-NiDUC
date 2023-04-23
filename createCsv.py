import csv
def create(sigBegin, sigEnd, shotsPerRound, points):
    
    with open('distribution.csv', 'w', newline="") as file:
        writer = csv.writer(file, dialect='excel', delimiter = ';')
        writer.writerow(["Nr Rundy", "Punkty", "Punkty z modyfikatorem", "Średnia ilość pkt'ów na rzut", "Sigma"])
        shotsTaken = 0
        rounds = (sigEnd - sigBegin) / 0.1
        
        for i in range(int(rounds) + 1):
            sumOfPoints = sum_elements_range(points, shotsTaken, shotsTaken + shotsPerRound - 1)
            sumOfPointsCond = sum_elements_with_bool(points, shotsTaken, shotsTaken + shotsPerRound - 1)
            shotsTaken += shotsPerRound
            writer.writerow([i+1,sumOfPoints,sumOfPointsCond, "%.2f" % (sumOfPoints/shotsPerRound), "%.2f" % sigBegin])
            sigBegin += 0.1
            
        

def sum_elements_range(arr, start_idx, end_idx):
    return sum([t[0] for t in arr[start_idx:end_idx+1]])

def sum_elements_with_bool(arr, start_idx, end_idx):
    return sum(val for val, bool_val in arr[start_idx:end_idx+1] if bool_val)
        