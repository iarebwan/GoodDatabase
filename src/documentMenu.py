import json
import csv
from importjsonDoc import *
from tkinter import *
from DocumentStat import *

def printDocumentMenu(filepath, choice):
    while(True):
        print("--------------")
        print("Document Menu:")
        print("--------------")
        print("1. edit document")
        print("2. convert document")
        print("3. retrieve document statistics")
        print("4. return to main menu\n")
        # print(filepath)
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            print("\n")
            editDocument(filepath)
        elif inp == "2":
            print("\n")
            convertDocument(filepath, choice)
            break
        elif inp == "3":
            print("\n")
            getDocumentStatistics(filepath)
        elif inp == "4":
            print("\n")
            break
        else:
            print("Unknown input. Please try again.\n")


def editDocument(filepath):
    #set up window
    texteditor = Tk()
    texteditor.geometry("400x400")
    texteditor.title("Text Editor")
    scrollbar = Scrollbar(texteditor)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    text = Text(texteditor, yscrollcommand=scrollbar.set)
    text.pack(fill=BOTH)
    scrollbar.config(command=text.yview)
    
    #set up file
    def open_file():
        textfile = open(documentpath + filepath, 'r')
        content = textfile.read()
        text.insert(END, content)
        textfile.close()
    #save file
    def save_file():
        textfile = open(documentpath + filepath, 'w')
        textfile.write(text.get(1.0, END))
        textfile.close()
    #set up buttons
    mymenu = Menu(texteditor)
    texteditor.config(menu=mymenu)
    filemenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Load File", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    
    open_file()
    texteditor.mainloop()

    

def convertDocument(filepath, choice):
    print("1. Convert CSV to JSON")
    print("2. Convert JSON to CSV\n")

    inp = input("Please input the number corresponding to the desired function to be executed:\n")
            
    if(inp == '1'):
        convertToJson(documentpath + filepath, documentpath + filepath)
    elif(inp == '2'):
        downloadDocument(documentpath + filepath, filepath, choice)
    else:
        print("Unknown input, please try again.\n")
        convertDocument(documentpath + filepath)

def getDocumentStatistics(filepath):
    populateDataStat(documentpath + filepath)
