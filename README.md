# Project-8---Caesar-Cipher

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to encrypt and decrypt messages using the Caesar Cipher technique.

**Project Overview**

This project is a command-line implementation of the classic Caesar Cipher.

The user can:

Choose to encode or decode a message

Enter a custom message

Specify a shift number

The program then:

Shifts each letter in the alphabet by the given amount

Wraps around the alphabet when needed

Preserves non-alphabet characters

Allows the user to repeat the process multiple times

**Project File Structure**

The project is split into multiple files for clarity and reuse.

main.py
Contains the main program loop and Caesar Cipher logic.

art.py
Stores the ASCII art logo displayed at program start.

**Why this project exists**

This project represents my first implementation of a real-world encryption algorithm.

It helped me:

Understand how character shifting works

Translate mathematical logic into code

Structure logic using functions

Combine loops, conditionals, and user input

**What I learned**

How to define and call functions

How to pass arguments into functions

How to use lists and indexes to shift characters

How to handle wrapping using modulo (%)

How to keep programs running using while loops

How to preserve non-alphabet characters in transformations

**How the code works (step-by-step)**

Display the program logo

Ask the user whether to encode or decode

Take a message and shift number as input

Reverse the shift when decoding

Loop through each character in the message

Shift letters while leaving other characters unchanged

Display the transformed message

Repeat until the user exits

**Example Output**

Type 'encode' to encrypt, type decode to decrypt:

encode

Type your message:

hello world

Type the shift number:

5

Here is your encoded result: mjqqt btwqi
