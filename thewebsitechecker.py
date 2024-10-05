import json
import os
import requests
from blocksi_dict import blocksipolicies
from color_lib import cprint

blockers = ['blocksi']

websitetocheck = input("\033[93m{}\033[00m".format("enter a website to check: "))
websitetocheck = str(websitetocheck)

def blocksi_check(website):
    # payload for later
    def checkCatNum(category_number):
        with open("blocksi_category.json", "r") as file:
            data = json.load(file)

        for category in data["categories"]:
            if category["mainCategoryNumber"] == category_number // 100:
                # now we do main name and main num
                mainCatName = category['mainCategoryName']
                mainCatNum = category["mainCategoryNumber"]

                for subcategory in category["subcategories"]:
                    if subcategory["subcategoryNumber"] == category_number:
                        # now we do sub name and desc
                        subCatName = subcategory['subCategoryName']
                        subCatDesc = subcategory['description']
                        # create array
                        allBlocksiInfo = [mainCatName, mainCatNum, subCatName, subCatNum, subCatDesc]
                        return allBlocksiInfo
        # should not have reached this stage, report false.
        print('weird error occured.') # i know good error reporting right right
        return False

    # first, we define all category stuff
    mainCatName = None
    mainCatNum = None
    subCatName = None
    subCatNum = None
    subCatDesc = None

    try:
        findCatNum = requests.get('https://service1.blocksi.net/getRating.json?url=' + website)
        catNumAnswer = findCatNum.json()
        if catNumAnswer == None:
            return "None"
        else:
            catNum = catNumAnswer['Category'] 
            # add subcatnum
            subCatNum = catNum
            catNumInfo = checkCatNum(catNum)
            if catNumInfo == False:
                return False
            else:
                return catNumInfo
    except Exception as error:
        # print(error)
        return False

def resultprocessor(website):
    # we store results in an array within a dictionary.
    # for example {'blocksi': array_here, 'lightspeed': array_here}
    # blocksi check
    # return is [mainCatName, mainCatNum, subCatName, subCatNum, subCatDesc]
    # even if one of them is empty, it will still contain "None"(this should never happen)
    blocksiCollect = blocksi_check(website)
    if blocksiCollect == False:
        print(cprint['red'] + 'fetching to blocksi failed. womp womp')
    elif blocksiCollect == "None":
        # this should never happen
        print('no info')

    # compile to dictionary
    blockerDict = dict()
    for count in range(0, len(blockers)):
        currentArrow = blockers[count]
        blockerDict.update({currentArrow: locals()[f"{currentArrow}Collect"]})
    return blockerDict

def resultcollection(website):
    resultDict = resultprocessor(website)
    # we now process the blocksi output
    blocksiArray = resultDict['blocksi']
    def blocksiBlockPossibilityWrapper():
        blocksiBlockPossibility = blocksipolicies[blocksiArray[3]]
        if blocksiBlockPossibility == 1:
            return cprint['red'] + 'Possibly Blocked'
        else:
            return cprint['green'] + 'Possibly Unblocked'
    divider = cprint['cyan'] + '-----------------------------'
    print(divider)##############
    print(cprint['yellow'] + f'website you looked up: {websitetocheck}')
    print(divider)##############
    print(cprint['lblue'] + 'Information on this website.')
    print(divider)##############
    print(cprint['lpurple'] + 'Blocksi Results')
    print(cprint['yellow'] + 'Category: ' + cprint['green'] + blocksiArray[2])
    print(cprint['yellow'] + f'Blockage Possibility: {blocksiBlockPossibilityWrapper()}')
    print(cprint['green2'] + f'Blocksi Category Number: {blocksiArray[3]}')
    print(divider)
    print(cprint['white'] + cprint['italic']+ "v0.1, made by appleflyer")

    
resultcollection(websitetocheck)
