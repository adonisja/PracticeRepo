from collections import defaultdict

def Grouping(words):
    groupedWords = defaultdict(list)
    for word in words:
        groupedWords[word[0]].append(word)

def main():
    pass

def testcases():
    return 
    [
        {"words" : ["apples", "banana", "cherries", "avocado", "currants", "blueberries"],
         "expected": {"a": ["apples", "avocado"], "b": ["banana", "blueberries"], "c" : ["cherries", "currants"]}
        }
    ]