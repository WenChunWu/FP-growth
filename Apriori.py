from numpy import *
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


# 其中D為全部數據集，
# # Ck為大小為k（包含k個元素）的候選項集，
# # minSupport為設定的最小支持度。
# # 返回值中retList為在Ck中找出的頻繁項集（支持度大於minSupport的），
# # supportData記錄各頻繁項集的支持度
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems     # 計算頻數
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


# 生成 k+1 項集的候選項集
# 注意其生成的過程中，首選對每個項集按元素排序，然後每次比較兩個項集，只有在前k-1項相同時才將這兩項合併。
# # 這樣做是因為函數並非要兩兩合併各個集合，那樣生成的集合並非都是k+1項的。在限制項數為k+1的前提下，只有在前k-1項相同、最後一項不相同的情況下合併才為所需要的新候選項集。
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            # 前k-2項相同時，將兩個集合合併
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


# 頻繁項集列表L
# 包含那些頻繁項集支持數據的字典supportData
# 最小可信度閾值minConf
def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    # 頻繁項集是按照層次搜索得到的, 每一層都是把具有相同元素個數的頻繁項集組織成列表，再將各個列表組成一個大列表，所以需要遍歷Len(L)次, 即逐層搜索
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]    # 對每個頻繁項集構建只包含單個元素集合的列表H1
            print("\nfreqSet: ", freqSet)
            print("H1: ", H1)
            rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)     # 根據當前候選規則集H生成下一層候選規則集
    return bigRuleList


# 根據當前候選規則集H生成下一層候選規則集
def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    while (len(freqSet) > m):  # 判斷長度 > m，這時即可求H的可信度
        H = calcConf(freqSet, H, supportData, brl, minConf)     # 返回值prunedH保存規則列表的右部，這部分頻繁項將進入下一輪搜索
        if (len(H) > 1):  # 判斷求完可信度後是否還有可信度大於閾值的項用來生成下一層H
            H = aprioriGen(H, m + 1)
            print("H = aprioriGen(H, m + 1): ", H)
            m += 1
        else:  # 不能繼續生成下一層候選關聯規則，提前退出循環
            break

# 計算規則的可信度，並過濾出滿足最小可信度要求的規則
def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    ''' 對候選規則集進行評估 '''
    prunedH = []
    for conseq in H:
        print("conseq: ", conseq)
        print("supportData[freqSet]: ", supportData[freqSet])
        print("supportData[freqSet - conseq]: ", supportData[freqSet - conseq])
        conf = supportData[freqSet] / supportData[freqSet - conseq]
        if conf >= minConf:
            print(freqSet - conseq, '-->', conseq, 'conf:', conf)
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
            print("prunedH: ", prunedH)
    return prunedH





dataSet = loadDataSet()
L, suppData = apriori(dataSet, minSupport=0.5)      # 得到頻繁項集列表L，以及每個頻繁項的支持度
print("頻繁項集L: ")
for i in L:
    print(i)
print("頻繁項集L的支持度列表suppData: ")
for key in suppData:
    print(key, suppData[key])

# 基於頻繁項集生成滿足置信度閾值的關聯規則
rules = generateRules(L, suppData, minConf=0.7)
print("rules = generateRules(L, suppData, minConf=0.7)")
print("rules: ", rules)


rules = generateRules(L, suppData, minConf=0.5)
#print
#print "rules = generateRules(L, suppData, minConf=0.5)"
#print "rules: ", rules