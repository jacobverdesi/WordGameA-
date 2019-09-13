from string import ascii_lowercase
def search(curr,goal,dict,indexs,path):
    if curr==goal:
        path.append(curr)
        return path
    else:
        newIndex = indexs
        for i in range(len(indexs)):
            print(i,indexs)
            for g in range(newIndex[i]+97,123):
                newPath=path
                s=curr
                s = s[:i] + str(chr(g)) + s[i + 1:]
                newIndex[i]=g-96
                if (dict.__contains__(s) and not newPath.__contains__(s)):
                    newPath.append(curr)
                    print(s,newPath)
                    search(s,goal,dict,newIndex,newPath)
            print("test")


def searchHelper(curr,goal,dict):
    indexs=[0]*len(curr)
    print(indexs)
    return search(curr,goal,dict,indexs,path=[])
def main(filename):
    file=open(filename)
    dict=[]
    for line in file:
        dict.append(line.strip())
    path=searchHelper("cold","warm",dict)
    print(path)
if __name__ == '__main__':
    main("exampleWords.txt")