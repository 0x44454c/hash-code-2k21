# -*- coding: utf-8 -*-
# Author: DelusionaL
# Team: Nebuda

import sys

def eve():
	fLine = input().split()
	pizza_count = int(fLine[0])
	t2_count = int(fLine[1])
	t3_count = int(fLine[2])
	t4_count = int(fLine[3])
	# total_person = t2_count*2 + t3_count*3 + t4_count*4
	pizzas = []
	ingredients = []
	for i in range(pizza_count):
		inp_line = input().split()
		ingredients += inp_line[1:]
		pizzas.append(inp_line)
	# unique_ing = set(ingredients)


	count_del = 0
	out = []
	pc = pizza_count-1
	# sampling for 2 persons teams
	while pc >= 0 and t2_count > 0:
		ar = [2]
		i = 2
		while pc>=0 and i > 0:
			i-=1
			ar.append(pc)
			pc -= 1
		if len(ar) == ar[0]+1:
			out.append(ar)
			count_del += 1
		t2_count -= 1

	# sampling for 3 persons teams
	while pc >= 0 and t3_count > 0:
		ar = [3]
		i = 3
		while pc>=0 and i > 0:
			i-=1
			ar.append(pc)
			pc -= 1
		if len(ar) == ar[0]+1:
			out.append(ar)
			count_del += 1
		t3_count -= 1

	# sampling for 4 persons teams
	while pc >= 0 and t4_count > 0:
		ar = [4]
		i = 4
		while pc>=0 and i > 0:
			i-=1
			ar.append(pc)
			pc -= 1
		if len(ar) == ar[0]+1:
			out.append(ar)
			count_del += 1
		t4_count -= 1

	print(count_del)
	for i in range(len(out)):
		print(" ".join(map(str, out[i])))

if __name__ == "__main__":
	filenames = ['a_example','b_little_bit_of_everything', 'c_many_ingredients', 'd_many_pizzas', 'e_many_teams']

	for name in filenames:
		##- For taking input and out from file -##
		sys.stdin = open(f"{name}.in", 'r')
		sys.stdout = open(f"{name}.out", 'w')
		##########################################
		eve()