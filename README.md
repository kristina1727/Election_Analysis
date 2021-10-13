# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Calculate the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest turnout.
3. Get a complete list of candidates who received votes.
4. Calculate the total number of votes each candidate received.
5. calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code 

## Audit Results
The analysis of the election showed that:
- There were 369,711 votes cast in the election.

- The county results were:
    - Jefferson county accounted for 10.5% of the vote with 38,855 total votes cast.
    - Denver county accounted for 82.8% of the vote with 306,055 total votes cast.
    - Arapahoe count accounted for 6.7% of the vote with 24,801 total votes cast.
    
- The county with the largest number of votes was:
    - Denver county, which had 8.28% of the vote turnout and 306,055 votes cast.
    
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
    - Diana DeGette received 73.8% of the vote and 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.

- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 total votes.
 
## Summary
If the dataset contained additional fields such as; voter city, voter district, candidate party, candidate status (incumbent), and position running for this script could be modified to look at different breakouts of the data and provide a more insightful look into the elections. Outlined below are a few recommendations for additional outcomes that could be measured and how we could modify the script appropriately.

- What percentage of the total votes were cast for each party?
    - We would want to create initiate a variable for each political party and create both a list and dictionary. From there we would create the appropriate for loops to track the votes for each political party and an if statement to track the votes and append the lists and dictionaries. Then print the terminal and write to our txt file.
    
- Breakdown the number of votes and percentage of votes for each city and district.
    - To get this breakout we would copy and modify the script used to get the county breakdown. Ensuring that we create the appropriate lists and dictionaries for both city and district. And modify or if statements and for loops appropriately. Then we would also need to modify the script to print the results to the terminal and print to the txt file.
