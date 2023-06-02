def morse_to_alphabet(morse_code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z'
    }

    words = morse_code.split(' / ')
    translated_text = ''

    for word in words:
        letters = word.split(' ')
        translated_word = ''

        for letter in letters:
            if letter in morse_dict:
                translated_word += morse_dict[letter]

        translated_text += translated_word + ' '

    return translated_text.strip()


morse_code = '.... . .-.. .-.. ---'
translated_text = morse_to_alphabet(morse_code)
print(translated_text)
