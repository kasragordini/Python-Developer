# we loop over top_ten_girl_names and unpack each tuple into top_ten_rank and name
for top_ten_rank, name in top_ten_girl_names:
  	# so we print each name in the proper format
    print(f"Rank #: {top_ten_rank} - { name }")

### output:
# 
Rank #: 1 - Jada
Rank #: 2 - Emily
Rank #: 3 - Ava
Rank #: 4 - Serenity
Rank #: 5 - Claire
Rank #: 6 - Sophia
Rank #: 7 - Sarah
Rank #: 8 - Ashley
Rank #: 9 - Chaya
Rank #: 10 - Abigail


# preamble
preamble = "The top ten boy names are: "

# , and as conjunction
conjunction = ", and"

# We combine the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[0:9])

# We print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.

### output:
# The top ten boy names are: Josiah, Ethan, David, Jayden, Mason, Ryan, Christian, Isaiah, Jayden, and Michael.


# to store a list of girl_names that start with s
names_with_s = [name for name in girl_names if name.lower().startswith('s')]

print(names_with_s)

# to store a list of girl_names that contain angel
names_with_angel = [name for name in girl_names if 'angel' in name.lower()]

print(names_with_angel)

### output
# 
['Serenity', 'Sophia', 'Sarah', 'Sophia', 'Savannah', 'Serenity']
['Angela']


