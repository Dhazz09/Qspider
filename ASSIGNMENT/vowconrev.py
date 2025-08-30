#  Vowel-Consonant-Middle Check with Reversal (Nested elif edition)

text = input("Enter a string to check and reverse: ")
text_lower = text.lower()
if len(text_lower) > 0:
    first_char = text_lower[0]
    last_char = text_lower[-1]
    if first_char in 'aeiou':
        if last_char.isalpha() and last_char not in 'aeiou':
            if len(text_lower) % 2 != 0:
                reversed_text = text[::-1]
                print(f" Conditions met! Reversed string: {reversed_text}")
            elif len(text_lower) % 2 == 0:
                print("No middle character (even length). Skipping reversal.")
            else:
                print(" Unexpected length issue.")
        elif not last_char.isalpha():
            print("Last character is not a letter.")
        else:
            print("Last character is a vowel. Need a consonant.")
    elif first_char not in 'aeiou':
        print(" First character is not a vowel.")
    else:
        print(" First character is invalid.")
else:

    print(" Empty string. Nothing to check.")