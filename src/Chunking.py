# I initilized a dictionary to chunk a large tweet file
counts_dict = {}

# Iterate over the tweet file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize = 10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

print(counts_dict)
