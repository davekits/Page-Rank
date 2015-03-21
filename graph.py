import re
import matplotlib.pyplot as plt
import numpy as np
"This is testing for Git Hub"
counts = []
voted = []
def clean_string(s):
    stripped = s.strip().capitalize();
    stripped = re.sub(r"\s+", " ", stripped)
    return stripped

def has_already_voted(name):
    if name in voted:
        print(name + " has already voted! Fraud!")
        return True
    return False

def count_vote(radish): 
    if not radish in counts:
        counts[radish] = 1
    else:
        counts[radish] += 1

for line in open("radishsurvey.txt"):
    line = line.strip()
    name, vote = line.split(" - ")
    name = clean_string(name)
    vote = clean_string(vote)
    count_vote(vote)
    voted.append(name)

#print the results

print("Results: ")
for name in counts:
    print(name + ": " + str(counts[name]))

#find the winner
maxVote = None
winner = None 
for vote in counts:
    count = counts[vote]
    if not maxVote or count > maxVote:
        maxVote = count
        winner = vote

print("Winner: " + winner + " - vote: " + str(maxVote))

names = []
votes = []
for radish in counts:
    names.append(radish)
    votes.append(counts[radish])

print(names)

x = np.arange(len(counts))
plt.bar(x, votes)
plt.xticks(x + 0.5, names, rotation=90)

raw_input()
