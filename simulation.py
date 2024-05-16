#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:15:24 2024

@author: yuhanzhao
"""

import random

class Agent:
    def __init__(self, id, world):
        self.id = id
        self.world = world
        self.position = None

    def find_empty_patch(self):
        empty_patches = [(i, j) for i in range(self.world.size) for j in range(self.world.size) if self.world.grid[i][j] is None]
        return random.choice(empty_patches) if empty_patches else None

    def move_to_patch(self, patch):
        if patch:
            self.world.grid[patch[0]][patch[1]] = self
            self.position = patch

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = [Agent(i, self) for i in range(num_agents)]

    def initialize(self):
        for agent in self.agents:
            patch = agent.find_empty_patch()
            agent.move_to_patch(patch)

    def step(self):
        for agent in self.agents:
            if agent.position:
                self.grid[agent.position[0]][agent.position[1]] = None
            patch = agent.find_empty_patch()
            agent.move_to_patch(patch)

def main():
    world_size = 10
    num_agents = 5

    world = World(world_size, num_agents)
    world.initialize()

    num_steps = 10
    for _ in range(num_steps):
        world.step()

if __name__ == "__main__":
    main()
