#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import requests
import pandas as pd
import random

def histogram_times(givenfilename):
    with open(givenfilename) as filename:
        csv_reader = csv.reader(filename)
        airplane_data = list(csv_reader)
    from collections import defaultdict

    crash_per_hour = defaultdict(int)
    listCrashes = list()
    for incident in airplane_data[1:]:
        if incident[1] and not any(c.isalpha() for c in incident[1]) and ':' in incident[1]:
                hour = int (incident[1].split(':')[0])
                if hour < 24:
                    crash_per_hour[hour] += 1

    for temp in sorted(crash_per_hour):
        listCrashes.append(crash_per_hour[temp])
    return listCrashes


def weigh_pokemons(filename, weight):
    given = open(filename, 'r')
    j = json.load(given)
    a = list()
    for i in j["pokemon"]:
        if((i["weight"]) == str(weight):
            a.append(i["name"])
    return a

def single_type_candy_count(filename):
    given = open(filename, 'r')
    j = json.load(given)
    a = 0
    for i in j["pokemon"]:
        if(len(i["type"]) == 1):
            if(i["candy_count"]):
                a = a + i["candy_count"]
    return a


def reflections_and_projections(points):
    points2 = np.array(points)
    points2[1] = -(points2[1]-2)
    print (points2)
    points3 = np.array(points2)
    points3[0] = -(points2[1])
    points3[1] = points2[0]
    print(points3)
    points4 = points3/20
    points4[0] = points3[0] + 3 * (points3[1])
    points4[1] = 3 * (points4[0])
    points4[1] = points4[1] / 10
    points4[0] = points4[0] / 10
    return points4

def normalize(image):
    image2 = np.array(image)
    most = image.max()
    least = image.min()
    image2 = (255/(most - least)) * (image2 - least)
    return image2


def sigmoid_normalize(image, a):
    image2 = np.array(image)
    image2 = 255 * ((1 + (np.exp(1) **((image2 - 128)*((-a)**-1))))**-1)
    return image2
