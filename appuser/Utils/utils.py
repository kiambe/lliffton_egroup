
import json

import requests
from appuser.Utils import constants
from appuser.models import Sessions


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }

def listToString(s):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


def replaceEstericWithSpace(string):
    value = string.replace("*", " ")

    return value


def replaceCommaWithConcat(string):
    value = string.replace(",", "")

    return value


def replaceSpaceWithEstaric(string):
    string = listToString(string)
    print(f"string {string}")
    value = string.replace(" ", "*")

    return value


def replaceCommaSpace(string):
    value = string.replace(",", " ")

    return value


def goToMain(text):
    text = replaceEstericWithSpace(text)
    print(f"text  {text.split()}")
    text = text.split()

    if(len(text) != 1):
        # loop over text to see if back_main_digit exists
        while constants.BACK_MAIN_DIGIT in text:
            # get the index of the back_main_digit in the text
            firstIndex = text.index(constants.BACK_MAIN_DIGIT)

            # remove all the texts before the  back_digit
            text = text[firstIndex+1:]

        # text=listToString(text)
        print(f"REMOVED back main digit from text and text is {text}")

    return replaceSpaceWithEstaric(text)


def goToBack(text):

    text = replaceSpaceFromText(text)  # Added recent 6th Feb
    text = replaceEstericWithSpace(text)
    print(f"text  {text.split()}")
    text = text.split()

    if(len(text) != 1):

        # loop over text to see if back_main_digit exists
        while constants.BACK_DIGIT in text:

            # get the index of the back_main_digit in the text
            firstIndex = text.index(constants.BACK_DIGIT)

            # get the index of the previous_ndex in the text
            firstIndex_minus_1 = firstIndex-1
            print(
                f"index is {firstIndex}, previous digit is {firstIndex_minus_1} n text is {text}")

            del text[firstIndex]
            del text[firstIndex_minus_1]

        print(f"text23 {text}")

    return replaceSpaceWithEstaric(text)


def removeUnwantedTexts(text, array, position_in_text):

    text = replaceSpaceFromText(text)  # Added recent 6th Feb
    text = replaceEstericWithSpace(text)
    print(
        f"Removing texts in position {position_in_text} ---- {text.split()} --- against {array}")
    text = text.split()

    # while len(text) >0:
    # print("-----")
    if len(text) > position_in_text:
        while len(text) != position_in_text:
            if text[position_in_text] not in array:

                del text[position_in_text]

                # text=text[1:]
            else:
                break

            print(f"removing texts, text is now {text}")

    return replaceSpaceWithEstaric(text)


def removeGoBackText(custom_text):
    print(f"array for custom text {custom_text}")
    my_list = []
    if len(custom_text) > 1:
        for id, x in enumerate(custom_text):
            print(f"ran loop {id} tines")
            if x == '0' and '0' in custom_text:
                index = custom_text.index('0')
                index2 = index-1
                print("removing ---------")
                del custom_text[index]
                del custom_text[index2]
            else:
                print(f"notinghere {custom_text} and x is {x}")

        return custom_text


def replaceSpaceFromText(string):
    value = string.replace(" ", "")

    return value


def saveSessionsToDatabase(phoneNumber, sessionNumber, text, response):

    session = Sessions(phoneNumber=phoneNumber,
                       sessionNumber=sessionNumber, text=text, response=response)
    session.save()
    print("Session saved")


            


def checkInstanceIsInt(val):
    try:
        print("trying")
        val = int(val)
        val = isinstance(val, str)
        return val

    except:
        print("error")
        return True



def getRealIDForRepID(array, rep_id, key1="rep_id", key2="id"):

    real_id = None

    for x in array:
        if str(x[key1]) == str(rep_id):
            real_id = x[key2]

    return real_id
