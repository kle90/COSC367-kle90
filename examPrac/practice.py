def select(population, error, max_error, r):        
    roulette_list = []
    total = 0
    for individual in population:
        total += (max_error - error(individual))
        roulette_list.append(total)

    for tup in enumerate(roulette_list):
        if total * r < tup[1]:
            return population[tup[0]]    
    

def estimate(time, observations, k):
    time_list = [(abs(time - items[0]), items[1]) for items in observations]
    time_list.sort()
    
    calc_list = []
    for i in range(len(time_list)):
        if i <= k - 1:
            calc_list.append(time_list[i])            
        if i > k - 1:
            if time_list[i][0] <= calc_list[k-1][0]:
                calc_list.append(time_list[i])
        
    return_val = 0
    for items in calc_list:
        return_val += items[1]
    
    denom = len(calc_list)
    
    return return_val / len(calc_list)
    
    
def main():
    observations = [
        (-1, 1),
        (0, 0),
        (-1, 1),
        (5, 6),
        (2, 0),
        (2, 3),
    ]
    
    for time in [-1, 1, 3, 3.5, 6]:
        print(estimate(time, observations, 2))
    
if __name__ == "__main__":
    main()