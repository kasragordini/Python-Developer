# Our list of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# conditional list comprehension
new_fellowship = [member for member in fellowship if len(member)>=7]

print(new_fellowship)

