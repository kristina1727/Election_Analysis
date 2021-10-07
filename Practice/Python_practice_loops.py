#while loop (youTube)
i = 1
while i <= 5:
    print (i)
    i =i+1
print("Done")

i = 1
while i <= 5:
    print ('*'*i)
    i =i+1
print("Done")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit: 
    guess = int(input('Guess: '))
    guess_count +=1
    if guess==secret_number:
        print('You won!')
        break
else:
    print("Sorry you failed")

#For Loops (youTube)

for item in 'python':
    print(item)

for item in['Mosh', 'John', 'Sarah']:
    print(item)

for item in range (10):
    print(item)

for item in range (5,10):
    print(item)

for item in range (5,10, 2):
    print(item)

prices = [10, 20, 30]
total = 0

for price in prices:
    total = total + price
print (f"Total: {total}")

# While Loops (Course)

x = 0
while x <=5:
    print(x)
    x = x+1

count = 7
while count < 1:
    print("hello world")

# For loop (Course)

#List 
counties = ["Arapahoe" , "Denver", "Jefferson"]
for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#Range
numbers = [0, 1, 2, 3, 4]
for num in range(5):
    print(num)

counties = ["Arapahoe" , "Denver", "Jefferson"]
for i in range(len(counties)):
    print (counties [i])

#Tuple
counties_tuple =("Arapahoe","Denver", "Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

counties_tuple =("Arapahoe","Denver", "Jefferson")
for county in counties_tuple:
    print(county)

#Dictionary
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print (county)

counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print (county)
   
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict.values():
    print (county)

counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print (counties_dict[county])

#get key and values
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print (county, voters)




# print msg with kesy and values
counties_dict = {"Arapahoe": 422829,"Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print (str(county) + " " + "county has " + str(voters) +" " + "registered voters.")

#Dictionary in a Dictionary for loop

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438},]
for county_dict in voting_data:
    print(county_dict)

#Using a range to iterate over the list
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438},]
for i in range(len(voting_data)):
      print(voting_data[i])

#Nested loop 

#pulling values only
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 46335},
                {"county": "Jefferson", "registered_voters": 432438},]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


#NOT WOKING - PRINTING SAME VALUE 3 TIMES
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438},]
for county_dict in voting_data:
    print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])