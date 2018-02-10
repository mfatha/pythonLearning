import nltk

#nltk.download()


#tokenzing -> work tokenizer, sentence tokenizer: grouping of data
#lexicon and corporas
#corporas -> body of text eg : medical rport anything in english language
#lexicon -> word and their meaning

#investor-speak -> regular english speak -> position in state
#english-speak  -> general english speak ->  grammer meaning

"""tokenize"""
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Hello mr. fathauddin world, how are you? what doing da? wherer?"

##print(sent_tokenize(text))
##
##print(word_tokenize(text))


##for i in word_tokenize(text):
##    print(i)


"""stopwords"""
#from nltk.corpus import stopwords

text = "text is example of stop word filtering"

#stop_words = set(stopwords.words("english"))
"""
{'both', 'm', "should've", 'as', 'yourself', 'when', 'ain', 'very', 'to', 'aren', 'such', 'if', 'there', 't', 'we', 'too', "wasn't", 'not', 'who', 'each', 'on', 'above', 'the', 'is', 'be', "needn't", 'at', 'has', "won't", 'below', 'was', 'itself', 'yourselves', 'an', 'once', 'out', "that'll", 'they', 'it', 'a', 'mightn', 'here', 'wouldn', 'myself', 'own', "hasn't", 'am', 'himself', 'him', "weren't", 'been', 'hasn', 'just', "shan't", 'her', 'and', 'or', "isn't", "doesn't", 'yours', 'doing', 'by', 'some', 'weren', 'had', 'same', 'isn', 'in', 'which', "you're", 'having', 'he', 'any', 'herself', 'against', 'have', "couldn't", 'our', "you'd", 'theirs', 'what', 'this', "hadn't", 'for', "didn't", 'off', "shouldn't", 'haven', 'where', 'ourselves', 'but', "aren't", 'down', 'those', "haven't", 'you', 'couldn', 'few', 'under', 'she', 'during', 'while', 'most', 'shouldn', 'don', "wouldn't", 'my', 'now', 'so', 'does', "you've", 'ours', 'how', 're', 'between', 'are', 'do', 'should', "it's", 'more', 'me', 'nor', 'needn', 'them', 'being', 'his', 'up', 'were', 'o', 's', "you'll", 'shan', 'over', 've', 'hers', 'than', 'won', 'didn', "she's", 'because', 'all', 'of', 'did', 'that', 'before', 'will', 'whom', 'again', 'about', 'these', 'then', 'its', 'other', "don't", 'your', 'themselves', 'no', 'hadn', 'wasn', 'll', 'with', 'from', 'i', 'only', 'into', 'further', 'ma', "mightn't", 'after', 'why', 'their', 'd', 'until', 'mustn', "mustn't", 'through', 'doesn', 'y', 'can'}
"""

#print(stopwords)

words = word_tokenize(text)

##filtered_sentence = []
##
##for w in words:
##    if w not in stop_words:
##        filtered_sentence.append(w)
##
##print(filtered_sentence)

##filtered_sentence =[w for w in words if not w in stop_words]
##
##print(filtered_sentence)



"""Stemming"""
#from nltk.stem import PorterStemmer

##ps= PorterStemmer()
##
##words =["python","pythoner","pythoned","pythonly","pythoning"]
##
##for w in words:
##    print(ps.stem(w))


"""Speech tagging"""
#from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer

##traintext = state_union.raw("2005-GWBush.txt")
##sampletext = state_union.raw("2006-GWBush.txt")
##
##custom = PunktSentenceTokenizer(traintext)
##
##token = custom.tokenize(sampletext)
##
##def process():
##    try:
##        for i in token:
##            word = nltk.word_tokenize(i)
##            tagges = nltk.pos_tag(word)
##            print(tagges)
##    except Exception as e:
##        print(e)
##
##process()
"""

Given a sentence or paragraph, it can label words such as verbs, nouns and so on.
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""



"""Chunking"""
"""Find of Something"""

"""Chinking"""
"""Removing of Something"""

##traintext = state_union.raw("2005-GWBush.txt")
##sampletext = state_union.raw("2006-GWBush.txt")
##
##custom = PunktSentenceTokenizer(traintext)
##
##token = custom.tokenize(sampletext)
##
##def process():
##    try:
##        for i in token:
##            word = nltk.word_tokenize(i)
##            tagges = nltk.pos_tag(word)
##            
##            #chunking
##            #chunkGram = r"""Chunk:{<RB.?>*<VB.?>*<NNP>+<NN>?}"""
##
##            #chinking
##            chunkGram = r"""Chunk:{<.*>+}
##                                    }<VB.?|IN|DT>+{"""
##            
##            chunkParser = nltk.RegexpParser(chunkGram)
##            chunked = chunkParser.parse(tagges)
##            chunked.draw()
##    except Exception as e:
##        print(e)
##
##process()



"""Name entinty Recognition"""
##traintext = state_union.raw("2005-GWBush.txt")
##sampletext = state_union.raw("2006-GWBush.txt")
##
##custom = PunktSentenceTokenizer(traintext)
##
##token = custom.tokenize(sampletext)
##
##def process():
##    try:
##        for i in token:
##            word = nltk.word_tokenize(i)
##            tagges = nltk.pos_tag(word)
##            namedEnt = nltk.ne_chunk(tagges)
##
##            namedEnt.draw()
##            
##    except Exception as e:
##        print(e)
##
##process()

"""
NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
"""



"""Lemmatizing"""
"""Stemming some form of synonam"""
"""pural to single"""
from nltk.stem import WordNetLemmatizer

##lemmatizer = WordNetLemmatizer()
##
##print(lemmatizer.lemmatize("cats"))
##print(lemmatizer.lemmatize("goods", pos="a"))
##print(lemmatizer.lemmatize("better", pos="n"))
##print(lemmatizer.lemmatize("running", "v"))
##print(lemmatizer.lemmatize("placements"))
##print(lemmatizer.lemmatize("rocks"))
##print(lemmatizer.lemmatize("mice"))

#print(nltk.__file__)


"""Corpora"""
#from nltk.corpus import gutenberg

##
##sample = gutenberg.raw("bible-kjv.txt")
##
##tok =  sent_tokenize(sample)
##
##print(tok[5:15])


"""Wordnet"""
"""Word menaing definistion and antomons"""
#from nltk.corpus import wordnet

##syn = wordnet.synsets("program")
##
###synset
##print(syn)
##print(syn[0].name())
##
###just the word
##print(syn[0].lemmas())
##print(syn[0].lemmas()[1].name())
##
##
###definition
##print(syn[0].definition())
##
###example
##print(syn[1].examples())

##synonyms = []
##antonyms = []
##
##for syn in wordnet.synsets("good"):
##    for l in syn.lemmas():
##        #print(l)
##        synonyms.append(l.name())
##        if l.antonyms():
##            #print(l.antonyms())
##            antonyms.append(l.antonyms()[0].name())
##
##print(set(synonyms))
##print(set(antonyms))


"""WORDNET ->symantic Similarity"""
###compare words 
##w1 = wordnet.synset("good.n.01")
##w2 = wordnet.synset("bad.n.01")
###wup -> wone and pumber logic
##print(w1.wup_similarity(w2)*100)


"""Text classification"""
import random
from nltk.corpus import movie_reviews

doc = [(list(movie_reviews.words(fileid)), category)
       for category in movie_reviews.categories()
       for fileid in movie_reviews.fileids(category)]

#similar to
##doc=[]
##for category in movie_reviews.categories():
##    for fileid in movie_reviews.fileids(category):
##        doc.append(list(movie_reviews.words(fileid)),category)

random.shuffle(doc)
#print(doc[1])

all_words= []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

#print(all_words.most_common(15))
#print(all_words["stupid"])

"""Word features"""

word_features = list(all_words.keys())[:3000]

def findFeatures(docs):
    words = set(docs)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

print(findFeatures(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(findFeatures(rev),category) for (rev,category) in doc]
