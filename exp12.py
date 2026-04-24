
import matplotlib.pyplot as plt

# Window
xmin, ymin = 10, 10
xmax, ymax = 100, 100

# Region codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

def compute_code(x, y):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        if code1 == 0 and code2 == 0:
            return True, x1, y1, x2, y2
        elif (code1 & code2) != 0:
            return False, None
        else:
            code_out = code1 if code1 != 0 else code2

            if code_out & TOP:
                x = x1 + (x2 - x1)*(ymax - y1)/(y2 - y1)
                y = ymax
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1)*(ymin - y1)/(y2 - y1)
                y = ymin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1)*(xmax - x1)/(x2 - x1)
                x = xmax
            elif code_out & LEFT:
                y = y1 + (y2 - y1)*(xmin - x1)/(x2 - x1)
                x = xmin

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

# Input line
x1, y1 = 5, 20
x2, y2 = 120, 80

result = cohen_sutherland(x1, y1, x2, y2)

plt.figure()

# Draw window
plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin], label="Window")

# Original line
plt.plot([x1,x2],[y1,y2], linestyle='dashed', label="Original Line")

if result[0]:
    _, cx1, cy1, cx2, cy2 = result
    plt.plot([cx1,cx2],[cy1,cy2], linewidth=2, label="Clipped Line")
    print(f"Clipped Line: ({cx1:.2f},{cy1:.2f}) to ({cx2:.2f},{cy2:.2f})")
else:
    print("Line Rejected")

plt.legend()
plt.title("Cohen-Sutherland Line Clipping")
plt.grid()
plt.xlim(0,150)
plt.ylim(0,150)

plt.show()
