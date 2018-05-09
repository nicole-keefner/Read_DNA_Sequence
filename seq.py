#import packages
import matplotlib.pyplot as plt
import pandas

#create Seq class
class Seq:

    #this class accepts a DNA sequence
    def __init__(self, sequence):
        self.sequence = sequence

    #this method counts theoretically possible kmers of size k
    def possibleKmers(self, k):
        length = len(self.sequence)
        assert (k < length + 1 and k >= 1 and k % 1 == 0)
        fourToK = 4**k
        if fourToK < length:
            return fourToK
        else:
            return length-k+1

    #this method counts observed kmers of size k
    def observedKmers(self, k):
        count = 0
        list = []
        length = len(self.sequence)
        assert (k < length + 1 and k >= 1 and k % 1 == 0)
        for i in range(0, length-k+1):
            kmer = self.sequence[i:i+k]
            if not kmer in list:
                list.append(kmer)
                count = count + 1
        return count

    #this method creates a pandas dataframe
    def createPandasDataFrame(self):
        length = len(self.sequence)
        kmerLengths = []
        observedKmersList = []
        possibleKmersList = []
        for k in range(1, length + 1):
            observed = self.observedKmers(k)
            possible = self.possibleKmers(k)
            kmerLengths.append(k)
            observedKmersList.append(observed)
            possibleKmersList.append(possible)
        d = {'k':kmerLengths, 'Observed kmers':observedKmersList, 'Possible kmers':possibleKmersList}
        df = pandas.DataFrame(data=d)
        df = df[['k', 'Observed kmers', 'Possible kmers']]
        df = df.set_index('k')
        df.loc['Total']= df.sum()
        return df

    #this method produces a graph of the kmer size on the x-axis and the proportion of observed/possible kmers on the y-axis
    def createGraph(self):
        df = self.createPandasDataFrame()
        kmerLengths = df.index.tolist()
        observedKmersList = df['Observed kmers'].tolist()
        possibleKmersList = df['Possible kmers'].tolist()
        proportions = []
        for i in range(0, len(kmerLengths)):
            proportion = observedKmersList[i] / (possibleKmersList[i] * 1.0)
            proportions.append(proportion)
        d1 = {'k':kmerLengths, 'Proportion Observed':proportions}
        df1 = pandas.DataFrame(data=d1)
        df1 = df1.set_index('k')
        return df1.plot(kind='bar');

    #this method calculates the linguistic complexity of the sequence (i.e. total observed kmers/total possible kmers)
    def linguisticComplexity(self):
        length = len(self.sequence)
        observedKmersList = []
        possibleKmersList = []
        for k in range(1, length + 1):
            observed = self.observedKmers(k)
            possible = self.possibleKmers(k)
            observedKmersList.append(observed)
            possibleKmersList.append(possible)
        return sum(observedKmersList) / sum(possibleKmersList) * 1.0

#Examples of how to use these methods:
#foo = Seq("TTATTAATGAAC")
#k = 2
#obs = foo.observedKmers(k)
#print(obs)
#pos = foo.possibleKmers(k)
#print(pos)
#df = foo.createPandasDataFrame()
#print(df)
#graph = foo.createGraph()
#print(graph)
#lC = foo.linguisticComplexity()
#print(lC)

##END##
