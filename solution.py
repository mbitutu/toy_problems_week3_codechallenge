def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minute:02d}"

def two_positive(a, b, c):
    positive_count = sum([num > 0 for num in [a, b, c]])
    return positive_count == 2

def solve(word):
    consonant_values = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10,
                         'k': 11, 'l': 12, 'm': 13, 'n': 14, 'p': 16, 'q': 17, 
                         'r': 18, 's': 19, 't': 20, 'v': 22, 'w': 23, 'x': 24, 
                         'y': 25, 'z': 26}
    
    max_value = 0
    current_value = 0
    
    for char in word:
        if char in consonant_values:
            current_value += consonant_values[char]
            if current_value > max_value:
                max_value = current_value
        else:
            current_value = 0
    
    return max_value

