from typing import Any
from collections import defaultdict
from heapq import heappush, heappop
from dataclasses import dataclass
import sys


@dataclass
class Node():
    """
    Node dataclass used for A* algorithm to store f and g values easily
    :param f cost of going to the next node
    :param g cost of all previous connections
    :param word current word of this node
    :param prev All the previous connected nodes
    """
    f: int
    g: int
    word: str
    prev: Any

    def __lt__(self, other):
        return self.f < other.f


def readFile(filename):
    """
    function that takes a filename and turns into dictionary list
    :param filename: string
    :return: dictionary of words
    """
    file = open(filename)
    dict = []
    for line in file:
        dict.append(line.strip())
    return dict


def createGraph(dict, length):
    """
    Reads a dictionary and creates a connected graph of words that are length long
    Uses default dictionary to create the graph easy
    :param dict: a list of words
    :param length: length of goal/start word // this allows all other words in dictonary to be excluded
    :return: a graph of connected words
    """
    graph = defaultdict(list)
    placeholder = object()
    connections = defaultdict(list)

    for word in dict:
        if len(word) == length:  # check if the word is equal to goal
            for letter in range(len(word)):  # iterate through each letter
                pattern = tuple(placeholder
                                if letter == j
                                else c
                                for j, c in enumerate(word)
                                )  # use enumerate to go through each word and letter to check for matches
                match = connections[pattern]
                match.append(word)
                graph[word].append(match)
    return graph


def score(start, goal):
    """
    heuristic score function that determines how many letters are not equal to the goal
    :param start: the current word string
    :param goal:  the goal string
    :return: value 0-n length of string; depending on how many letter are equal to eachother
    """
    score = 0
    for a, b in zip(start, goal):
        if a != b:
            score += 1
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
    argv = argv[0]
    if len(argv) != 3:
        print("Usage: start goal dictionary.txt")
    start = argv[0]
    goal = argv[1]
    g = createGraph(readFile(argv[2]), len(goal))
    print(aStar(g, start, goal))


if __name__ == '__main__':
    main(sys.argv[1:])
