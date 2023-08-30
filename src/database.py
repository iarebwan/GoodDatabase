import json
import os

class Database:
    currentpath = os.getcwd()
    parentpath = os.path.dirname(currentpath)
    documentpath = parentpath + "/documents/"
    db = {}
    docnum = 1
    pinnedDocs = []
    def __init__(self, username):
        filepath = self.parentpath + "/data/docinfo" + username + ".json"
        if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
            with open(filepath, "r") as f:
                if (f):
                    self.db = json.load(f)
                self.docnum = len(self.db['documents'])+1
                for doc in self.db['documents']:
                    if 'pinned' in doc and doc['pinned']:
                        self.pinnedDocs.append(doc['name'])
        else:
            payload = {
                "documents": []
            }
            self.db = payload

    def printDocs(self):
        print("List of your documents: ")
        self.db['documents'] = sorted(self.db['documents'], key=lambda x: x['docnum'])

        for i in range(1, self.docnum):
            for doc in self.db['documents']:
                if (i == doc['docnum'] and doc['pinned'] == 1):
                    print("Pinned: " + str(doc['docnum']) + ". " + doc['name'])

        for i in range(1, self.docnum):
            for doc in self.db['documents']:
                if (i == doc['docnum'] and doc['pinned'] == 0):
                    print(str(doc['docnum']) + ". " + doc['name'])
        print("\n")


    def getDoc(self, choice):
        if choice > self.docnum-1:
            print("Invalid Input")
            return -1

        for doc in self.db['documents']:
            if choice == doc['docnum']:
                return doc
            
    def printDBMenu(self):        
        while (True):
            print("--------------")
            print("Query Options:")
            print("--------------")
            print("1. Find JSON file by name")
            print("2. Find longest document (most characters)")
            print("3. Find document with most occurrences of a word")
            print("4. Find number of documents")
            print("5. Find average file size of document")
            print("6. Find average word count")
            print("7. Return to main menu\n")

            inp = input("Please input the number corresponding to the desired function to be executed:")
            if inp == "1":
                tempval = 0
                choice = str(input("File Name: "))
                for doc in self.db['documents']:
                    if choice == doc['name']:
                        tempval+=1
                        print("\nDocument found. Doc Num is", doc['docnum'], "\n")
                if tempval == 0:
                    print("\nDocument not found\n")
            elif inp == "2":
                max_characters = 0
                max_name = ""
                for doc in self.db['documents']:
                    path = self.documentpath + doc['name']
                    file = open(path, "r")
                    data = file.read()
                    number_of_characters = len(data)
                    if (max_characters < number_of_characters):
                        max_characters = number_of_characters
                        max_name = doc['name']
                print("Largest file: " + max_name + "\nNumber of characters: " + str(max_characters) + "\n")
                input("Press ENTER to continue")
            elif inp == "3":
                choice = str(input("Please enter the words you wish to search for occurrences of:"))

                max_characters = 0
                max_name = ""
                for doc in self.db['documents']:
                    path = self.documentpath + doc['name']
                    file = open(path, "r")
                    data = file.read()
                    number_of_characters = data.count(choice)
                    if (max_characters < number_of_characters):
                        max_characters = number_of_characters
                        max_name = doc['name']
                print("\nFile with most occurrences of \'" + choice + "\': " + max_name + "\nNumber of \'" + choice + "\'s: " + str(max_characters) + "\n")
                input("Press ENTER to continue")
                print("\n")
            elif inp == "4":
                print("\nNumber of Documents in the database: " + str(len(self.db['documents'])))
                print("\n")
            elif inp == "5":
                averagefileSize = 0
                for doc in self.db['documents']:
                    path = self.documentpath + doc['name']
                    averagefileSize += os.path.getsize(path)
                
                averagefileSize /= len(self.db['documents'])
                print("\nAverage file size among documents is: " + str(averagefileSize) + " bytes.")
                
                print("\n")
            elif inp == "7":
                print("\n")
                break
            elif inp == "6":
                overallwordCount = 0
                for doc in self.db['documents']:
                    path = self.documentpath + doc['name']
                    file = open(path, "r")
                    data = file.read()
                    lines = data.split()
                    overallwordCount += len(lines)
                
                overallwordCount /= len(self.db['documents'])
                print("\nAverage word count among documents is: " + str(overallwordCount))
                
                print("\n")

    def pinDoc(self, fileName):
        self.pinnedDocs.append(fileName)
        for doc in self.db['documents']:
            if doc['name'] == fileName:
                doc['pinned'] = 1
        self.updateJson()

    
    def addFile(self, fileName):
        for doc in self.db['documents']:
            if doc['name'] == fileName:
                print("Duplicate file name: " + fileName)
                print("File not added")
                return

        new_entry = {
            "name": fileName,
            "docnum": self.docnum,
            "pinned": 0
        }
        self.db['documents'].append(new_entry)

        self.docnum = self.docnum+1

        self.updateJson()

    def deleteFile(self, fileName, docnum, flag):
        #delete file
        deletenum = self.docnum
        if docnum == -1:
            for i in range (self.docnum-1):
                if self.db['documents'][i]['name'] == fileName:
                    deletenum = self.db['documents'][i]['docnum']
                    del self.db['documents'][i]
                    break
        else:
            for i in range (self.docnum-1):
                if self.db['documents'][i]['docnum'] == docnum:
                    deletenum = self.db['documents'][i]['docnum']
                    fileName = self.db['documents'][i]['name']
                    del self.db['documents'][i]
                    break
        
        #decrement all docnums greater

        for doc in self.db['documents']:     
            if doc['docnum'] > deletenum:
                doc['docnum'] = doc['docnum']-1       
        #decrement docnum
        self.docnum = self.docnum-1
        path = self.documentpath + fileName
        if flag == 0:
            os.remove(path)
        self.updateJson()
        
    def updateJson(self):
        json_object = json.dumps(self.db, indent=3)
        with open(self.parentpath + "/data/docinfo.json", "w") as f:
            f.write(json_object)
