# To find if the point is inside a rectangle the x-coordinate lies
# between the bottom right and left coordinates of the rectangle
# and vise versa for the y-coordinates

def FindPoint(x1, y1, x2, y2, x, y):
    if (x > x1 and x < x2 and y > y1 and y < y2):
        return True
    else:
        return False

if __name__ == "__main__":
    x1, y1, x2, y2, = 0, 0, 10, 8
    x, y = 1, 5
    if FindPoint(x1, y1, x2, y2, x, y):
        print("Yes")
    else:
        print("No")