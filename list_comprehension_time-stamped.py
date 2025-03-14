# We extracted the created_at column from df
tweet_time = pd.read_csv("tweets.csv")["created_at"]

# Extract the clock time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == "19"]

print(tweet_clock_time)

# Output

#   GNU nano 8.3           list_comprehension_time-stamped.py           Modified
# We extracted the created_at column from df
tweet_time = pd.read_csv("tweets.csv")["created_at"]

# Extract the clock time
tweet_clock_time = [entry[11:19] for entry in tweet_time if entry[17:19] == "19>

print(tweet_clock_time)

# Output
# ['23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19', '23:40:19']

