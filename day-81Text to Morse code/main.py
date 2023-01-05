
''' Dictionary for morse code encoding'''
morse_dict = {

    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '· − − − − ·',
    '!': '− · − · − −',
    '/': '− · · − ·',
    '(': '− · − − ·',
    ')': '− · − − · −',
    '&': '· − · · ·',
    ':': '− − − · · ·',
    ';': '− · − · − ·',
    '=': '− · · · −',
    '+': '· − · − ·',
    '-': '− · · · · −',
    '_': '· · − − · −',
    '"': '· − · · − ·',
    '$': '· · · − · · −',
    '@': '· − − · − ·',
}

process = True


def translate(user_input):
    encoded = ' '
    print(user_input)
    for char in user_input:
        if char == ' ':
            encoded += ' '
        elif char != ' ':
            encoded += morse_dict[char.upper()] + ' '
    return encoded


while process is True:
    print("Welcome to the text to morse code converter.")
    user_input = input("Enter the text you want to convert to morse code: ")
    print("The morse code for the text you entered is: ")
    print(translate(user_input))
    print("Do you want to convert another text to morse code?")
    user_input = input("Enter Y for yes and N for no: ")
    if user_input == 'Y':
        process = True
    else:
        process = False
        print("Thank you for using the text to morse code converter.")
