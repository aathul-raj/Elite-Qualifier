from spellchecker import SpellChecker

text = input("INPUT TEXT: " )
spell = SpellChecker()
words = spell.split_words(text)
final = ''
for word in words:
  final += spell.correction(word)
  final += ' '
print(final)