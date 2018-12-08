def countSentences(wordSet, sentences):
    dic = {}
    for i in range(len(wordSet)):
        sel = anagram(wordSet[i])
        if sel not in dic:
            dic[sel] = 1
        else:
            dic[sel]+=1
    l = []
    for sentence in sentences:
        temp = 1
        for wordSet in sentence.split(' '):

            if anagram(wordSet) in dic:

                temp *= dic[anagram(wordSet)]
        l.append(temp)
    return l

def anagram(s):
    result = 0

    return ''.join(sorted(s))



words = ['star','tars','stay','tay','seed','dees','eesd','rast','date','ate']
sentences = ['ate date stay ',
             'rast tay star',
             'tay stay tars',
             'seed dees star',
             'ate seed rast'
             ]
print(countSentences(words,sentences))


