# 17 FEB 2026
# Today topic is Wordnet
""" 
WordNet = English dictionary + relations (computer ke liye)
👉 Ye batata hai:
word ka meaning
same meaning words (synonyms)
opposite meaning (antonyms)
word ka relation dusre words se
* WordNet NLTK ka part hai.

Examples:-
run
Meaning: move fast by foot
Synonyms: sprint, jog
"""

""" 
🔹 IMPORTANT TERM: SYNSET
🔑 Synset = Synonym Set
Synset = same meaning wale words ka group
ex:- {car, auto, automobile}
"""

from nltk.corpus import wordnet         

syns = wordnet.synsets('computer')
print(syns)
# [Synset('computer.n.01'), Synset('calculator.n.01')]
""" 
Meaning:-
computer → word
n → noun
01 → most common meaning
 """
print(syns[0].name())
print(syns[0].definition())
print(syns[0].examples())
print(syns[0].lemmas())