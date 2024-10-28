import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Get the first word from the returned list
        word = response.json()[0]
        return word
    else:
        return "Error fetching word"

def display_word(word):
    width = 50  # Width of the display
    centered_word = word.center(width)
    print("\n" + centered_word + "\n")

# Get a random word and display it
word_of_the_day = get_random_word()
display_word(word_of_the_day)
