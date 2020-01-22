inputList = list(map(int, input("Please Enter A List : ").split()))
pairList = []
pairSum = 0
answerPairs = []
answerList = []
k = int(input("Enter Value Of K : "))
for i in range(0, len(inputList)):
    for j in range(i + 1, len(inputList)):
        pairList.append((inputList[i], inputList[j]))
for l in range(0, len(pairList)):
    pairSum = sum(pairList[l])
    if pairSum % k != 0:
        answerPairs = pairList[l]
        answer1 = answerPairs[0];
        answer2 = answerPairs[1];
        if not answerList.__contains__(answer1) in answerList:
            answerList.append(answer1)
        elif not answerList.__contains__(answer2) in answerList:
            answerList.append(answer2)
print(answerList, len(answerList))