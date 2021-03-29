# -*- coding: utf-8 -*-
# Date: 25/02/2021
# @author: Nebuda = [Tapati, Arup, Baivab, Monimoy]

import sys

sys.stdin = open('e.txt', 'r')
sys.stdout = open('e.out.txt', 'w')


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
	del inp_line

cars_route = [] # stores cars info
for i in range(t_cars): 
	inp_line = input().split()
	cars_route.append(car_route(i, inp_line[0], inp_line[1:]))
	del inp_line

# a = """3
# 1
# 2
# rue-d-athenes 2
# rue-d-amsterdam 1
# 0
# 1
# rue-de-londres 2
# 2
# 1
# rue-de-moscou 1
# """
# print(a)

# b = """5049
# 1768
# 3640
b = """4
6549
1
gfhd-gfej 1
5959
1
fjie-fjfj 1
5658
1
fgjc-fgfi 1
6606
1
gffd-ggag 1
"""
# print(b)

c = '''1
3900
1
djhc-djaa 1
3828
1
djaa-dici 1
'''
# print(c)
e = '''1
438
1
edh-edi 1
'''
print(e)
"""
2 gfhd-gfej gfej-gffe
6573 6549 gfhd-gfej 69
6549 6554 gfej-gffe 52


2 fjie-fjfj fjfj-fjff
5984 5959 fjie-fjfj 307
5959 5955 fjfj-fjff 166

2 fgjc-fgfi fgfi-gbdc
5692 5658 fgjc-fgfi 259
5658 6132 fgfi-gbdc 538

2 gffd-ggag ggag-fgig
6553 6606 gffd-ggag 67
6606 5686 ggag-fgig 2317

3 djhc-djaa djaa-dici dici-dhfg
3972 3900 djhc-djaa 4
3900 3828 djaa-dici 4
3828 3756 dici-dhfg 7


2 edh-edi edi-ejj
437 438 edh-edi 71
438 499 edi-ejj 24


"""