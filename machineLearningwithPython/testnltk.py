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

"""Combining Algorithms with Vote -> GOTO (2)"""

from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes/ len(votes)
        return conf

"""Word features"""

word_features = list(all_words.keys())[:3000]

def findFeatures(docs):
    words = set(docs)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print(findFeatures(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(findFeatures(rev),category) for (rev,category) in doc]

"""Naive Bayes Algorithm"""
"""Non grammer feature... just based on words.. count"""

traning_set  = featuresets[:1900]
testing_set  = featuresets[1900:]

##classifier = nltk.NaiveBayesClassifier.train(traning_set)
##print("NAive bayes ALgo: ", (nltk.classify.accuracy(classifier, testing_set))*100)
##
##classifier.show_most_informative_features(15)

"""Save classifier using Pickle"""
"""Used to save all the training objects"""
import pickle

#save the Object
##save_classifier = open("naivebayes.pickle","wb")
##pickle.dump(classifier,save_classifier)
##save_classifier.close()
 

#load traing data Object
read_classifier = open("naivebayes.pickle","rb")
classifier = pickle.load(read_classifier)
read_classifier.close()
print("NAive bayes ALgo: ", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)


"""Scikit learn incorporation"""
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC , NuSVC

#MultinomialNB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(traning_set)
print("MNB_classifier acuracy percent: " , (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


#GaussianNB
"""Does work with SKLearn classifier """
##GNB_classifier = SklearnClassifier(GaussianNB())
##GNB_classifier.train(traning_set)
##print("GNB_classifier acuracy percent: " , (nltk.classify.accuracy(GNB_classifier, testing_set))*100)

#BrnoulliNB
BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(traning_set)
print("BNB_classifier acuracy percent: " , (nltk.classify.accuracy(BNB_classifier, testing_set))*100)

#LogisticRegression
Logis_classifier = SklearnClassifier(LogisticRegression())
Logis_classifier.train(traning_set)
print("Logis_classifier acuracy percent: " , (nltk.classify.accuracy(Logis_classifier, testing_set))*100)

#SGDClassifier
SGD_classifier = SklearnClassifier(SGDClassifier())
SGD_classifier.train(traning_set)
print("SGD_classifier acuracy percent: " , (nltk.classify.accuracy(SGD_classifier, testing_set))*100)

#SVC
##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(traning_set)
##print("SVC_classifier acuracy percent: " , (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

#LinearSVC
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(traning_set)
print("LinearSVC_classifier acuracy percent: " , (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

#NuSVC
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(traning_set)
print("NuSVC_classifier acuracy percent: " , (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)


"""
::::: Accuracy Score ::::::
MNB_classifier acuracy percent:  87.0
BNB_classifier acuracy percent:  85.0
Logis_classifier acuracy percent:  88.0
SGD_classifier acuracy percent:  85.0
SVC_classifier acuracy percent:  82.0
LinearSVC_classifier acuracy percent:  83.0
NuSVC_classifier acuracy percent:  86.0
"""


"""(2) Combining Algorithms with Vote"""

voted_classifer = VoteClassifier(classifier,LinearSVC_classifier,MNB_classifier,BNB_classifier,SGD_classifier,LinearSVC_classifier,NuSVC_classifier)
print("voted_classifer accuracy percent: " , (nltk.classify.accuracy(voted_classifer, testing_set))*100)
print("Classfication:", voted_classifer.classify(testing_set[0][0]), "Confidence : %", (voted_classifer.confidence(testing_set[0][0]))*100)
print("Classfication:", voted_classifer.classify(testing_set[1][0]), "Confidence : %", (voted_classifer.confidence(testing_set[1][0]))*100)
print("Classfication:", voted_classifer.classify(testing_set[2][0]), "Confidence : %", (voted_classifer.confidence(testing_set[2][0]))*100)
print("Classfication:", voted_classifer.classify(testing_set[3][0]), "Confidence : %", (voted_classifer.confidence(testing_set[3][0]))*100)
print("Classfication:", voted_classifer.classify(testing_set[4][0]), "Confidence : %", (voted_classifer.confidence(testing_set[4][0]))*100)
print("Classfication:", voted_classifer.classify(testing_set[5][0]), "Confidence : %", (voted_classifer.confidence(testing_set[5][0]))*100)

