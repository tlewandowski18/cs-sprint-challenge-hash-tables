def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #set up number index
    number_index = {}
    #loop through each list in array
    for list in arrays:
        #loop through each number in list
        for number in list:
            #check if number(key) in index
            if number in number_index:
                #if so increase frequency(value) by one
                number_index[number] += 1
            else:
                #if not create entry in index and set frequency at 1
                number_index[number] = 1
    #create intersections array and append all numbers that have a frequency equal to length of arrays
    intersections = []
    for key, value in number_index.items():
        if value == len(arrays):
            intersections.append(key)

    return intersections


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
