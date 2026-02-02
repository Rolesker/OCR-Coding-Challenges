letter_to_morse={
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".--",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
    " ":"|",
    "":" "
}

def encode(s):
    output=""
    for i in s:
        output+=letter_to_morse[i]+" "
    print(output)

def decode(s):
    morse_to_letter=dict([(value, key) for key, value in letter_to_morse.items()])
    output=""
    letters=s.split()
    for i in letters:
        output+=morse_to_letter[i]
    print(output)

encode("SOS HELP")
decode("... --- ... | .... . .-.. .--.")
encode("I AM SENDING IN MORSE")
decode(".. | .- -- | ... . -. -.. .. -. --. | .. -. | -- --- .-. ... .")