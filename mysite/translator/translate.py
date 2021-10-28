from googletrans import Translator


def translate(text):
    translator = Translator()
    transilation = translator.translate(text=text, dest="ml").text
    return transilation
