Morse_code =  {
                'A': '.-',          'B': '-...',        'C': '-.-.',        'D': '-..',         'E': '.',           'F': '..-.', 
                'G': '--.',         'H': '....',        'I': '..',          'J': '.---',        'K': '-.-',         'L': '.-..', 
                'M': '--',          'N': '-.',          'O': '---',         'P': '.--.',        'Q': '--.-',        'R': '.-.', 
                'S': '...',         'T': '-',           'U': '..-',         'V': '...-',        'W': '.--',         'X': '-..-', 
                'Y': '-.--',        'Z': '--..',


    '0': '-----',       '1': '.----',       '2': '..---',       '3': '...--',       '4': '....-', 
    '5': '.....',       '6': '-....',       '7': '--...',       '8': '---..',       '9': '----.',
                                            
                                             ' ': '/'
    }

# print(Morse_code)

def text_to_morse(text):
    morse_code = ' '
    for char in text.upper():
        if char in Morse_code:
            morse_code += Morse_code[char] + ' '
    return morse_code

name = input("Enter your name: ")

print("Morse Code:", text_to_morse(name))


output:
Enter your name: Naresh
Morse Code:  -. .- .-. . ... .... 
