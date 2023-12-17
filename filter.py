import math
import csv

import sys

if len(sys.argv) < 2:
    print("Usage: python3 filter.py <dataset_filename>")
    exit(1)

# get first arg
dataset_filename = f"dataset{sys.argv[1]}.csv"

with open(dataset_filename, "r") as f:
    reader = csv.DictReader(f)
    dataset = list(reader)

# earth radius
R = 6378.1366
# max range
range = 600
# range with earth radius
range_earth = range + R

dist_antena = R + 1.5

INTERVAL_STEP_SIZE = 5

# get all ranges
ranges2 = [float(data["Range (km)"]) for data in dataset]

ranges = []
for data in dataset:
    d = float(data["Range (km)"])
    o = float(data["Elevation (deg)"])
    o = math.radians(o)

    y = dist_antena

    vx = y + math.sin(o) * d
    vy = math.cos(o) * d

    alt = math.sqrt(vx**2 + vy**2) - dist_antena

    res = alt

    # res = r * math.cos(e)
    ranges.append(res)

    # print("D:", d, "O (deg):", math.degrees(o), "alt:\t", res)
    # if res < range:

# calculate standard deviation
mean = sum(ranges) / len(ranges)
variance = sum([(r - mean) ** 2 for r in ranges]) / len(ranges)
std_dev = variance**0.5

mean2 = sum(ranges2) / len(ranges2)
variance2 = sum([(r - mean) ** 2 for r in ranges2]) / len(ranges2)
std_dev2 = variance**0.5

# save all ranges to file
# with open("ranges.txt", "w") as f:
#     f.write("\n".join([str(r) for r in ranges]))


# print results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Max Range:", max(ranges))
print("Min Range:", min(ranges))


# filter dataset
filtered = []
for val in ranges:
    if val < range:
        filtered.append(val)
# filter dataset
filtered2 = []
for val in ranges2:
    if val < range:
        filtered2.append(val)


# print("FILTERED:", filtered)

print(f"Events in target of <{range}:", len(filtered) * INTERVAL_STEP_SIZE)
print("-------------")
print("Mean (linear):", mean2)
print("Standard Deviation (linear):", std_dev2)
print("Max Range (linear):", max(ranges2))
print("Min Range (linear):", min(ranges2))
print(f"Events in target of <{range} (linear):", len(filtered2) * INTERVAL_STEP_SIZE)

# save printed info to res%d.txt
with open(f"res{sys.argv[1]}.txt", "w") as f:
    f.write(f"Mean: {mean}\n")
    f.write(f"Standard Deviation: {std_dev}\n")
    f.write(f"Max Range: {max(ranges)}\n")
    f.write(f"Min Range: {min(ranges)}\n")
    f.write(f"Events in target of <{range}: {len(filtered) * INTERVAL_STEP_SIZE}\n")
    f.write(f"Mean (linear): {mean2}\n")
    f.write(f"Standard Deviation (linear): {std_dev2}\n")
    f.write(f"Max Range (linear): {max(ranges2)}\n")
    f.write(f"Min Range (linear): {min(ranges2)}\n")
    f.write(
        f"Events in target of <{range} (linear): {len(filtered2) * INTERVAL_STEP_SIZE}\n"
    )
    # f.write(f"FILTERED: {filtered}\n")
