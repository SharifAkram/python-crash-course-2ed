from textblob import Word


def check_word_spelling(word):
	"""Program to check spelling of a word."""
	word = Word(word)
	result = word.spellcheck()
	if word == result[0][0]:
		print(f"Spelling of '{word}' is correct!")
	else:
		print(f"Spelling of '{word}' is not correct!")
		print(f"Correct spelling of '{word}': '{result[0][0]}'\
 (with {result[0][1]} confidence).")


check_word_spelling('insert')
