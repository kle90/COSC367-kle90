import math

def euclidean_distance(v1, v2):
    diff = 0
    for i in range(len(v1)):
        diff += (v1[i] - v2[i]) ** 2
    return math.sqrt(diff)

def majority_element(labels):
    el_count = dict()
    
    for label in labels:
        if label in el_count:
            el_count[label] += 1
        else:
            el_count[label] = 0
    
    max_el = max(el_count, key=el_count.get)
    
    return max_el

def knn_predict(input, examples, distance, combine, k):
    
        
    

def main():
    print(majority_element("ababc") in "ab")
    
    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))

if __name__ == "__main__":
    main()