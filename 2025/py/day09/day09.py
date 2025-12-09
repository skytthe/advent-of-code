import sys

def lines_intersect(p1, p2, p3, p4):
    """
    Check whether line segment p1->p2 intersects with line segment p3->p4.
    Points are given as tuples: (x, y)
    """

    def orientation(a, b, c):
        """Returns the orientation of the triplet (a, b, c).
           0 -> collinear
           1 -> clockwise
           2 -> counterclockwise
        """
        val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def on_segment(a, b, c):
        """Check if point b lies on segment a->c (collinear case)."""
        return (min(a[0], c[0]) <= b[0] <= max(a[0], c[0]) and
                min(a[1], c[1]) <= b[1] <= max(a[1], c[1]))

    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    # General case: segments intersect
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases (collinear overlaps)
    if o1 == 0 and on_segment(p1, p3, p2): return True
    if o2 == 0 and on_segment(p1, p4, p2): return True
    if o3 == 0 and on_segment(p3, p1, p4): return True
    if o4 == 0 and on_segment(p3, p2, p4): return True

    return False


example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split("\n")

with open('2025/py/day09/day09.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = example
data = lines

data = [list(map(int, line.split(","))) for line in data]

biggest1 = 0
for i in range(len(data)-1):
    for j in range(i,len(data)):
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if area > biggest1:
            biggest1 = area

print(biggest1)


data.append(data[0])
lines = []
for (x1, y1), (x2, y2) in zip(data, data[1:]):
    lines.append(((x1, y1), (x2, y2)))

biggest2 = 0
bp =[]
bbox =[]
for i in range(len(data)-1):
    for j in range(i,len(data)):
        area = (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1)
        if area >= biggest2:
            x1,y1 = data[i][0],data[i][1]
            x2,y2 = data[j][0],data[j][1]

            top_left     = (min(x1, x2) + 0.5, min(y1, y2) + 0.5)
            top_right    = (max(x1, x2) - 0.5, min(y1, y2) + 0.5)
            bottom_left  = (min(x1, x2) + 0.5, max(y1, y2) - 0.5)
            bottom_right = (max(x1, x2) - 0.5, max(y1, y2) - 0.5)

            box = [top_right,top_left,bottom_left, bottom_right,top_right]            

            intersect = any(
                lines_intersect(p1, p2, lp1, lp2)
                for lp1, lp2 in lines
                for p1, p2 in zip(box,box[1:])
            )            

            if not intersect:
                biggest2 = area
                bp = [(x1,y1),(x2,y2)]
                bbox = box
    
print(biggest2)




# import matplotlib.pyplot as plt

# x_vals1 = [p[0] for p in data]
# y_vals1 = [p[1] for p in data]

# x_vals2 = [p[0] for p in bbox]
# y_vals2 = [p[1] for p in bbox]

# x_vals3 = [p[0] for p in bp]
# y_vals3 = [p[1] for p in bp]

# plt.plot(x_vals1, y_vals1, marker='o')
# plt.plot(x_vals2, y_vals2)
# plt.plot(x_vals3, y_vals3, marker='x')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Line Plot Through Points")
# plt.grid(True)
# plt.show()