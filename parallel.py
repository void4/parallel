from itertools import combinations

resistorstxt = """3 100
1 150
1 220
1 330
2 470
1 680
4 1000
1 1500
2 2200
2 4700
4 10000
1 15000
3 22000
1 33000
3 47000
2 100000"""

resistors = {}

def parlist(rl):
	return 1/sum([1/v for v in rl])

MAXCOUNT = 10

for line in resistorstxt.split("\n"):
	count, r = line.split()
	try:
		count = min(MAXCOUNT, int(count))
	except ValueError:
		count = MAXCOUNT

	r = int(r)

	resistors[r] = count

MAXTOTAL = 10

allr = []
for r, c in resistors.items():
	for i in range(c):
		allr.append(r)

TRIES = 0
TARGET = 900
opt = [None, None, []]
for total in range(1, MAXTOTAL):
	for comb in set(combinations(allr, total)):
		R = parlist(comb)
		#print(R, comb)
		delta = abs(TARGET-R)
		if opt[1] is None or delta <= opt[1]:
			if opt[1] is not None and delta < opt[1]:
				opt[2] = []

			opt[1] = delta
			opt[0] = R
			#if comb not in opt[2]:
			opt[2].append(comb)
			print(opt)

		TRIES += 1

print(TRIES, "tries")
