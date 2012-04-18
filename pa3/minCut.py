import pprint
import random
import copy

def buildAdjListFromFile(file):
    adjList = []
    f = open(file)
    for line in f:
        vertice = line.strip().split()
        for i in range(len(vertice)):
            vertice[i] = int(vertice[i])
        vertex = []
        vertex.append(vertice[0])
        vertexAdj = vertice[1:]
        adjInfo = []
        adjInfo.append(vertex)
        adjInfo.append(vertexAdj)
        adjList.append(adjInfo)
    return adjList
    

def kargerAlgorithm(adjList):
    if len(adjList) > 2:
        newAdjList = contract(adjList)
        #pp.pprint(adjList)
        return kargerAlgorithm(newAdjList)
    else:
        return adjList

def contract(adjList):
    newAdjList = copy.deepcopy(adjList)
    x = random.randint(0, len(newAdjList) - 1)
    y = random.randint(0, len(newAdjList[x][0]) - 1)
    # pick a random vertex X
    vertex_x = newAdjList[x][0][y]
    z = random.randint(0, len(newAdjList[x][1]) - 1)
    # pick a random vertex Y, X and Y are connected
    vertex_y = newAdjList[x][1][z]
    
    # find index of vertex Y in the adj list by its value
    vertex_y_index = findVextex(vertex_y, newAdjList)
    
    # merge vertex X and Y and all edges with X and Y
    newAdjList[x][0].extend(newAdjList[vertex_y_index][0])
    newAdjList[x][1].extend(newAdjList[vertex_y_index][1])
    
    # remove self loop
    for item in newAdjList[x][0]:
        for i in range(newAdjList[x][1].count(item)):
            if item in newAdjList[x][1]:
                newAdjList[x][1].remove(item)
            
    # remove vertex Y from adj list
    newAdjList.pop(vertex_y_index)
    return newAdjList
    
def findVextex(vetex_val, adjList):
    for i in range(len(adjList)):
        if vetex_val in adjList[i][0]:
            return i
    return -1

if __name__ == "__main__":
    #pp = pprint.PrettyPrinter()
    adjList = buildAdjListFromFile("kargerAdj.txt")
    #pp.pprint(adjList)
    #adjList = [[[1],[2,3,4]],[[2],[1,3,4]],[[3],[1,2,4]],[[4],[1,2,3]]]
    min_cuts = []
    # run more than n**2 times to get the right min-cut
    for i in range(2 * len(adjList)**2):
        min_cuts.append(len(kargerAlgorithm(adjList)[0][1]))
    print min(min_cuts)