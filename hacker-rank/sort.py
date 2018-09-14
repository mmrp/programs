#!/usr/bin/python

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        
    def __repr__(self):
        return "name : {}, score: {}".format(self.name, self.data)
   # @staticmethod
    def cmp_string(s1, s2):
        #print(type(s1), type(s2))
        s1 = list(map(ord, s1))
        s2 = list(map(ord, s2))
        l1 = len(s1)
        l2 = len(s2)
        l = min(l1, l2)
        for i in range(l):
            r = s1[i] - s2[i]
            if r != 0:
                return r       
        return l1 - l2
        
        
    def comparator(a, b):
        score = b.score - a.score
        return score if score != 0 else Player.cmp_string(a.name, b.name)
        
n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)


