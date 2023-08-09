import json
import os

class Database:
    currentpath = os.getcwd()
    parentpath = os.path.dirname(currentpath)
    db = {}
    docnum = 1
    def __init__(self):
        with open(self.parentpath + "/data/docinfo.json", "r") as f:
            if (f):
                self.db = json.load(f)
            self.docnum = len(self.db['documents'])+1

    def printDocs(self):
        print("List of your documents: ")
        self.db['documents'] = sorted(self.db['documents'], key=lambda x: x['docnum'])
        for i in range(1, self.docnum):
            for doc in self.db['documents']:
                if (i == doc['docnum']):
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
            print("1. Find longest document (most characters)")
            print("2. Find document with most occurrences of a specific character")
            print("3. Find number of documents")
            print("4. Find average size of document")
            print("5. Return to main menu\n")

            inp = input("Please input the number corresponding to the desired function to be executed:")

            if inp == "1":
                max_characters = 0
                max_name = ""
                for doc in self.db['documents']:
                    path = "./documents/" + doc['name']
                    file = open(path, "r")
                    data = file.read()
                    number_of_characters = len(data)
                    if (max_characters < number_of_characters):
                        max_characters = number_of_characters
                        max_name = doc['name']
                print("Largest file: " + max_name + "\nNumber of characters: " + str(max_characters) + "\n")
                input("Press ENTER to continue")
            elif inp == "2":
                inp = input("Please enter the character you wish to search for occurrences of:")

                max_characters = 0
                max_name = ""
                for doc in self.db['documents']:
                    path = "./documents/" + doc['name']
                    file = open(path, "r")
                    data = file.read()
                    number_of_characters = data.count(inp)
                    if (max_characters < number_of_characters):
                        max_characters = number_of_characters
                        max_name = doc['name']
                print("\nFile with most occurrences of \'" + inp + "\': " + max_name + "\nNumber of \'" + inp + "\'s: " + str(max_characters) + "\n")
                input("Press ENTER to continue")
                print("\n")
            elif inp == "3":
                print("\n")
            elif inp == "4":
                print("\n")
            elif inp == "5":
                print("\n")
                break

    
    def addFile(self, fileName):
        for doc in self.db['documents']:
            if doc['name'] == fileName:
                print("Duplicate file name: " + fileName)
                print("File not added")

        new_entry = {
            "name": fileName,
            "docnum": self.docnum
        }
        self.db['documents'].append(new_entry)

        self.docnum = self.docnum+1

        self.updateJson()


    def deleteFile(self, fileName, docnum):
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
        path = self.parentpath + "/documents/" + fileName
        os.remove(path)
        self.updateJson()
        
    def updateJson(self):
        json_object = json.dumps(self.db, indent=3)
        with open(self.parentpath + "/data/docinfo.json", "w") as f:
            f.write(json_object)
