#%% 
def generate_range(min: int, max: int, step: int) -> None:
    for i in range(min, max+1, step):
        print(i)

generate_range(2, 10, 2)

# %%
     
# %%

def generate_range(min: int, max: int, step: int) -> None:
    
    i = min
    
    while i <= max:
        print(i)
        
        i = i + step
        

generate_range(2, 10, 2)