from database import *
from documentMenu import *
from importjsonDoc import *
from LoginMenu import *

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
documentpath = parentpath + "/documents/"

def printMenu(user):
    global db
    db = Database(user)
    while (True):
        print("----------")
        print("Main Menu:")
        print("----------")
        print("1. open document")
        print("2. upload document")
        print("3. delete document")
        print("4. sort documents")
        print("5. list documents")
        print("6. pin document")
        print("7. Query Database")
        print("8. Logout\n")
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            print("\n")
            openDocument()
        elif inp == "2":
            print("\n")
            uploadDoc()
        elif inp == "3":
            print("\n")
            deleteDocument()
        elif inp == "4":
            print("\n")
            sortDocuments()
        elif inp == "5":
            print("\n")
            listDocuments()
        elif inp == "6":
            print("\n")
            pinDocument()
        elif inp == "7":
            print("\n")
            getDatabaseStats()
        elif inp == "8":
            return
        else:
            print("Unknown input. Please try again.\n")

def openDocument():
    db.printDocs()
    print("Please type the number of the document you want to open")
    choice = int(input())
    filepath = db.getDoc(choice)['name'] #docinfo is the json entry of the document in docinfo.json
    # removed parenth path 
    printDocumentMenu(filepath, choice)
    
def uploadDoc():
    flag = 0
    while(True):
        if(flag == 1):
            break
        print("1. Return to Main Menu")
        srcPath = input("Input file you want to upload: ")
        split = os.path.splitext(srcPath)
        
        if(os.path.isfile(srcPath) or split[1] == '.json' or split[1] == '.csv'):
            print("\n")
            while(True):
                print("1. Return to Main Menu")
                print("2. Change file you want to upload\n")
                print("Uploading file to: " + documentpath + "\n")
                destPath = input("File name: ")
                split1 = os.path.splitext(documentpath + destPath)
                
                if(os.path.isfile(documentpath + destPath) or os.path.isfile(documentpath + destPath + '.json')):
                    print("File already exists")
                elif(destPath == "1"):
                    return
                elif(destPath == "2"):
                    break
                # elif(os.path.isdir(destPath)):
                #     print("Directory exists, need filename\n")
                elif(len(split1[1]) == 0):
                    flag = 1
                    break
                elif(split1[1] != '.json'):
                    print("Invalid file extension\n")
                elif(not destPath):
                    print("Invalid Input\n")
                else:
                    flag = 1
                    break
        elif(srcPath == "1"):
            return
        else:
            print("File does not exist or Invalid input\n")
        

    
    if(split[1] == '.json' and not validateJSON(srcPath)):
        print("Inavlid json file")
        return
    else:
        # The uploadDocument function calls convertToJson function
        uploadDocument(srcPath, documentpath + destPath) 
        split1 = os.path.splitext(destPath)
        if(split1[1] == ''):
            destPath += '.json'
        db.addFile(destPath)
        print("Uploaded document")

def deleteDocument():
    db.printDocs()
    print("Please type the number of the document you want to delete")
    choice = int(input())
    db.deleteFile(fileName = "", docnum=choice, flag = 0)

def sortDocuments():
    db.printDocs()
    print("sort documents")

def listDocuments():
    db.printDocs()
    input("Press Enter to continue.")

def pinDocument():
    db.printDocs()
    print("Please type the number of the document you want to pin")
    choice = int(input())
    db.pinDoc(db.getDoc(choice)['name'])

def getDatabaseStats():
    db.printDBMenu()

def userInput():
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    if inp == "1":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "2":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "3":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "4":
        print("\n")
        temporaryFeatureMenu()
    else:
        print("Unknown input. Please try again.\n")
        userInput()
        
def temporaryFeatureMenu():
    print("------------------------")
    print("Respective Feature Menu:")
    print("------------------------")
    print("1. return to main menu\n")
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    if inp == "1":
        print("\n")
        printMenu()
    else:
        print("Unknown input. Please try again.\n")
        temporaryFeatureMenu()
        printMenu()
