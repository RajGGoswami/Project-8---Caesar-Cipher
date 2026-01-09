# Day 8 – Caesar Cipher
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Understanding how encryption and decryption work conceptually
# - Using functions to encapsulate logic
# - Passing parameters into functions
# - Using while loops to allow repeated program execution
# - Working with lists and indexes to shift characters
# - Handling non-alphabet characters gracefully
#
# This project represents my first experience implementing
# a real-world algorithm (Caesar Cipher) in Python.

from art import logo

# Ceaser Cipher
print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

program_on = True

while program_on:

    # Ask user whether to encode or decode
    direction = input("Type 'encode' to encrypt, type decode to decrypt:\n").lower()

    # Get message and shift amount
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Caesar cipher function
    def caesar(encode_or_decode, original_text, shift_amount):
        cipher_text = ""

        # Reverse shift for decoding
        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            # Leave non-alphabet characters unchanged
            if letter not in alphabet:
                cipher_text += letter
            else:
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                cipher_text += alphabet[shift_position]

        print(f"Here is your {encode_or_decode}d result: {cipher_text}")

    # Run cipher
    caesar(direction, text, shift)

    # Ask user if they want to continue
    continue_program = input(
        "Type 'yes' if you want to do it again. Otherwise type 'no'\n"
    ).lower()

    if continue_program == "no":
        program_on = False
        print("Goodbye!")
