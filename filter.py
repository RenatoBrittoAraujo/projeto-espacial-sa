import csv

with open("dataset.csv", "r") as f:
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

print("FILTERED:", filtered)

print("Events:", len(filtered))
