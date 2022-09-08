# FOREIGN LANGUAGE FLASH CARDS  

A simple foreign language flash card program created with PyCharm.

(https://github.com/ygyzys83/Foreign-Language-Flash-Cards/blob/main/ref/Flash_Card_Front.PNG)
(https://github.com/ygyzys83/Foreign-Language-Flash-Cards/blob/main/ref/Flash_Card_Back.PNG)

## Description

Load a dictionary of words from a foreign language to learn. Save the words that have not been learned into a new dictionary which loads the next time the program is run.

## Getting Started

### Installing

* Download the zip and unpack.
* Open the project in your Python IDE.

### Executing the program

* Before running the program, create a new .csv of words to learn using the same structure as french_words.csv found in the data folder.
* Save the new .csv file in the data folder.
* Replace `data/french_words.csv` in line 17 of `main.py` with the new .csv file name e.g. `data/spanish_words.csv`
* Run the program. Click the green check mark ✅ if you know the word. Click the red ❌ if you don't know the word. 
* All words that are ❌'d will be saved to a new .csv file called "words_to_learn.csv" within the data folder. 
* Each successive time the program is run, the "words_to_learn.csv" file will automatically load first.

## Authors

* Godman Tan
  * gtprogramming1@gmail.com
