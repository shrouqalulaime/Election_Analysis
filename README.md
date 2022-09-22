# Election_Analysis

## Overview of the Election Audit
This project aims to assist in an election audit of the tabulated results for a U.S. congressional precinct in Colorado. The tasks include reporting the following results:

1. The total number of votes cast.
2. The total number of votes for each candidate and county.
3. The percentage of votes for each candidate and county.
4. The election's winner based on the popular vote.
5. The county with the largest voter turnout.

## Election-Audit Results
The analysis of the election show that:
1. There were 369,711 votes cast in the election.
2. Breakdown the total votes by county:
   - Jefferson turnedout 10.5% of the vote and 38,855 number of votes
   - Denver turnedout 82.8% of the vote and 306,055 number of votes
   - Arapahoe turnedout 6.7% of the vote and 24,801 number of votes
3. The county that had the largest number of votes is Denver.
4. Breakdown the total votes by candidate:
   - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes. 
   - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
   - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
5. The winner of the election was:
   - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Election-Audit Summary
This project provides a script to automate election results analysis To define the winner based on the popular vote. It can be used to solve similar problems with minor changes, such as:
1. Change the file_to_load path based on the file name that the user wants to check
2. If an election is performed on a state level, the user can change the row[1] to refer to the column of interest, for example, country, state, etc. 
