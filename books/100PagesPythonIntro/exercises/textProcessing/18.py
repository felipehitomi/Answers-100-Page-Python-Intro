import string

def words(phrase):
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation)) #map punctuation to space
    splited = phrase.translate(translator).split()
    print(splited)



words('"Hi", there! How *are* you? All fine here.')
#['Hi', 'there', 'How', 'are', 'you', 'All', 'fine', 'here']
words('This-Is-A:Colon:Separated,Phrase')
#['This', 'Is', 'A', 'Colon', 'Separated', 'Phrase']
