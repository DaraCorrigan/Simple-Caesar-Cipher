import string

plain_text = "Hello!"
shift = 7

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]