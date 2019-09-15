from typing import Any
from collections import defaultdict
from heapq import heappush, heappop
from dataclasses import dataclass
import sys

@dataclass
class Node():
    f: int
    g: int
    word: str
    prev: Any
    def __lt__(self, other):
        return self.f < other.f

def readFile(filename):
    file = open(filename)
    dict = []
    for line in file:
        dict.append(line.strip())
    return dict

def createGraph(dict, length):
    graph = defaultdict(list)
    placeholder = object()
    connections = defaultdict(list)

    for word in dict:
        if len(word) == length:
            for letter in range(len(word)):
                pattern = tuple(placeholder
                                if letter == j
                                else c
                                for j, c in enumerate(word)
                                )
                match = connections[pattern]
                match.append(word)
                graph[word].append(match)
    return graph


def score(start, goal):
    score = 0
    for a, b in zip(start, goal):
        if a!=b:
            score +=1
    return score

def aStar(graph, start, goal):
    closed_path = set()
    open_path = set([start])

    heap = [Node(score(start, goal), 0, start, None)]
    while heap:
        curr = heappop(heap)
        if curr.word == goal:
            path = []
            while curr:
                path.append(curr.word)
                curr = curr.prev
            return path[::-1]

        open_path.remove(curr.word)
        closed_path.add(curr.word)
        
        gScore = curr.g + 1
        for neighbors in graph[curr.word]:
            for w in neighbors:
                if w not in closed_path and w not in open_path:
                    next = Node(score(w, goal) + gScore, gScore, w, curr)
                    heappush(heap, next)
                    open_path.add(w)


def main(*argv):
    argv=argv[0]
    if len(argv)!=3:
        print("Usage: start goal dictionary.txt")
    start = argv[0]
    goal = argv[1]
    g = createGraph(readFile(argv[2]), len(goal))
    print(aStar(g, start, goal))

if __name__ == '__main__':
    main(sys.argv[1:])
