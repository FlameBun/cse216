from pyTPS_Transaction import pyTPS_Transaction

class pyTPS:
    def __init__(self):
        self.transactions = []
        self.mostRecentTransaction = -1
        self.performingDo = False
        self.performingUndo = False
        
    def isPerformingDo(self):
        return self.performingDo
        
    def isPerformingUndo(self):
        return self.performingUndo
        
    def hasTransactionToRedo(self):
        return self.mostRecentTransaction < self.getSize() - 1
        
    def hasTransactionToUndo(self):
        return self.mostRecentTransaction > -1
    
    def getSize(self):
        return len(self.transactions)
    
    def getRedoSize(self):
        return self.getSize() - self.mostRecentTransaction - 1
        
    def getUndoSize(self):
        return self.mostRecentTransaction + 1

    def addTransaction(self, transaction):
        while self.hasTransactionToRedo():
            self.transactions.pop(self.getSize() - 1)

        self.transactions.append(transaction)
        self.doTransaction()

    def doTransaction(self):
        if self.hasTransactionToRedo():
            self.performingDo = True
            self.mostRecentTransaction += 1
            transaction = self.transactions[self.mostRecentTransaction]
            transaction.doTransaction()
            self.performingDo = False
    
    def undoTransaction(self):
        if self.hasTransactionToUndo():
            self.performingUndo = True
            transaction = self.transactions[self.mostRecentTransaction]
            transaction.undoTransaction()
            self.mostRecentTransaction -= 1
            self.performingUndo = False

    def clearAllTransactions(self):
        self.transactions = []
        self.mostRecentTransaction = -1

    def __str__(self):
        return "TPS Description"
