# deepanki

## Description
This is a Python script to translate text and add a new card to Anki with the translation, using the [DeepL API](https://www.deepl.com/docs-api) and [AnkiConnect](https://github.com/FooSoft/anki-connect).

I created this script as I watch YouTube or Twitch in my language of study (Finnish) for immersion and regularly come across more colloquial words or phrases. DeepL translation has proved far more capable than Google, particularly for Finnish. I considered a GUI or Anki addon but found a simple command line tool was quickest, allowing translation and adding to a new Anki card without having to change tabs or open windows (beyond terminal).

## Installation
* Install Python 3
* Clone this repo
* Install using either:
    * Install from requirements (```pip install -r requirements.txt```)
    * Install with pipenv (```pipenv install```)
* Install [AnkiConnect](https://github.com/FooSoft/anki-connect) and have Anki open
* Sign up for a **free** DeepL Pro account (up to 500,000 characters a month translated)
* Copy your Authentication Key for DeepL API from the [account page](https://www.deepl.com/pro-account)
* Open *.env.example* and paste your key after the '=' (```AUTH_KEY=YOUR_DEEPL_API_AUTH_KEY```)
* Rename *.env.example* to **.env**, save and close file

## Usage
Several examples are shown below.

* The standard arguments
```
.\deepanki.py --input Paljonko --target_lang EN-GB --deck test1
```
* The input argument can accept sentences as long as they are enclosed in single or double quotes. Single words do not require this, as above
```
.\deepanki.py --input 'Paljonko se maksaa' --target_lang EN-GB --deck test1
```
* Once familiar with the script, shorthand versions of the argument exist to speed things up
```
.\deepanki.py --in Paljonko --tl EN-GB --dk test1
```
* After pressing enter, the script will print two lines; the first upon successful translation with DeepL, the second the ID of the new card
```
Success! Translation: How much does it cost
Success! Note ID: 1628179552022 added
```

## Recommendations
* The addon (Minimize to tray)[https://ankiweb.net/shared/info/85158043] is useful to keep Anki open but out of the way. The script will create a new card with AnkiConnect and does not require any input from the main Anki program
* If you intend to only use one deck, you can easily remove or comment out this argument like so:
```
# ap.add_argument(
                '--deck', '--dk',
                type=str,
                help='Type the target deck name for the new card')
```
And input your target deck in single or double quotations here:
```
result = cn.invoke(action='addNote', note={
            'deckName': 'your_target_deck',
```
* AnkiConnect has a large number of (actions)[https://github.com/FooSoft/anki-connect#card-actions] that could be added into this script if you are familiar with Python and have more complicated requirements for your cards than me. If you require Cloze cards rather than Basic cards, tags or want to open the 'Add card dialog' rather than do it automatically, these can all be added here:
```
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
```