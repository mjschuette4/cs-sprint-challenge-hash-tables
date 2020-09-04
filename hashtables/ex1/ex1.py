def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for i in range(len(weights)):
        cache[weights[i]] = i
    # find match to limit
    for i in range(len(weights)):
        equalToLimit = limit-weights[i]
        if equalToLimit in cache:
            return (max(i, cache[equalToLimit]), min(i, cache[equalToLimit]))


if __name__ == "__main__":
    test = [ 4, 6, 10, 15, 16 ]
    print(get_indices_of_item_weights(test, 5, 21))
