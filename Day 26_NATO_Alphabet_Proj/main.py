import pandas as pd
import csv


#TODO 1. Create a dictionary in this format:

#reads csv  file
reader = csv.reader(open('nato_phonetic_alphabet.csv','r'))
#skips header of csv file
next(reader)

#create empty dictionary
d = {}
#create a dictionary by iterating through reader
for key,value in reader:
    #keys are created, but values are created through finding keys
    d[key] = value


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

program = True

words = str(input('Please enter a word you want to phoneticize \n').upper())
phonetic = list(words)
print(phonetic)

#what do i have now
# i have a dictionary of key value pairs of phonetic alphabet
# i have a list which chops up the words that are inputted
# i want to iterate through the words in this list and find the values for them

output = [d[value] for value in phonetic]
#goes through dictionary looking for a value from phonetic
print(output)