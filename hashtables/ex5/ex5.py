# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    queries_index = {}
    for query in queries:
        queries_index[query] = []
    final_list = []
    for file in files:
        file_list = file.split("/")
        if file_list[-1] in queries_index:
            final_list.append(file))
    return final_list

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
