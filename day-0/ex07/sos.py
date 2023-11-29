import sys


def dict_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morse_text = []
    for char in text.upper():
        if char in morse_dict:
            morse_text.append(morse_dict[char])
        else:
            raise AssertionError("Unsupported character: {}".format(char))
    return ' '.join(morse_text)


def main():
    """
    Morse Encoder

    This program encodes a given text message into Morse code.
    It takes a single command-line argument,
    which should be the text message to be encoded.

    Usage:
        python3.10 morse_encoder.py <text>

    Parameters:
        <text>: The text message to be encoded.

    The program uses a dictionary to map each character to
    its Morse code representation. Unsupported
       characters will raise an AssertionError.

    Example:
        python3.10 morse_encoder.py "Hello World"
        Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
    """
    try:
        if len(sys.argv) != 2 or len(sys.argv[1]) == 0 or not isinstance(
                sys.argv[1], str):
            raise AssertionError("Usage: python3.10 morse_encoder.py <text>")
        input_text = sys.argv[1]
        morse_result = dict_morse(input_text)
        print(morse_result)
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
