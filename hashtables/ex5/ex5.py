import os
def finder(files, queries):

    """
    Given paths and filenames, return all paths that match
    filename.
    """
    paths = {}
    filenames = {}
    matches = []
    # create dictionary with key as filename taken out of path, value is full path:
    for x in files:
        paths[x] = os.path.basename(x)

    for y in queries:
        filenames[y] = y
    
    # search queries against the key in the dictionary, if there are matches, add them
    # to the matches array.
    for key, value in paths.items():
        if value in filenames:
            matches.append(key)

    return matches




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
