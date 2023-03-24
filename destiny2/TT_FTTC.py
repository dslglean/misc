# Triple Tap/FTTC Calculator (Python)

starter = int(100000) #Base Magazine Size
mag = starter
shot = int(0)
proc = int(0)
while mag:
    shot+=1
    mag-=1
#---------------FTTC-------------------
    if not shot%4:
        mag+=2
        proc+=1
#------------Triple Tap----------------
    #if not shot%3:
    #    mag+=1
    #    proc+=1
#--------------------------------------
print("Total shots = ")
print(shot)    

print("Magazine % increase = ")
print(100*(shot-starter)/starter)

print("Perk activations = ")
print(proc)    

