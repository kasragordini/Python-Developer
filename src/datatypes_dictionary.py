squirrels= 
[('Marcus Garvey Park', ('Black', 'Cinnamon', 'Cleaning', None)),
 ('Highbridge Park',
  ('Gray',
   'Cinnamon',
   'Running, Eating',
   'Runs From, watches us in short tree')),
 ('Madison Square Park', ('Gray', None, 'Foraging', 'Indifferent')),
 ('City Hall Park', ('Gray', 'Cinnamon', 'Eating', 'Approaches')),
 ('J. Hood Wright Park', ('Gray', 'White', 'Running', 'Indifferent')),
 ('Seward Park', ('Gray', 'Cinnamon', 'Eating', 'Indifferent')),
 ('Union Square Park', ('Gray', 'Black', 'Climbing', None)),
 ('Tompkins Square Park', ('Gray', 'Gray', 'Lounging', 'Approaches'))]


# to create an empty dictionary
squirrels_by_park = {}

# to loop over the squirrels list and unpack each tuple
for park, squirrels_details in squirrels:
    # to add each squirrel_details to the squirrels_by_park dictionary 
    squirrels_by_park[park] = squirrels_details
    
# to sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # to print each park and its value in squirrels_by_park
    print(f'{park}: {squirrels_by_park[park]}')

### <script.py> output:
    City Hall Park: ('Gray', 'Cinnamon', 'Eating', 'Approaches')
    Highbridge Park: ('Gray', 'Cinnamon', 'Running, Eating', 'Runs From, watches us in short tree')
    J. Hood Wright Park: ('Gray', 'White', 'Running', 'Indifferent')
    Madison Square Park: ('Gray', None, 'Foraging', 'Indifferent')
    Marcus Garvey Park: ('Black', 'Cinnamon', 'Cleaning', None)
    Seward Park: ('Gray', 'Cinnamon', 'Eating', 'Indifferent')
    Tompkins Square Park: ('Gray', 'Gray', 'Lounging', 'Approaches')
    Union Square Park: ('Gray', 'Black', 'Climbing', None)






# to safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get('Union Square Park'))

# to safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get('Fort Tryon Park')))

# to safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get('Central Park', 'Not Found'))


### output:
('Gray', 'Black', 'Climbing', None)
<class 'NoneType'>
Not Found



