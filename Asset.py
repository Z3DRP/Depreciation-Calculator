#!/user/bin/env python3
#Asset class .. by - Zach Palmer
#Supporting file for Depreciation.py


class Asset:
    """Asset Logic For Depreciation Calculator"""
    def __init__(self,asset=0.0,sVal=0.0,life=0):
        self.setAssetCost(asset)
        self.setSalvageValue(sVal)
        self.setLife(life)
        self._Error = "Input Error: Could Not Calculate Depreciation"
        self._DepreciationValue = 0
        if self.isValid():
            self.CalcDepreciationValue()

    def setAssetCost(self,amount):
        self._AssetCost = amount
    def getAssetCost(self):
        return self._AssetCost

    def setSalvageValue(self,sval):
        self._SalvageValue = sval
    def getSalvageValue(self):
        return self._SalvageValue

    def setLife(self,life):
        self._Life = life
    def getLife(self):
        return self._Life

    def isValid(self):
        valid = True
        if self._AssetCost <= 0:
            raise Exception("Asset Cost must be positive")
            valid = False
        elif self._SalvageValue < 0:
            raise Exception("Salvage Value must be positive")
            valid = False
        elif self._SalvageValue >= self._AssetCost:
            raise Exception("Salvage Value must be less than Asset Cost")
            valid = False
        elif self._Life <= 0:
            raise Exception("Life of Asset in years must be positive")
        return valid

    def getErrorMsg(self):
        return self._Error

    def CalcDepreciationValue(self):
        self._StartBalance = [0] * self._Life
        self._EndBalance = [0] * self._Life
        self._DepreciationValue = (self._AssetCost - self._SalvageValue) / self._Life
        self._StartBalance[0] = self._AssetCost
        self._EndBalance[0] = self._AssetCost - self._DepreciationValue

        for i in range(0,self._Life):
            if i > 0:
                self._StartBalance[i] = self._EndBalance[i-1]
                self._EndBalance[i] = self._StartBalance[i] - self._DepreciationValue

    def getDepreciationValue(self):
        return self._DepreciationValue
                
    def getStartBalance(self,year):
        if year < 0:
            raise Exception("Year must be a positive number")
        else:
            return self._StartBalance[year-1]

    def getEndBalance(self,year):
        if year < 0:
            raise Exception("Year must be a positive number")
        else:
            return self._EndBalance[year-1]
                
        
















        
