#f string with dictionary
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    #original
    print (county + " county has " + str(voters)  + " registered voters.")
    #f string
    print(f"{county} county has {voters} registered voters.")

# multiline f strings

# Calculate the percentage of votes you received.

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {my_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {my_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Formatting the decimals and numbers
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

# f string dictionary
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters. " )

# f string list dictionary 
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438},]
for county_dict in voting_data:
    print(f"{county ['county']} county has {voters['registered_voters']:,} registered voters.")
