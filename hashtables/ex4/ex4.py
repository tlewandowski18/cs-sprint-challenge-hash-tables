def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    number_index = {}
    for number in a:
        if -number in number_index:
            number_index[-number] = True
        else:
            number_index[number] = False
    result = []
    for key, value in number_index.items():
        if value == True:
            if key < 0:
                result.append(-key)
            else:
                result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
