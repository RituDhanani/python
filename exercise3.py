sentences=["my name is ram","he is a good person","you should be careful while coding","he can do better","the person is mysterious","jay shree ram","it is my pen"]

word_trees=[sentance.split()for sentance in sentences]
print("list of word trees is ",word_trees)

count={}
for tree in word_trees:
    for word in tree:
        if word in count:
            count[word]+=1
        else:
            count[word]=1

print("\n number of word count is ",count)