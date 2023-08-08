
"""
Shortener of Journal names
Some journals ask that the bibliography entries display shortened journal names. Doing it manually is painful. This code automatises the process.
"""

import urllib.request
import os

# Shortener function
def shorten(input_name, which_if_multiple = -1):

    # Get correct alphabetic url from Web of Science (complete database of journal abbreviations)
    if input_name[0].isnumeric():
        url = "https://images.webofknowledge.com/images/help/WOS/0-9_abrvjt.html"
    elif input_name[0].isalpha():
        url = "https://images.webofknowledge.com/images/help/WOS/"+input_name[0].upper()+"_abrvjt.html"
    else:
        raise Exception("Sorry, unrecognised name") 
        
    # Access the website
    request = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(request)
    except:
        print("something wrong")
    
    htmlBytes = response.read()
    htmlStr = htmlBytes.decode("utf8")
    htmlSplit = htmlStr.split('\n')
    
    # Search for the journal and get its line
    lines = []

    for line in range(len(htmlSplit)):
        if htmlSplit[line].find(input_name.upper()) != -1 and htmlSplit[line].find("<DT>") != -1:  # Only the names line, not already that of abbreviations
            lines.append(line)

    # Handle if the are multiple entries for that journal name
    if lines:
        if which_if_multiple == -1:
            if len(lines) > 1:
                for i in lines:
                    print(htmlSplit[i])
                which_if_multiple = int(input("From the list above, enter the line number of the journal you want to shorten (starting from 1): ")) + 1
            else: which_if_multiple = 0
    else:
        raise Exception("Journal not found, check the name again") 

    # Get the abbreviation
    abbrv_list = htmlSplit[lines[which_if_multiple]+1].split()[1:]
    abbrv = []
    for i in abbrv_list:
        abbrv.append(" ")
        if i == "IEEE":   #exception for IEEE, all uppercase
            abbrv.append(i)
        else:
            abbrv.append(i.title())
    
    return "".join(abbrv)
    

def uniqueAbbr():
    
    # Define input
    a = input('Enter the name of the journal you want to search: ')

    if a.title() == 'Nature': 
        abbreviation = "Nature"
    elif a.title() == 'Science':
        abbreviation = "Science"
    else:
        abbreviation = shorten(a)[1:]

    print(abbreviation)


def fileAbbr():
    # Set path to file and read it

    path_to_file = input('Enter the path to your .txt bibliography file: ')

    with open(path_to_file) as f:
        contents = f.readlines()

    # Find whenever the bib file has a "journal" entry

    lines = []
    for line in range(len(contents)):
            if contents[line].find("journal") != -1:
                lines.append(line)

    # Handle the way that bib files connect the keyword "journal" with the name, and iterate for all the instances
    journals = []
    abbreviations = []
    for line in lines:
        journalNameList = contents[line].split()
        
        adf = -1
        for i in range(len(journalNameList)):
            if journalNameList[i].find("=") == 0:          adf = 1
            if journalNameList[i].find("journal=") == 0:   adf = 2
            if journalNameList[i].find("journal={") == 0:  adf = 3
            if journalNameList[i].find("journal=\"") == 0: adf = 4
        
        # Crop the name of the journal
        if adf == 1:
            b = journalNameList[2:]
            b[0] = b[0][1:]; b[-1] = b[-1][:-2]
        elif adf == 2:
            b = journalNameList[2:]
            b[0] = b[0][1:]; b[-1] = b[-1][:-2]
        elif adf == 3:
            b = [i.split('={', 1)[-1] for i in journalNameList]
            b[-1] = b[-1][:-2]
        elif adf == 4:
            b = [i.split('=\"', 1)[-1] for i in journalNameList]
            b[-1] = b[-1][:-2]
        else: raise Exception("Journal line not found, check your bibliography file") 
            
        jName = []
        for i in b:
                jName.append(i)
                jName.append(" ")
        journal = "".join(jName[:-1])
        journals.append(journal)
        
        # Handle a few exceptions, and call the shorten routine
        if journal.upper() == 'NATURE': 
            abbreviation = "Nature"
        elif journal.upper() == 'NATURE':
            abbreviation = "Science"
        elif journal.upper() == 'ARXIV':
            abbreviation = "arXiv"
        elif journal.upper() == 'MEDRXIV':
            abbreviation = "medRxiv"
        elif journal.upper() == 'BIORXIV':
            abbreviation = "bioRxiv"
        else:
            abbreviation = shorten(journal)[1:]
        abbreviations.append(abbreviation)
            

    # Write a new bib file with shorthened journal names

    with open(path_to_file) as f:
        filedata = f.read()
    for i in range(len(journals)):
        filedata = filedata.replace(journals[i],abbreviations[i])
    fi = open(os.path.join(os.path.dirname(path_to_file),"shortBib.txt"),'w')
    fi.write(filedata)
    fi.close()



###### Main 

choice = input("Do you want to search for a unique journal abbreviation [1] or to edit a whole file [2]? ")
if choice == "1":
    uniqueAbbr()
elif choice == "2":
    fileAbbr()
