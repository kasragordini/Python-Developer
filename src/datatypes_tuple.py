# to pair up the girl and boy names, we use zip as an iterator to aggregate iterables (here iterables are lists)
pairs = zip(girl_names, boy_names)

# then we iterate over pairs and use enumerate to rank them
for rank, pair in enumerate(pairs):
    # to unpack pair
    girl_name, boy_name = pair
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')

### output:
# 
Rank 1: Jada and Josiah
Rank 2: Emily and Ethan
Rank 3: Ava and David
Rank 4: Serenity and Jayden
Rank 5: Claire and Mason
Rank 6: Sophia and Ryan
Rank 7: Sarah and Christian
Rank 8: Ashley and Isaiah
Rank 9: Chaya and Jayden
Rank 10: Abigail and Michael
Rank 11: Zoe and Noah
Rank 12: Leah and Samuel
Rank 13: Hailey and Sebastian
Rank 14: Ava and Noah
Rank 15: Olivia and Dylan
Rank 16: Emma and Lucas
Rank 17: Chloe and Joshua
Rank 18: Sophia and Angel
Rank 19: Aaliyah and Jacob
Rank 20: Angela and Matthew
Rank 21: Camila and Josiah
Rank 22: Savannah and Jacob
Rank 23: Serenity and Muhammad
Rank 24: Chloe and Alexander
Rank 25: Fatoumata and Jason





# we create the normal variable
normal = 'simple'

# then we create the mistaken variable
error = 'trailing comma',

# After printing can be seen that comma in 'error' makes the type tuple
print(type(normal))
print(type(error))

### output:
# <class 'str'>
# <class 'tuple'>
