import json

class Database:

    db = {}
    def __init__(self):
        with open("./data/docinfo.json") as f:
            self.db = json.load(f)

    def printDocs(self):
        i=0
        print("List of your documents: ")
        for doc in self.db['documents']:
            s = str(i) + ". " + doc["name"]
            i = i+1
            print(s)

    def getDoc(self):
        print("Please type the number of the document you want to access")
        choice = int(input())
        #if choice > self.db['documents'].length:
        #    print("Invalid Input")
        #    return

        for doc in self.db['documents']:
            if choice == doc['docnumber']:
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

            inp = input("Please input the number corresponding to the desired function to be executed:\n")

            if inp == "1":
                print("\n")
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
                inp = input("Please enter the character you wish to search for occurrences of:\n")

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
                print("File with most occurrences of \'" + inp + "\': " + max_name + "\nNumber of \'" + inp + "\'s: " + str(max_characters) + "\n")
                input("Press ENTER to continue")
                print("\n")
            elif inp == "3":
                print("\n")
            elif inp == "4":
                print("\n")
            elif inp == "5":
                print("\n")
                break




    

            
        