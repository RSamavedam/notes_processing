import nltk
#TODO
#implement support for multiple subject / predicate -> mostly done
#create a wider array of possible sentences, like implications
# add in infinitive phrases
#add a DS that has a P / G / infinitive after it
import sys
def get_tree():
    sent = "Nixon, who was very corrupt, was impeached after many hearings on the house floor"
    sent_tk = nltk.pos_tag(nltk.word_tokenize(sent))
    print(sent_tk)
    Noun = ""
    Verb = ""
    Gerund = ""
    Adj = ""
    Adverb = ""
    Modal = ""
    Prep = ""
    WDT = ""
    #split the sentence into its parts of speech
    for word in sent_tk:
        if word[1] == "NN" or word[1] == "NNS" or word[1] == "NNP" or word[1] == "NNPS" or word[1] == "PRP" or word[1] == "CD":
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
        if word[1] == "WDT" or word[1] == "WP":
            if Prep == "":
                WDT = "\'" + word[0] + "\' "
            else:
                WDT = WDT + "| \'" + word[0] + "\' "



    grammar2 = nltk.CFG.fromstring("""
    Sent1 -> S P | S G | MS P | MS G | S | MS
    Sent2 -> S DS | S SEP DS | DS SEP S | P SEP S | G SEP S | DS SEP S P | P SEP S P | G SEP S P | DS SEP S G | P SEP S G | G SEP S G
    S -> S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S-det
    MS -> MS1 | MS2 | MS3 | MS4 | MS5 | MS6 | MS7 | MS8 | MS9 | MS10 | MS11 | MS12 | MS13 | MS-det

    S-det -> Det S1 | Det S2 | Det S3 | Det S4 | Det S5 | Det S6 | Det S7 | Det S8 | Det S9 | Det S10 | Det S11 | Det S12 | Det S13
    MS-det -> Det MS1 | Det MS2 | Det MS3 | Det MS4 | Det MS5 | Det MS6 | Det MS7 | Det MS8 | Det MS10 | Det MS11 | Det MS12 | Det MS13

    S2 -> S1 Noun
    S3 -> S1 Gerund
    S4 -> S1 Adj
    S5 -> S1 Adverb
    S6 -> S1 Adverb Adj
    S7 -> S1 Det Noun
    S8 -> Noun Adverb Verb
    S9 -> S1_D Adj
    S10 -> Noun P Adverb Verb | Noun G Adverb Verb
    S11 -> S1_D Adverb Adj
    S12 -> S1_D Adverb
    S13 -> S1_D Adj
    S1 -> Noun Verb
    S1_D -> S1_P | S1_G | S1_W
    S1_P -> Noun P Verb
    S1_G -> Noun G Verb
    S1_W -> Noun DS Verb | Noun SEP DS SEP Verb

    MS2 -> MS1 Noun
    MS3 -> MS1 Gerund
    MS4 -> MS1 Adj
    MS5 -> MS1 Adverb
    MS6 -> MS1 Adverb Adj
    MS7 -> MS1 Det Noun
    MS8 -> Noun Modal Adverb Verb
    MS9 -> MS1_D Adj
    MS10 -> Noun P Modal Verb Adj | Noun G Modal Verb Adj
    MS11 -> MS1_D Adverb Adj
    MS12 -> MS1_D Adverb
    MS13 -> MS1_D Adj
    MS1 -> Noun Modal Verb
    MS1_D -> MS1_P | MS1_G | MS1_W
    MS1_P -> Noun P Modal Verb
    MS1_G -> Noun G Modal Verb
    MS1_W -> Noun DS Modal Verb | Noun SEP DS SEP Modal Verb

    DS -> DS1 | DS2 | DS3 | DS4 | DS5 | DS6 | DS7 | DS8 | DS9 | DS10 | DS11 | DS12 | DS13
    DS2 -> DS1 Noun
    DS3 -> DS1 Gerund
    DS4 -> DS1 Adj
    DS5 -> DS1 Adverb
    DS6 -> DS1 Adverb Adj
    DS7 -> DS1 Det Noun
    DS8 -> WDT Adverb Verb
    DS9 -> DS1_D Adj
    DS10 -> WDT P Adverb Verb | Noun G Adverb Verb
    DS11 -> DS1_D Adverb Adj
    DS12 -> DS1_D Adverb
    DS13 -> DS1_D Adj
    DS1 -> WDT Verb
    DS1_D -> DS1_P | DS1_G
    DS1_P -> WDT P Verb
    DS1_G -> WDT G Verb


    G -> G1 | G2 | G3 | G4 | G5 | G6 | G7
    G1 -> Gerund Adverb
    G2 -> Gerund Adverb Adverb
    G3 -> Gerund Adverb Noun
    G4 -> Gerund Noun Adverb
    G5 -> Gerund Adverb TO Adj Noun
    G6 -> Gerund Adj Noun Adverb
    G7 -> Gerund P

    P -> P_singular | P_singular P_singular | P_singular Coor_conj P_singular | P_singular P_singular P_singular | P_singular P_singular Coor_conj P_singular
    P_singular -> P1 | P2 | P3 | P4 | P5 | P6
    P1 -> Prep Det Noun
    P2 -> Prep Det Adj Noun
    P3 -> Prep Adj Noun
    P4 -> Prep Noun
    P5 -> Prep Gerund Det Noun | Prep Gerund Noun
    P6 -> Prep Gerund Adverb

    Det -> 'a' | 'the' | 'A' | 'The'
    TO -> 'to' | 'To'
    Noun -> Noun_singular | Noun_singular Coor_conj Noun_singular | Noun_singular SEP Noun_singular SEP Coor_conj Noun_singular | Noun_singular SEP Noun_singular Coor_conj Noun_singular | Noun_singular Noun_singular
    Verb -> Verb_singular | Verb_singular Coor_conj Verb_singular | Verb_singular SEP Verb_singular SEP Coor_conj Verb_singular | Verb_singular SEP Verb_singular Coor_conj Verb_singular
    Gerund -> Gerund_singular | Gerund_singular Coor_conj Gerund_singular | Gerund_singular SEP Gerund_singular SEP Coor_conj Gerund_singular | Gerund_singular SEP Gerund_singular Coor_conj Gerund_singular
    Adj -> Adj_singular | Adj_singular Coor_conj Adj_singular | Adj_singular SEP Adj_singular SEP Coor_conj Adj_singular | Adj_singular SEP Adj_singular Coor_conj Adj_singular
    Adverb -> Adverb_singular | Adverb_singular Coor_conj Adverb_singular | Adverb_singular SEP Adverb_singular SEP Coor_conj Adverb_singular | Adverb_singular SEP Adverb_singular Coor_conj Adverb_singular
    SEP -> ',' | '.'
    Coor_conj -> 'for' | 'and' | 'nor' | 'but' | 'or' | 'yet' | 'so'
    Imply -> 'because' | 'if' | 'Because' | 'If'
    Noun_singular -> {}
    Verb_singular -> {}
    Gerund_singular -> {}
    Adj_singular -> {}
    Adverb_singular -> {}
    Modal -> {}
    Prep -> {}
    WDT -> {}
    """.format(Noun, Verb, Gerund, Adj, Adverb, Modal, Prep, WDT))

    split_sent = [word[0] for word in sent_tk]
    #print(split_sent)
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    #print(rd_parser.parse(split_sent))
    all_trees = []
    for tree in rd_parser.parse(split_sent):
        all_trees.append(tree)
    print(all_trees[0])

    for tree in all_trees[0]:
        print(tree.label)
    return all_trees[0]

def listToString(words):
    outputString = ""
    for word in words:
        if word != ",":
            outputString = outputString + " " + word
        else:
            outputString = outputString + word

    outputString = outputString[1:]
    return outputString


def getLeafString(tree):
    words = tree.leaves()
    outputString = ""
    for word in words:
        if word != ",":
            outputString = outputString + " " + word
        else:
            outputString = outputString + word

    outputString = outputString[1:]
    return outputString

def getChildren(tree):
    new_level = []
    for child in tree:
        new_level.append(child)
    return new_level

def isPerson(noun_string):
    sent_tk = nltk.pos_tag(nltk.word_tokenize(noun_string))
    result = nltk.ne_chunk(sent_tk, binary=True)
    new_level = getChildren(result) #new_level always has length one
    type = new_level[0].label()
    return (type == "PERSON")


def processTree(main_tree):
    #generates questions
    q_and_a = []
    end_descriptor = ""
    level_1 = []
    for child in main_tree:
        level_1.append(child)
    #Level_1_labels = [tree.label() for tree in level_1]
    if len(level_1) == 2:
        end_descriptor = getLeafString(level_1[1])
        level_2 = []
        for child in level_1[0]:
            level_2.append(child)
        s_label = level_2[0].label() #only has one element
        has_modal = False
        has_det = False
        enumerator = 0
        if "det" in s_label:
            has_det = True
            level_2 = getChildren(level_2[0])
            s_label = level_2[0].label()
        #at this point level_2 is either S(x) or MS(x)
        if s_label[0:1] == "M":
            has_modal = True
            enumerator = int(s_label[2:])
        else:
            enumerator = int(s_label[1:])
        if enumerator < 8:
            level_3 = getChildren(level_2[0]) #at this point level_3 of form: (M)S1 {optional} {optional}
            level_4 = getChildren(level_3[0]) #at this point level_4 of form: Noun {optional modal} Verb
            question = ""
            if (isPerson(getLeafString(level_4[0]))):
                question = "Who"
            else:
                question = "What"
            for i in range(1, len(level_4)):
                question = question + " " + getLeafString(level_4[i])
            for i in range(1, len(level_3)):
                question = question + " " + getLeafString(level_3[i])
            question = question + end_descriptor + "?"
            answer = getLeafString(level_4[0])
            q_and_a.append((question, answer))
            #you can ask what did [subject] do / what happened to [subject] potentially as another question
        if enumerator == 8:
            #easy case
            level_3 = getChildren(level_2[0]) #at this point level_3 of form: Noun {optional modal} adverb verb
            question = ""
            if (isPerson(getLeafString(level_3[0]))):
                question = "Who"
            else:
                question = "What"
            for i in range(1, len(level_3)):
                question = question + " " + getLeafString(level_4[i])
            question = question + end_descriptor + "?"
            answer = getLeafString(level_3[0])
            q_and_a.append((question, answer))
            #you can ask what did [subject] do / what happened to [subject] potentially as another question
        if enumerator >= 9 and enumerator != 10:
            level_3 = getChildren(level_2[0]) #at this point level_3 of form: (M)S1_D {optional} {optional}
            level_4 = getChildren(level_3[0]) #at this point level_4 has one value, either (M)S1_(P G or W)
            level_5 = getChildren(level_4[0]) #at this point level_5 of form: (Noun (P or G) {optional modal} Verb) or (Noun {optional SEP} DS {optional SEP} {Optional Modal} Verb)
            level_5_labels = [member.label() for member in level_5]
            if "DS" not in level_5_labels:
                #know that it's first case
                question = ""
                if (isPerson(getLeafString(level_5[0]))):
                    question = "Who"
                else:
                    question = "What"
                for i in range(1, len(level_5)):
                    question = question + " " + getLeafString(level_5[i])
                question = question + end_descriptor + "?"
                answer = getLeafString(level_5[0])
                q_and_a.append((question, answer))
                #you can ask what did [subject] do / what happened to [subject] potentially as another question
            else:
                index = 1
                if level_5_labels[1] == "SEP":
                    index += 1
                question = getLeafString(level_5[index]) + "?"
                answer = getLeafString(level_5[0])
                q_and_a.append((question, answer))
                #can copy over previous case to here
    return q_and_a
