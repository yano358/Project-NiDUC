import csv


def create(rounds, coefficient, sigma_current, shots_per_round, points, player_index=int):
    number = str(player_index)

    with open('distribution' + number + '.csv', 'w', newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Round's number", "Points", "Modified points", "Average amount of points per throw", "Sigma", "Coefficient"])
        shots_taken = 0
        
        for i in range(int(rounds)):
            sum_of_points = sum_elements_range(points, shots_taken, shots_taken + shots_per_round - 1)
            sum_of_points_cond = sum_elements_with_bool(points, shots_taken, shots_taken + shots_per_round - 1)
            shots_taken += shots_per_round

            writer.writerow([i + 1, sum_of_points, sum_of_points_cond, "%.2f" % (sum_of_points / shots_per_round), "%.2f" % sigma_current, coefficient])
            

def sum_elements_range(arr, start_idx, end_idx):
    return sum([t[0] for t in arr[start_idx:end_idx+1]])


def sum_elements_with_bool(arr, start_idx, end_idx):
    return sum(val for val, bool_val in arr[start_idx:end_idx+1] if bool_val)
