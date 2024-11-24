---

# Concept of Programming Languages - Task Solutions

Welcome to the repository for the Concept of Programming Languages course assignment! This project contains solutions to three Python programming tasks designed to apply key concepts and problem-solving skills. Below, you'll find the descriptions of each task, the implemented solutions, and the resources used during development.

---

## *Task Descriptions and Solutions*

### 1. Daily Steps Tracker
*Description*: Analyze daily step counts for a month.  
*Program Features*:  
- Accepts daily step counts as input (space-separated).  
- Determines the highest and lowest step counts.  
- Calculates the average daily step count.  
- Sorts the step counts in descending order.  

*How I Wrote the Code*:  
1. *Input Handling*: I used the input() function to take the user's daily step counts as a single line of input, then split the input into a list of integers using the split() and map() functions.  
2. *Calculations*: Leveraged Python's built-in functions like max() and min() for finding the highest and lowest step counts, and used sum() with len() for calculating the average.  
3. *Sorting*: Utilized Python's sorted() function with the reverse=True parameter to sort the step counts in descending order.  

---

### 2. Library Book Borrowing Analysis
*Description*: Analyze library book borrowing records.  
*Program Features*:  
- Accepts borrowing records in the format "Book Title - Days Borrowed".  
- Determines the most and least borrowed books based on days borrowed.  
- Calculates the average borrowing duration.  
- Identifies unique book titles using a set.  
- Sorts books by the number of days borrowed in descending order.  

*How I Wrote the Code*:  
1. *Input Parsing*: I split the input into lines, processed each line by separating the book title and days borrowed using the split(" - ") method.  
2. *Data Storage*: Created a dictionary to store book titles as keys and their total borrowed days as values.  
3. *Set Usage*: Used a set to collect unique book titles for easy identification of distinct entries.  
4. *Calculations*: Found the most and least borrowed books using max() and min() on the dictionary values. The average was calculated by dividing the sum of all borrowed days by the total number of books.  
5. *Sorting*: Sorted the dictionary by its values in descending order using a lambda function with sorted().  

---

### 3. Word Scramble Game
*Description*: A fun word guessing game with scrambled words.  
*Program Features*:  
- Randomly selects and scrambles a word from a predefined list.  
- Allows the player 5 attempts to guess the original word.  
- Provides feedback after each guess.  
- Congratulates the player upon a correct guess or reveals the word after 5 failed attempts.  
- Handles invalid inputs gracefully.  

*How I Wrote the Code*:  
1. *Word Selection*: Used the random.choice() function to select a random word from a predefined list of words.  
2. *Scrambling*: Used random.sample() to shuffle the characters of the word into a scrambled version.  
3. *Game Logic*: Implemented a loop to track the player's attempts and compare their guesses with the original word.  
4. *Feedback*: Displayed the number of attempts left after each incorrect guess, and provided congratulatory or failure messages at the end.  
5. *Error Handling*: Used if conditions to check for empty inputs and ensure the game continued without crashing.  

---

## *Usage*

1. Clone this repository:  
   bash
   git clone https://github.com/NADER2005/Concept_task.git
   cd Concept_task
   

2. Run the Python scripts for each task:  
   - *Daily Steps Tracker*: python steps_tracker.py  
   - *Library Book Borrowing Analysis*: python book_analysis.py  
   - *Word Scramble Game*: python word_scramble.py  

---

## *Development Approach*  

- *Problem Understanding*: Started by carefully reading and breaking down the problem statements into smaller tasks.  
- *Planning*: Designed a step-by-step solution plan for each problem before writing code.  
- *Implementation*: Wrote the code iteratively, testing each feature individually before integrating them into the full program.  
- *Testing*: Tested the code with various inputs to ensure all edge cases were handled.  
- *Refinement*: Improved code readability and structure by adding comments and ensuring proper variable naming.  

---

## *Resources*

The following resources were used to solve these problems:  
- [GeeksforGeeks](https://www.geeksforgeeks.org/)  
- [Copilot](https://copilot.github.com/)  
- [w3Schools](https://www.w3schools.com/)  

---

## *License*

This project is open-source and available under the MIT License. Feel free to use and modify the code as needed.  

---
