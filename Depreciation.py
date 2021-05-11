#!/user/bin/env python3
#Depreciation by - Zach Palmer
#main file


import locale
from Asset import Asset

def getChoice(prompt):
    goodVal = False
    while not goodVal:
        try:
            choice = str(input(prompt)).upper()
            if choice == "Y" or choice == "N":
                goodVal = True
            else:
                goodVal = False
        except ValueError:
            print("Illegal Input: Please Enter 'Y' for yes or 'N' for No")
            goodVal = False
    return choice

def calcDepreciation():
    assetCost = getValue("Asset Cost : ",'f')
    salvageVal = getValue("Salvage Value : ",'f')
    years = getValue("Life (years) : ",'i')

    Dval = Asset(assetCost,salvageVal,years)
    if Dval.isValid():
        print(f"That asset will have an annual depreciation of : %s" %locale.currency(Dval.getDepreciationValue(),grouping=True))
        schedule = input("Full Schedule? (Y/N) : ")
        if len(schedule) > 0 and schedule[0].upper() == "Y":
            print("Year      Start Value      Depreciation      End Value ")
            for i in range(1,Dval.getLife()+1):
                print("{:3}".format(i)
                      + "{:17,.2f} {:17,.2f} {:16,.2f}".format(Dval.getStartBalance(i),Dval.getDepreciationValue(),Dval.getEndBalance(i)))
    else:
        print(f"Asset Error : {Dval.getErrorMsg()}")
        

def getValue(prompt, valType):
    #valType: 'i' = int 'f' = float
    goodVal = False
    while not goodVal:
        try:
            if valType.lower() == 'i':
                value = int(input(prompt))
                goodVal = True
            elif valType.lower() == 'f':
                value = float(input(prompt))
                goodVal = True
            else:
                goodVal = False
        except ValueError as ex:
            print(f"Illegal Value: {ex} ")
            goodVal = False
    return value


            
    

def main():
    result = locale.setlocale(locale.LC_ALL,'')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.Lc_ALL,'en_US')

    print("Welcome to the Depreciation Calculator")
    choice = getChoice("Do you have an asset? (Y/N): ")
    while choice != "N":
        try:
            if choice == "Y":
                calcDepreciation()
            else:
                print("Operation Unkown")
        except ValueError as DataErrMsg:
            print(f"Data Error: {DataErrMsg}")
        except Exception as GenErrMsg:
            print(f"General Error: {GenErrMsg}")

        choice = getChoice("Do you have another asset? (Y/N) : ")
        print()
    print("Thanks for using The Depreciation Calculator")


if __name__ == "__main__":
    main()
    
            
