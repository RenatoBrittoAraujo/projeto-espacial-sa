filename = "ContactLocator1.txt"

content = ""
with open(filename) as f:
    content = f.read()

lines = [x.strip() for x in content.split("\n")]

header = lines[2]

# get all header, remove empty string
headers = [x for x in header.split(" ") if x != ""]


# if a string starts with '(', belongs to last header
for i in range(len(headers)):
    if headers[i].startswith("("):
        headers[i - 1] += " " + headers[i]
        headers[i] = ""


headers = [x for x in headers if x != ""]

headers = [
    "Pass Number",
    "Observer",
    "Time (UTCGregorian)",
    "Azimuth (deg)",
    "Elevation (deg)",
    "Range (km)",
]

print("HEADERS:", headers)

lines = lines[4:]

dataset = []

for line in lines:
    line = [x.strip() for x in line.split(" ")]

    if len(line) < 6:
        continue

    line = [x for x in line if x != ""]
    date = line[2] + " " + line[3] + " " + line[4] + " " + line[5]

    antena = line[1]
    passn = line[0]
    azim = line[6]
    elevation = line[7]
    range = line[8]

    # get a dict with header_name: value
    data = dict(zip(headers, [passn, antena, date, azim, elevation, range]))
    dataset.append(data)

import csv

# save dataset to csv
with open("dataset.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(dataset)


print(*dataset[0:10], sep="\n")
