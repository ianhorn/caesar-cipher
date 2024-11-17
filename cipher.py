# Caeser Cipher with right shift 5

# create input
letters = input("Please enter a sentence: ")
letter_shift = 5
encryption = ""

# for loop:
for letter in letters:
    if letter.isalpha():
        new_letter = ord(letter) + letter_shift
        if new_letter > 90 and new_letter < 97:         # account for upper case
            new_letter -= 26                                # loop to beginning of alpha
        elif new_letter > 122:                          # account for lower case
            new_letter -= 26                                # loop to beginning of alpha
        else:
            new_letter = new_letter 

        # encrpyt character
        encrypt_letter = chr(new_letter)
        # append new letter to encryption
        encryption += encrypt_letter

    # account for special character
    else:
        encryption += letter

print(f'Message encryption: {encryption}')     