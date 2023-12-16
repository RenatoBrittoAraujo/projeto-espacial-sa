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
R = 6371
# max range
range = 600
# range with earth radius
range_earth = range + R


# filter dataset
filtered = []
for data in dataset:
    if float(data["Range (km)"]) < range:
        filtered.append(data)

# get all ranges
ranges = [float(data["Range (km)"]) for data in dataset]

# calculate standard deviation
mean = sum(ranges) / len(ranges)
variance = sum([(r - mean) ** 2 for r in ranges]) / len(ranges)
std_dev = variance**0.5

# print results
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Max Range:", max(ranges))
print("Min Range:", min(ranges))


print("FILTERED:", filtered)

print(f"Events in target of <{range}:", len(filtered))
