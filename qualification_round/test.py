# -*- coding: utf-8 -*-
# Date: 25/02/2021
# @author: Nebuda = [Tapati, Arup, Baivab, Monimoy]

import sys

sys.stdin = open('a.txt', 'r')
sys.stdout = open('a.out.txt', 'w')


class street:
	def __init__(self, id, si, ei, name, time):
		self.id = id
		self.si = si
		self.ei = ei
		self.name = name
		self.time = time

class car_route:
	def __init__(self, id, no_route, path):
		self.id	= id
		self.no_route = no_route
		self.path = path


fLine = input().split()

total_time =int(fLine[0])
t_intersections = int(fLine[1])
t_streets = int(fLine[2])
t_cars = int(fLine[3])
bonus = int(fLine[4])


streets = [] # stores street info
for i in range(t_streets):
	inp_line = input().split()
	streets.append(street(i, inp_line[0], inp_line[1], inp_line[2], inp_line[3]))

cars_route = []
for i in range(t_cars): # stores cars info
	inp_line = input().split()
	cars_route.append(car_route(i, inp_line[0], inp_line[1:]))

