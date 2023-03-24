#Power level scaling computations (WIP)
from numpy import mean

y = 0
current_items = [1804, 1804, 1803, 1600, 1600, 1600, 1600, 1600]

PL = mean(current_items)
x = 1
z = 0
PL_old = 0
print(PL)
while x :
    current_items.append(PL)
    current_items.remove(min(current_items))
    PL = mean(current_items)//1
    print(PL)
    if PL_old == PL:
        z+=1
    else:
        z=0
    if z > 100:
        x=0
    PL_old = PL 
print(PL)
