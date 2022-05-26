"""
String concatenation project.

Suppose we want to create a string that says "Subscribe to *insert YouTuber*!" There are many methods:

youtuber = "freeCodeCamp.org"

1. print("Subscribe to " + youtuber + "!")
2. print("Subscribe to {}!".format(youtuber))
3. print(f"Subscribe to {youtuber}!")

The third method uses an f-string. I will use f-strings in this project.
"""

# user input
adj1 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
college = input("College: ")

# madlib
madlib = (f"Computer programming is so {adj1}! It makes me so excited because I love to {verb1} and {verb2}! I am glad that I have a degree in computer science from {college}!")

# print the madlib with the user input
print(madlib)
