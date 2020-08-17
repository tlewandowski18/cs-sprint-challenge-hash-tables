def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #brute-force solution
    # for i in range(len(weights)):
    #     new_list1 = weights[0:i]
    #     new_list2 = weights[i+1:]
    #     new_list = new_list1.extend(new_list2)
    #     print(new_list1, new_list2)
    #     # for j in range(len(new_list)):
    #     #     if (weights[i] + new_list[j] == limit):
    #     #         if weights[i] >= new_list[j]:
    #     #             return (i, j)
    #     #         return(j, i)
    # return None
    weight_index = {}
    for i in range(len(weights)):
        weight_index[weights[i]] = limit - weights[i]
    for key, value in weight_index.items():
        if value in weight_index:
            if value > key



