"""
main.py: První projekt do Engeto Online Python Akademie, start January 23, 2025

author:Richard Ryzí
email: ryzi.richard@gmail.com
"""


# Projekt 1 - Datový analytik s Pythonem 23-1-2025
# Texts to analyze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Already registered users
users = {
    "Bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

break_line = ("-" * 45)

username = input("Enter user name: ").lower()
password = input("Enter your password: ")

print (break_line)

#  Dictionary comprehension - new dict created on iteration through current dict
users = {key.lower(): value for key, value in users.items()}
"""  above line equals:
old_users = users.copy()
for key, value in old_users.items():
    users[key.lower()] = value
    if key != key.lower():  # Pokud se klíč změnil
        del users[key] 
"""

if username not in users:
    print(f"Unregistered user, terminating the program... Bye.")
    exit()

if users[username] != password:
    print("Incorrect password, terminating the program... Bye.")
    exit()

if username in users and users[username] == password:
    print(f"Welcome to the app, {username.upper()}!")
    print(f"We have {len(TEXTS)} texts to be analyzed.")

    print (break_line)

    for index, t in enumerate(TEXTS, start=1):
        print(f"{index}.Text:\n{t}\n")
    
    print (break_line)

    input_text = (input("Enter a number btw. 1 and 3 to select: "))

    print (break_line)

    if not input_text.strip().isdigit():
        print("You didnt enter a number, terminating the program, bye.")
        exit()
    
    number = int(input_text.strip())

     # if number not in ["1", "2", "3"]: nasledujici je lepsi zapis
    if number < 1 or number > len(TEXTS):
        print(f"Wrong Text number: {input_text}, terminating the program, bye.")
        exit()
      
    if 1 <= number <= len(TEXTS):
            selected_text = TEXTS[number - 1]
            #  print(selected_text)

    # modifying the string to form one line and splitting to single words   
    words = selected_text.replace('\n', ' ').split()

    total_words = 0
    title_words = 0
    upper_words = 0
    lower_words = 0
    numbers = 0
    sum_numbers = 0
    word_lengths = {}

    # iteration through words and counting
    for word in words:
        # removing , and -
        clean_word = ""
        for char in word:
            if char.isalnum(): 
                clean_word += char
    
        # skip if empty
        if not clean_word:
            continue
        
        total_words += 1
    
        if clean_word.isdigit():
            numbers += 1
            sum_numbers += int(clean_word)       
        else:
            if clean_word.isupper(): 
                upper_words += 1
            elif clean_word[0].isupper() and clean_word[1:].islower():  
                title_words += 1
            elif clean_word.islower(): 
                lower_words += 1

        word_len = len(clean_word)
        if word_len in word_lengths:
            word_lengths[word_len] = word_lengths[word_len] + 1
        else:
            word_lengths[word_len] = 1

    # Print results
    print(f"There are {total_words} words in the selected text.")
    print(f"There are {title_words} titlecase words.")
    print(f"There are {upper_words} uppercase words.")
    print(f"There are {lower_words} lowercase words.")
    print(f"There are {numbers} numeric strings.")
    print(f"The sum of all the numbers {sum_numbers} " )

    print (break_line)
    print("LEN|  OCCURENCES  |NR.")
    print (break_line)
    
    # Sorted length list - ASC
    """
    lengths_list = []
    for key in word_lengths:
        lengths_list.append(key)
    sorted_lengths = sorted(lengths_list)
    """
    sorted_lengths = sorted(word_lengths.keys())

    # simple bar chart
    """
    for length in sorted_lengths:
      occurrences = word_lengths[length]
      stars = "*" * occurrences
      print(str(length).rjust(2) + "|" + stars.ljust(18) + "|" + str(occurrences))
    """
    # following bar chart is flexible
    max_occurrences = max(word_lengths.values())
    for length, occurrences in sorted(word_lengths.items()):
        print(f"{length:2} | {'*' * occurrences:<{max_occurrences}} | {occurrences}")
         # :<{max_occurrences} zarovná hvězdičky doleva na šířku největšího počtu výskytů.
         # > zarovnání doprava.
         # ^ zarovnání na střed.