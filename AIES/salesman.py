import random

def main():
    # tsp = [
    # [0, 2, 9, 10],
    # [1, 0, 6, 4],
    # [15, 7, 0, 8],
    # [6, 3, 12, 0],
    # ]

    tsp = []
    num_cities = int(input("Enter number of cities: "))
    print("Enter the distance matrix row by row (space-separated):")
    for i in range(num_cities):
        row = list(map(int, input().strip().split()))
        tsp.append(row)
    solution, length = hillClimbing(tsp)
    print("Best solution found:", solution)
    print("Length of the best solution:", length)


def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution


def routeLength(tsp, currentSolution):
    routeLength = 0
    for i in range(len(currentSolution)):
        fromCity = currentSolution[i]
        toCity = currentSolution[(i + 1) % len(currentSolution)]
        routeLength += tsp[fromCity][toCity]
    return routeLength

def getNeighbours(currentSolution):
    neighbours = []
    for i in range(len(currentSolution)):
        for j in range(i + 1, len(currentSolution)):
            neighbour = currentSolution[:]
            neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours):
    bestNeighbour = neighbours[0]
    bestNeighbourRouteLength = routeLength(tsp, bestNeighbour)

    for neighbour in neighbours:
        currentLength = routeLength(tsp, neighbour)
        if currentLength < bestNeighbourRouteLength:
            bestNeighbour = neighbour
            bestNeighbourRouteLength = currentLength

    return bestNeighbour, bestNeighbourRouteLength

if __name__ == "__main__":
    main()