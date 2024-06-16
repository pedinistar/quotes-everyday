import random
from datetime import datetime

# List of quotes
quotes = [
    "The early bird catches the worm.",
    "Every morning is a new beginning.",
    "The sun is new each day.",
    "The morning is a great opportunity to see life in a new way.",
    "With the new day comes new strength and new thoughts.",
    "Every sunrise is an invitation for us to arise and brighten someone's day."
]

# Function to print a random quote
def print_quote():
    quote = random.choice(quotes)
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Quote of the Day: {quote}")

# Call the function
print_quote()
