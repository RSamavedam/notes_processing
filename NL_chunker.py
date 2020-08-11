import nltk
#TODO
#implement support for multiple subject / predicate
#create a wider array of possible sentences, like implications
sent = "The man met his mom"
sent_tk = nltk.pos_tag(nltk.word_tokenize(sent))
print(sent_tk)
Noun = ""
Verb = ""
Gerund = ""
Adj = ""
Adverb = ""
Modal = ""
Prep = ""
#split the sentence into its parts of speech
for word in sent_tk:
    if word[1] == "NN" or word[1] == "NNS" or word[1] == "NNP" or word[1] == "NNPS" or word[1] == "PRP":
        if Noun == "":
            Noun = "\'" + word[0] + "\' "
        else:
            Noun = Noun + "| \'" + word[0] + "\' "
    if word[1] == "VB" or word[1] == "VBD" or word[1] == "VBP" or word[1] == "VBZ":
        if Verb == "":
            Verb = "\'" + word[0] + "\' "
        else:
            Verb = Verb + "| \'" + word[0] + "\' "
    if word[1] == "VBG":
        if Gerund == "":
            Gerund = "\'" + word[0] + "\' "
        else:
            Gerund = Gerund + "| \'" + word[0] + "\' "
    if word[1] == "JJ" or word[1] == "JJR" or word[1] == "JJS" or word[1] == "PRP$" or word[1] == "VBN" or word[1] == "POS":
        if Adj == "":
            Adj = "\'" + word[0] + "\' "
        else:
            Adj = Adj + "| \'" + word[0] + "\' "
    if word[1] == "RB" or word[1] == "RBR" or word[1] == "RBS":
        if Adverb == "":
            Adverb = "\'" + word[0] + "\' "
        else:
            Adverb = Adverb + "| \'" + word[0] + "\' "
    if word[1] == "MD":
        if Modal == "":
            Modal = "\'" + word[0] + "\' "
        else:
            Modal = Modal + "| \'" + word[0] + "\' "
    if word[1] == "IN" and word[0] != "if" and word[0] != "because":
        if Prep == "":
            Prep = "\'" + word[0] + "\' "
        else:
            Prep = Prep + "| \'" + word[0] + "\' "



grammar2 = nltk.CFG.fromstring("""
Sent1 -> S P | S G | MS P | MS G
S -> S1 | S2 | S3 | S4 | S5 | S6 | S7 | S-det
MS -> MS1 | MS2 | MS3 | MS4 | MS5 | MS6 | MS7 | MS-det
S-det -> Det S1 | Det S2 | Det S3 | Det S4 | Det S5 | Det S6 | Det S7
MS-det -> Det MS1 | Det MS2 | Det MS3 | Det MS4 | Det MS5 | Det MS6 | Det MS7
S2 -> S1 Noun
S3 -> S1 Gerund
S4 -> S1 Adj
S5 -> S1 Adverb
S6 -> Noun Adverb Verb
S7 -> S1 Adverb Adj
S1 -> Noun Verb
MS2 -> MS1 Noun
MS3 -> MS1 Gerund
MS4 -> MS1 Adj
MS5 -> MS1 Adverb
MS6 -> Noun Modal Adverb Verb
MS7 -> MS1 Adverb Adj
MS1 -> Noun Modal Verb
G -> G1 | G2 | G3 | G4 | G5 | G6 | G7
G1 -> Gerund Adverb
G2 -> Gerund Adverb Adverb
G3 -> Gerund Adverb Noun
G4 -> Gerund Noun Adverb
G5 -> Gerund Adverb TO Adj Noun
G6 -> Gerund Adj Noun Adverb
G7 -> Gerund P1 | Gerund P2 | Gerund P3
P -> P1 | P2 | P3 | P4
P1 -> Prep Det Noun
P2 -> Prep Det Adj Noun
P3 -> Prep Adj Noun
P4 -> Prep Noun
Det -> 'a' | 'the' | 'A' | 'The'
TO -> 'to'
SEP -> ',' | '.'
Coor_conj -> 'for' | 'and' | 'nor' | 'but' | 'or' | 'yet' | 'so'
Imply -> 'because' | 'if' | 'Because' | 'If'
Noun -> {}
Verb -> {}
Gerund -> {}
Adj -> {}
Adverb -> {}
Modal -> {}
Prep -> {}
""".format(Noun, Verb, Gerund, Adj, Adverb, Modal, Prep))

split_sent = [word[0] for word in sent_tk]
#print(split_sent)
rd_parser = nltk.RecursiveDescentParser(grammar2)
#print(rd_parser.parse(split_sent))
all_trees = []
for tree in rd_parser.parse(split_sent):
    all_trees.append(tree)
print(all_trees[0])
