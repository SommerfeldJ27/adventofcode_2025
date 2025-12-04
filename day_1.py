rotations = []

#read and parse file
with open("rotations_new.txt") as file:
    for line in file:
        direction, value_str = line.strip().split(",")
        value = int(value_str)

        if direction == "l":
            degrees = -value     #left rotation
        else:  #direction == "r"
            degrees = value      #right rotation
        rotations.append(degrees)

position = 50 
zero_hits = []

for deg in rotations:
    position = (position + deg) % 360
    if position == 0:
        zero_hits.append(deg)

#print results
if zero_hits:
    print("First hit 0 at rotation:", zero_hits[0])
else:
    print("Never returned to 0")

if len(zero_hits) > 1:
    print("Hits 0 at:", zero_hits)
