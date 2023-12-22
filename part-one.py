#!/usr/bin/env python3

import os
from time import perf_counter_ns
from string import ascii_uppercase
from itertools import combinations

id = (f'{id1}{id2}{id3}' for id1 in ascii_uppercase for id2 in ascii_uppercase for id3 in ascii_uppercase)

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        data = input.read().split('\n')

    rows = []
    for row in data:
        rows.append(list(row))
        if not '#' in row:
            rows.append(list(row))

    for ix in range(len(rows[0]) - 1, -1, -1):
        if all([rows[iy][ix] == '.' for iy in range(len(rows))]):
            for iy in range(len(rows)):
                rows[iy].insert(ix, '.')

    galaxy_locations = {
        next(id): (ix, iy)
        for iy in range(len(rows))
        for ix in range(len(rows[0]))
        if rows[iy][ix] == '#'
    }

    answer = 0
    for a, b in combinations(galaxy_locations.keys(), 2):
        combi = 0
        combi += abs(galaxy_locations[a][0] - galaxy_locations[b][0])
        combi += abs(galaxy_locations[a][1] - galaxy_locations[b][1])
        print(a, b, combi)
        answer += combi

    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
