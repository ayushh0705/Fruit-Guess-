import random

# List of fruits as a string
someFruits = "apple, banana, avocado, pineapple, strawberry, grapes, mango"

# Randomly choose a fruit from the list
guessFruit = random.choice(someFruits.split())

if __name__ == "__main__":
   print("Guess a correct letter for the fruit")
   
   # Set to store guessed letters
   letterGuesses = set()

   # Chances for guessing the fruit
   chances = len(guessFruit) + 2

   # Loop until chances run out
   while chances > 0:
      # Display the current state of guessed and blank letters
      print(" ".join([char if char in letterGuesses else "_" for char in guessFruit]))

      # Get a letter input from the user
      guess = str(input("Guess a letter of a fruit"))

      # Validate the input
      if not guess.isalpha() or len(guess) != 1:
         print("Enter a single letter at a time")
         continue

      # Check if the letter has already been guessed
      if guess in letterGuesses:
         print("The letter is already guessed")
         continue

      # Add the guessed letter to the set
      letterGuesses.add(guess)
      
      # Check if all letters of the fruit have been guessed
      if set(guessFruit) <= letterGuesses:
         print(f"Congratulations! Guessed the fruit {guessFruit}")
         break

      # Decrease the remaining chances
      chances -= 1
   else:
      print(f"You lost! The word is {guessFruit}")
