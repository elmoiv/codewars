from collections import Counter
def top_3_words(text):
	for i in list(r'!#$%&()*+,-./:;<=>?@[\]^_`{|}~0123456789'):text = text.replace(i,' ')
	return [i[0] for i in Counter(text.lower().split()).most_common(3) if i[0].replace("'",'').isalpha()]
