print("Welcome to the Mad Libs Game!")
print("Please fill in the blanks with the requested types of words.")

noun1 = input("Enter a noun (e.g., dog): ")
adjective1 = input("Enter an adjective (e.g., funny): ")
verb1 = input("Enter a verb (e.g., jump): ")
noun2 = input("Enter another noun (e.g., car): ")
place1 = input("Enter a place (e.g., park): ")
adjective2 = input("Enter another adjective (e.g., blue): ")
verb2 = input("Enter another verb (e.g., run): ")
number = input("Enter a number: ")

story = f"""
Once upon a time, a {adjective1} {noun1} decided to {verb1} all the way to the {place1}.
On the way, it encountered a {adjective2} {noun2} that was {verb2} around in circles. 
The {noun1} was so amazed that it immediately joined in the fun.
They both {verb1} and {verb2} until they reached {number} miles from home!
It was the most {adjective1} adventure of their lives!
"""

print("\nHere is your Mad Libs story:")
print(story)
