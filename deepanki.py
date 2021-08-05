from connection import Connection
import argparse


# Create instance of Connection class which handles
# connections to DeepL and Anki
cn = Connection()
# Create a parser object
ap = argparse.ArgumentParser()

# Define the arguments passed to the parser object
ap.add_argument(
                '--input', '--in',
                type=str,
                help='''Paste or type your input text for translation,
                which will become your card Front''')
ap.add_argument(
                '--target_lang', '--tl',
                type=str,
                help='Type the target language for the translation')
ap.add_argument(
                '--deck', '--dk',
                type=str,
                help='Type the target deck name for the new card')

# Interpret the arguments and return objects
args = ap.parse_args()

# Sends post request to DeepL API based on objects returned by parser
# and prints result of translation
translation = cn.translate(args.input, args.target_lang)
print('Success! Translation: ' + translation)

# Sends post request to AnkiConnect API based on objects returned by parser
# and translation and prints confirmation or error (see connection.py)
result = cn.invoke(action='addNote', note={
            'deckName': args.deck,
            'modelName': 'Basic',
            'fields': {
                'Front': args.input,
                'Back': translation,
            },
            'options': {
                'closeAfterAdding': True,
            }
            })

print('Success! Note ID: ' + format(result) + ' added')
