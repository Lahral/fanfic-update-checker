import csv
import requests
import re

fanficList = []

keys=('NAME','FIC ID','CHAPTER','AUTH', 'LAST UPDATE')

def readFile(filename, length):
    """reads out the list of fanfics from a CSV file.
    returns amount of lines read in."""
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, fieldnames=keys)
        next(reader)
        for row in reader:
            fanficList.append(row)
            length += 1

    csv_file.close()


def writeFile(filename):
    """writes out the list of fanfics to a CSV file."""
    with open(filename, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(fanficList)
    csv_file.close()

def check(fanfic):
    """Takes in the fanfiction.net story ID and chapter number.
    returns -1 if error, 0 if no update, 1 if update"""
    RegEx = "- Updated:\s*<span data-xutime='(\d{9,})'>"
    dead = "<span class='gui_warning'>Story Not Found"

    req = requests.get('https://www.fanfiction.net/s/' +
                       str(fanfic['FIC ID']) + '/' + str(fanfic['CHAPTER']))

    # checking to see if the fic still exists:
    if re.findall(dead,req.text):
        return -1
    # using RegEx to determine when a fanfic has been updated.
    # checking the updated mark against the old updated time
    xutime = re.findall(RegEx, req.text)
    if xutime:
        
        lastUpdate = xutime[0]

        if int(lastUpdate) > int(fanfic['LAST UPDATE']):
            fanfic['LAST UPDATE'] = lastUpdate
            fanfic['CHAPTER'] = int(fanfic['CHAPTER']) + 1
            return 1

    return 0

def main():
    """The main function that triggers all the others. Reads in a .csv file
    ficList that is in the same directory, and checks for updates. Check
    keys to see the order for content placement in ficList.csv"""
    length = 0
    if len(fanficList) > 0:
        pass
    else:
        readFile('ficList.csv',length)
    for fic in fanficList:
        status = check(fic)
        if status == -1:
            print(fic['NAME'] + ': is pining for the fjords.\n' +
                  'Check author at https://www.fanfiction.net/u/' + fic['AUTH'])
        elif status == 0:
            print(fic['NAME'] + ': no updates.')
        elif status == 1:
            print(fic['NAME'] + ': has been updated.')
    writeFile('ficList.csv')


main()