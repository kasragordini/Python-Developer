# to add individual data elements to a list we can use the .append() method. However, if we want to combine a list with another array type (list, set, tuple), we can use the .extend() method on the list

# to create a list containing the baby_names
baby_names = ['Ximena', 'Aliza', 'Ayden', 'Calvin']

# to extend baby_names with 'Rowen' and 'Sandeep'
print(baby_names.extend(['Rowen', 'Sandeep']))

# to find the position of 'Rowen'
position = baby_names.index('Rowen')

# to remove 'Rowen' from baby_names
baby_names.pop(position)

# Print baby_names
print(baby_names)

### Output:
# ['Ximena', 'Aliza', 'Ayden', 'Calvin', 'Sandeep']



### list of lists: records

[['2014', 'F', '20799', 'Emma'],
 ['2014', 'F', '19674', 'Olivia'],
 ['2014', 'F', '18490', 'Sophia'],
 ['2014', 'F', '16950', 'Isabella'],
 ['2014', 'F', '15586', 'Ava'],
 ['2014', 'F', '13442', 'Mia'],
 ['2014', 'F', '12562', 'Emily'],
 ['2014', 'F', '11985', 'Abigail'],
 ['2014', 'F', '10247', 'Madison'],
 ['2014', 'F', '10048', 'Charlotte'],
 ['2014', 'F', '9564', 'Harper'],
 ['2014', 'F', '9542', 'Sofia'],
 ['2014', 'F', '9517', 'Avery'],
 ['2014', 'F', '9492', 'Elizabeth'],
 ['2014', 'F', '8727', 'Amelia'],
 ['2014', 'F', '8692', 'Evelyn'],
 ['2014', 'F', '8489', 'Ella'],
 ['2014', 'F', '8469', 'Chloe'],
 ['2014', 'F', '7955', 'Victoria'],
 ['2014', 'F', '7589', 'Aubrey'],
 ['2014', 'F', '7554', 'Grace'],
 ['2014', 'F', '7358', 'Zoey'],
 ['2014', 'F', '7061', 'Natalie'],
 ['2014', 'F', '6950', 'Addison'],
 ['2014', 'F', '6869', 'Lillian'],
 ['2014', 'F', '6767', 'Brooklyn']]

# to create the list comprehension
baby_names = [row[3] for row in records]
    
# to sort baby names in ascending alphabetical order
print(sorted(baby_names))

### output
# ['Abigail', 'Addison', 'Amelia', 'Aubrey', 'Ava', 'Avery', 'Brooklyn', 'Charlotte', 'Chloe', 'Elizabeth', 'Ella', 'Emily', 'Emma', 'Evelyn', 'Grace', 'Harper', 'Isabella', 'Lillian', 'Madison', 'Mia', 'Natalie', 'Olivia', 'Sofia', 'Sophia', 'Victoria', 'Zoey']
