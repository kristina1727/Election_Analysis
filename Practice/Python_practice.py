print("Hello World")
 
counties = ["Arapahoe","Denver","Jefferson"]
counties.insert(1,"El Paso")
counties.remove("Arapahoe")
counties.insert(2,counties.pop(1))
counties.append("Arapahoe")
print(counties)

#creating a dictionary
counties_dict = {"Arapahoe" : 422829, "Denver": 463353, "Jefferson":432438}

#shows the dictionary
print(counties_dict["Arapahoe"])

print(len(counties_dict))

#gets list of tuples
print(counties_dict.items())

#gets list
print(counties_dict)

#gets only the keys in the dictionary
print(counties_dict.keys())

#gets only the values in the dictionary
print(counties_dict.values())

#gets the value for a specific key
print(counties_dict.get("Denver"))

#gets the value for a specific key
print(counties_dict["Arapahoe"])

#creating an empty list
voting_data = []

#appending the list dictionary

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

#get the length of the voting_data
print(len(voting_data))

#add in El Passo and its registered voters, 461149 into position 1 (index 0)
voting_data.insert(0,{ "county": "El Passo", "registered_voters": 461149})

print(voting_data)

#Remove Arapahoe from list 
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)

#Move Denver to the 3d item in the list

voting_data.insert(1,voting_data.pop(2))


#Add Arapahoe and its registered voters to list
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))

#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))

# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100

print("I received " + str(percentage_votes)+"% of the total votes.")

#If Statement
if counties[2] == 'Denver':
    print (counties[2])

 #If Else Statement
temperature = int(input("What is the temerature outside? "))

if temperature > 80:
        print("Turn on the AC.")
else:
    print("Open the windows")

#Nested if-else statement
#What is the score?
score=int(input("What is your test score? "))

#Determine the grade.
if score>=90:
    print('Your grade is an A.')
else:
    if score>=80:
        print('Your grade is a B.')
    else:
        if score >=70:
            print('Your grade is a C.')
        else:
            if score>=60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

#elif 
#What is the Score
score1 = int(input("What is your score? "))

#Determine the grade
if score1 >= 90:
    print('Your grade is an A.')
elif score1 >= 80:
   print ('Your grade is an B.')
elif score1 >=70:
    print ('Your grade is an C.')
elif score1 >=60:
    print ('Your grade is an D.')
else:
    print('Your grade is an F.')

#Membership Operation

counties1 = ["Arapahoe" , "Denver", "Jefferson"]

if "El Paso" in counties1:
    print("El Paso is in the list of countries.")
else:
    print("El Paso is not in the list of countries.")

if "Arapahole" in counties1 and "El Paso" in counties1:
    print("Arapahoe and El Paso are in the list of countries.")
else:
    print("Arapahoe or El Paso is not in the list of countries.") 


if "Arapahole" in counties1 or "El Paso" in counties1:
    print("Arapahoe or El Paso are in the list of countries.")
else:
    print("Arapahoe or El Paso is not in the list of countries.") 