# -*- coding: utf-8 -*-
"""

"""

#%%
#for i in range WINKEL
#for j in range WINKEL
def funk():
    c = 0 
    
    for i in range(1,10):
        if c in [x for x in range(0,10) if x%2 == 0 ]:
            for j in range(1,10):
                print(i,j)
            c = c+1
        else:
            for j in range(9,0, -1):            
                print(i,j)
            c = c+1
        
#%%
