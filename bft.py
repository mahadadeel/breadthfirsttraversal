##Breadth First Traversal Algorithm

def validateMatrix(matrix):
    for i in matrix:
        if len(i) != len(matrix):
            return False
    return True

def breadthFirstTraversal(key, matrix):
    if type(key) is tuple and len(key) == len(matrix) and validateMatrix(matrix):
        unvisitedNodes = list(key)
        visitedNodes = []
        queue = []
        queue.append(key[0])
        unvisitedNodes.remove(key[0])
        visitedNodes.append(key[0])
        print("INITIAL NODE")
        for i in range(len(matrix[0])):
            if matrix[0][i] == 1:
                unvisitedNodes.remove(key[i])
                visitedNodes.append(key[i])
                queue.append(key[i])
                print("unvisited nodes",unvisitedNodes)
                print("visited nodes",visitedNodes)
                print("queue",queue)
        print("MAIN BODY OF MATRIX")
        while len(queue) > 0:
            workingValue = queue.pop(0)
            workingValueIndex = key.index(workingValue)
            for i in range(len(matrix[workingValueIndex])):
                if matrix[workingValueIndex][i] == 1:
                    if key[i] not in visitedNodes:
                        unvisitedNodes.remove(key[i])
                        visitedNodes.append(key[i])
                        queue.append(key[i])
                        print("working value",workingValue)
                        print("working value index",workingValueIndex)
                        print("unvisited nodes",unvisitedNodes)
                        print("visited nodes",visitedNodes)
                        print("queue",queue)
        print("FINISHED")
        print("unvisited nodes",unvisitedNodes)
        print("visited nodes",visitedNodes)
        print("queue",queue)

adjacencyMatrix = [[0,1,1,1,0,0,0,0,0],
                   [1,0,1,0,1,0,0,0,0],
                   [1,1,0,1,0,1,1,0,0],
                   [1,0,1,0,0,0,1,0,0],
                   [0,1,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,1],
                   [0,0,1,1,0,0,0,1,0],
                   [0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,1,0,0,0]]

breadthFirstTraversal(('A','B','C','D','E','F','G','H','I'), adjacencyMatrix)
