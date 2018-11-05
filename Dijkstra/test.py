nodes = {
        1: {2: 1, 3: 12},
        2: {1: 1, 3: 9, 4: 3},
        3: {1: 12, 2: 9, 4: 4, 5: 5},
        4: {2: 3, 3: 4, 5: 13, 6: 15},
        5: {3: 5, 4: 13, 6: 4},
        6: {4: 15, 5: 4}
    }

for key in nodes.keys():
    temp = key
    print(nodes[temp])
    for ak in nodes[temp].keys():
        print(nodes[temp][ak])
