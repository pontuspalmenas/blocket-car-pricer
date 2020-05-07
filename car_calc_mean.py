import statistics
import sys


if len(sys.argv) != 2 or len(sys.argv[1]) < 1:
	print(f"Usage: {sys.argv[0]} [file]")
	sys.exit()
f = open(sys.argv[1], "r")
dict = {}
for l in f.readlines():
	v = l.strip().split(",")
	k = dict.get(str(v[0]), [])
	if len(v[1]) > 4: # remove some leasing cars that were included despite the filter
		k.append(int(v[1]))
		dict[str(v[0])] = sorted(k)

for year in dict:
	mean = int(statistics.mean(dict[year]))
	print(f"{year},{mean}")
