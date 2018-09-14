#!/usr/bin/python

class Dictionary:
    def __init__(self, words):
        self.words = words

    def most_familiar_with(self, word):
        return min([(self.dist(word, e), e) for e in self.words])[1]

    def dist(self, a, b):
        la = len(a)
        lb = len(b)
        dist = [[0 for i in range(la + 1)] for j in range(lb + 1)]
        for i in range(la + 1):
            dist[0][i] = i
        for i in range(lb + 1):
            dist[i][0] = i

        for i in range(1, lb + 1):
            for j in range(1, la + 1):
                if a[j-1] == b[i-1]:
                    dist[i][j] = dist[i-1][j-1]
                else:
                    dist[i][j] = 1 + min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1])
        return dist[i][j]

words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
test_dict = Dictionary(words)
print test_dict.most_familiar_with('berry')

#print distance("kgood", "kissgoodbye")
