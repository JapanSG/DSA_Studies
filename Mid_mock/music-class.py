'''test'''
import math
total = 0
for x in range(11):
    for y in range(11):
        if x+y > 10:
            continue
        p = math.factorial(x+y+(10-(x+y)))/(math.factorial(x)*math.factorial(y)*math.factorial(10-(x+y))) * ((0.1)**x) * ((0.3)**y) * ((0.6)**(10-(x+y))) 
        print(f"P(X = {x}, Y = {y}) = {p}")
        total += p
print(f"Total = {total}")
