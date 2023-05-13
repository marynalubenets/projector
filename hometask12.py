# 1 Task 1

from string import ascii_uppercase          # import for working with A to Z file names
from random import *
for letter in ascii_uppercase:
    file_group = open(letter + '.txt', 'w')  # creating files with A to Z names   
    rand_int = str(randint(1, 100))          # creating random variable
    file_group.write(rand_int)               # write random variable to each file
    file_group.close()  

with open('summary.txt', 'w') as file:
    for letter in ascii_uppercase:               # loop for reading file names 
        file_group = open(letter + '.txt', 'r')
        file_data  = file_group.read()        # reading data from each file 
        file.write(f'{letter}.txt: {file_data}' + '\n')  # write file name with file data in 'summary.txt' file

# Task 2

with open('original.txt','w') as firstfile:      # writing an original file
    firstfile.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum\n')    
with open('original.txt','r') as firstfile, open('copy.txt','a') as secondfile:  # opening original file for reading and copied file for writing
    for line in firstfile: 
        secondfile.write(line.upper())          # writing uppercased text from original file to copy

# Task 3

import random
import csv

players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
with open('scores.csv', 'w') as scores_file:
    csv_writer = csv.DictWriter(scores_file, fieldnames=['Player', 'Score']) # create a header in file
    csv_writer.writeheader()

    for i in range(100):                       # simulate 100 games for each player
        for player in players:
            score = random.randint(0, 1000)    # simulate random scores for each player for each game 
            current_dict = {                   # writing results to a dictionary 'player: score'
                'Score': score
            }
            csv_writer.writerow(current_dict)

# Task 4

with open('scores.csv', 'r') as scores_file, open('high_scores.csv', 'w') as highscores_file:
    csv_writer = csv.DictWriter(highscores_file, fieldnames=['name', 'score']) # create a header in highscores_file
    csv_writer.writeheader()
    high_score_list = []
    reader = csv.DictReader(scores_file)
    for row in reader:                   # loop through all rows in csv files
        current_player = {               # creating dict with values from current row to compare it later
            'name': row['Player'],
            'score': row['Score']
        }
        if len(high_score_list) > 0:     # checking if highscore list already has items in it
            for existing_player in high_score_list:                         # comparing existing values with current dict
                print(existing_player['name'], current_player['name'])
                if existing_player['name'] == current_player['name']:
                    if int(existing_player['score']) < int(current_player['score']):
                        existing_player['score'] = current_player['score']
                    break                                 # exit the loop if same player found 
            else:                                           
                high_score_list.append(current_player)    # adding current dict when the loop is over 
        else:   
            high_score_list.append(current_player)        # adding the first item to the list
    for player in high_score_list:
        csv_writer.writerow(player)
   


