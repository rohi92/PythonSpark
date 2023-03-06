class WordDictionary:

    def __init__(self, l1):
        self.l1=l1

    def addWord(self, word) :
        self.l1.append(word)

    def search(self, word):
        count = 0
        word1=word
        if len(self.l1)==0:
            return False
        for i in self.l1:
            if count<len(word1):
                diff=set(word)-set(i)
                if len(diff)<len(set(word)) and len(diff)!=0:
                    count=count+len(word)-len(diff)
                    word="".join(diff)
                elif len(diff)==0:
                    return True
            elif count==len(word):
                return True
        return False






if __name__=="__main__":
    sol=WordDictionary([])
    sol.addWord('bads')
    sol.addWord("dadf")
    sol.addWord("madq")
    print(sol.search("qsm"))
