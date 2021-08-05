# deepanki

## Description
This is a Python script to translate text and add a new card to Anki with the translation, using the [DeepL API](https://www.deepl.com/docs-api) and [AnkiConnect](https://github.com/FooSoft/anki-connect).

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