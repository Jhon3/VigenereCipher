import sys
class Vigenere:
    def __init__(self, fileAlfa):
        self.__alfa = self.getAlfa(fileAlfa)
    
    def readFile(self, fileName):
        with open(fileName, "r+") as f:
            fileString = f.read()
            f.close
        return fileString
    
    def save_file(self, msg, id_):
        with open('./results/msgVinegere_'+str(id_)+'.txt', 'w') as f:
            f.write(msg)
            f.close
    
    def getAlfa(self, fileAlfa):
        alfa = self.readFile(fileAlfa).rstrip()
        return alfa
    
    def newChar(self, c, k, alfaLen):
        index = (self.__alfa.index(c) - self.__alfa.index(k)) % alfaLen
        return self.__alfa[index]

    def tryAnalysis(self, fileName, key_):
        if self.validKey(key_):
            key = key_
            cifra = self.readFile(fileName)
            keyLen = len(key)
            alfaLen = len(self.__alfa)
            cifraLen = len(cifra)
            msg = ""
            iter_key = 0
            for i in range(cifraLen):
                if (cifra[i] not in self.__alfa):
                    msg = msg + cifra[i]
                    iter_key = iter_key + 1
                else:
                    msg = msg + self.newChar(cifra[i], key[(i - iter_key) % keyLen], alfaLen)
            self.save_file(msg, 0)
            print("Finished, open the folder results and see the message.")
        else:
            print("The key is not in alphabet")
    
    def validKey(self, key):
        for k in key:
            if k not in self.__alfa:
                return False
        return True

def main():
    fileAlfa = sys.argv[1]
    fileCifra = sys.argv[2]
    key_ = sys.argv[3]
    vigenere = Vigenere(fileAlfa) 
    vigenere.tryAnalysis(fileCifra, key_)

if __name__ == '__main__':
    main()