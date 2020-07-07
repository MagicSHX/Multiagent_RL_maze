import random
from random import randint
import pandas as pd
import torch

def exchange_value_in_scequence(a, b):
    if a > b:
        return (b, a)
    else:
        return (a, b)


def trancate_matrix(play_ground, centre_point, row, column):
    return play_ground[centre_point[0] - row : centre_point[0] + row + 1, centre_point[1] - column : centre_point[1] + column + 1]


def wall_generation(row, column, no_of_wall):
    outline = []
    for i in range(0, no_of_wall):
        line = [randint(2, row - 2) + row, randint(2, column - 2) + column, randint(2, row - 2) + row, randint(2, column - 2) + column]
        line[0], line[2] = exchange_value_in_scequence(line[0], line[2])
        line[1], line[3] = exchange_value_in_scequence(line[1], line[3])
        if randint(0,1) == 0:
            line[2] = line[0]
        else:
            line[3] = line[1]
        outline.append(line)
    return outline

def target_generation(row, column, no_of_target):
    target = []
    for i in range(0, no_of_target):
        point = [randint(1, row - 1) + row, randint(1, column - 1) + column]
        target.append(point)
    return target

def agent_generation(row, column, no_of_agent):
    agent = []
    for i in range(0, no_of_agent):
        point = [randint(1, row - 1) + row, randint(1, column - 1) + column]
        agent.append(point)
    return agent

def data_input(file_path):
    #to explore: remove duplicatioin - if both input and score are same, then remove duplication
    data_original = pd.read_csv(file_path)
    #data_original = data_original.drop_duplicates(subset=None, keep='first', inplace=False)
    torch_tensor = torch.tensor(data_original.values, dtype=torch.float)
    #print(torch_tensor)
    return torch_tensor