import numpy as np

counter = 1

x = 4

for i in range(0, 16):
    mod = counter % x
    print(f"counter {i} mod{x} = {mod}")
    
    if mod in range(0,2):
        print("kladne")
    elif mod in range(2,4):
        print("zaporne")
    else:
        print("how?")
        break
        
    if mod == 0:
        counter = 1
    else:
        counter += 1

