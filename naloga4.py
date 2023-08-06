from functools import reduce
import sys
import itertools
from heapq import heappop, heappush
from math import inf

class Node:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    def __lt__(self, other) -> bool:
        return self.x < other.x or self.y < other.y
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    def __str__(self) -> str:
        return f"@({self.x}, {self.y})"
    def neighbors(self):
        return ((self.x, self.y+1), (self.x+1, self.y), (self.x, self.y-1), (self.x-1, self.y))

def manhattan(n1: Node, n2: Node) -> int:
    return abs(n1.x-n2.x)+abs(n1.y-n2.y)

# pretty much kopija a* psevdokode na wikipediji, ker python itak je psevdokoda
# brez skrbi, nisem samo copy-pasteu, ampak tudi razumem kaj sem copy-pasteu :)
def astar(start: Node, end: Node, obstacles: list[Node]):
    openSet: list[tuple[int, Node]]
    cameFrom: dict[Node, Node]
    gScore: dict[Node, int]
    fScore: dict[Node, int]

    openSet = []
    heappush(openSet, (manhattan(start, end), start))

    cameFrom = dict()

    gScore = dict()
    gScore[start] = 0

    fScore = dict()
    fScore[start] = manhattan(start, end)

    while openSet:
        current = heappop(openSet)
        currentNode = current[1]
        if currentNode == end:
            return current[0]

        for node in filter(lambda node: node not in obstacles, map(lambda tup: Node(tup[0], tup[1]), currentNode.neighbors())):
            tentative_gScore = gScore[currentNode] + 1
            if tentative_gScore < gScore.get(node, inf):
                cameFrom[node] = currentNode
                gScore[node] = tentative_gScore
                fScore[node] = tentative_gScore + manhattan(node, end)
                if node not in map(lambda tup: tup[1], openSet):
                    heappush(openSet, (fScore[node], node))
    return -1

file = sys.stdin.read().split("\n")
umag = Node(*(map(int, file[1].split(" ")[0:2]))) # haha fuck yeah, maps n' unpacking!
rescue = Node(*(map(int, file[1].split(" ")[2:4])))
numboats = int(file[2])
# uporabt 
boats = reduce(lambda acc, s: acc + [
    Node(x, y)
    # lambda inkrementira 2. value v rangeu (end) za 1, zato da je tudi krma vkljucena v range
    for x in range(*((lambda x: (min(int(x[0]), x[1]+1), max(int(x[0]), x[1]+1)))(list(map(int, s.split(" ")[0:3:2])))))
    for y in range(*((lambda y: (min(int(y[0]), y[1]+1), max(int(y[0]), y[1]+1)))(list(map(int, s.split(" ")[1:4:2])))))
    ], file[3:numboats+3], []
)
print(astar(rescue, umag, boats)-1)
