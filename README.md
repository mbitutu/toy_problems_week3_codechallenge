# Toy Problems Week 3 Code Challenges

This repository contains solutions to the code challenges for Week 3 of the Toy Problems phase. The challenges include tasks related to converting time formats, evaluating positive numbers, and calculating consonant values in a string.

## Challenge 1: Converting 12-hour time to 24-hour time

The `convert_to_24_hour` function takes an hour (in the range of 1 to 12), a minute (in the range of 0 to 59), and a period ("am" or "pm") as input and returns the time in 24-hour format.

## Challenge 2: Two numbers are positive

The `two_positive` function takes three integers as input and returns True if exactly two of the three numbers are positive, otherwise False.

## Challenge 3: Consonant value

The `solve` function takes a lowercase string with alphabetic characters and calculates the highest value of consonant substrings. Consonants are any letters except "aeiou", and their values are assigned from a = 1 to z = 26.

## How to Use

1. Clone this repository to your local machine.
      
   git clone <>

2. Ensure you have Python 3 installed.

3. Navigate to the repository's directory in your terminal.

4. To test each challenge, create a separate Python script (e.g., `test_convert_to_24_hour.py`, `test_two_positive.py`, `test_solve.py`) that imports the respective function from `solution.py`, calls the function with specific arguments, and prints the result.

   ```python
   from solution import convert_to_24_hour

   hour = 8
   minute = 30
   period = "am"
   result = convert_to_24_hour(hour, minute, period)
   print(result)
   
1. Run the test scripts using the python3 command:

    python3 test_convert_to_24_hour.py

2. View the output in the terminal to see the results of the challenges.

Repository Structure

    solution.py: Contains the solutions to the code challenges.
    test_convert_to_24_hour.py, test_two_positive.py, test_solve.py: Test scripts for each challenge.

