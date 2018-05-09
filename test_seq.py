#!/usr/bin/env python
#to use: in the anaconda prompt, type py.test test_seq.py to make sure that the tests are successful

#* imports everything from seq.py script
from seq import *
import pytest

#creating example Seq objects
example = Seq("TTATTAATGAACCCCTACGC")
example2 = Seq("ATTTGGATT")

######################################
###possibleKmers tests###
#test k=1 produces 4 kmers
def test_possibleKmers1():
    kmers1 = example.possibleKmers(1)
    assert kmers1 == 4
#test k=2 produces 16 kmers
def test_possibleKmers2():
    kmers2 = example.possibleKmers(2)
    assert kmers2 == 16
#test k=5 produces 16 kmers
def test_possibleKmers5():
    kmers5 = example.possibleKmers(5)
    assert kmers5 == 16
#test k=19 produces 2 kmers
def test_possibleKmers19():
    kmers19 = example.possibleKmers(19)
    assert kmers19 == 2
#test k=20 produces 1 kmer
def test_possibleKmers20():
    kmers20 = example.possibleKmers(20)
    assert kmers20 == 1
######################################
###observedKmers tests###
#test k=1 produces 4 kmers
def test_observedKmers1():
    kmers1 = example.observedKmers(1)
    assert kmers1 == 4
#test k=2 produces 11 kmers
def test_observedKmers2():
    kmers2 = example.observedKmers(2)
    assert kmers2 == 11
#test k=5 produces 16 kmers
def test_observedKmers5():
    kmers5 = example.observedKmers(5)
    assert kmers5 == 16
#test k=19 produces 2 kmers
def test_observedKmers19():
    kmers19 = example.observedKmers(19)
    assert kmers19 == 2
#test k=20 produces 1 kmer
def test_observedKmers20():
    kmers20 = example.observedKmers(20)
    assert kmers20 == 1
######################################
###createPandasDataFrame test###
def test_createPandasDataFrame():
    correctPossibleList = [4, 8, 7, 6, 5, 4, 3, 2, 1, 40]
    correctObservedList = [3, 5, 6, 6, 5, 4, 3, 2, 1, 35]
    df = example2.createPandasDataFrame()
    possibleList = df['Possible kmers'].tolist()
    observedList = df['Observed kmers'].tolist()
    assert possibleList == correctPossibleList
    assert observedList == correctObservedList
######################################
#def test_createGraph(self):
#I'm not sure how to test a graph
######################################
###linguisticComplexity test###
def test_linguisticComplexity():
    lincom = example2.linguisticComplexity()
    assert lincom == 0.875

###END###
