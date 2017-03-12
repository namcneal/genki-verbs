# -*- coding: utf-8 -*-
from Verb import Verb
import FileIO


test_list = FileIO.import_verb_list('testing_verb_list.csv')
test_verbs = list()

for row in test_list:
    test_verbs.append(Verb(row[0], row[1], row[2], row[3]))

for verb in test_verbs:
    print verb.causative_passive()
    
