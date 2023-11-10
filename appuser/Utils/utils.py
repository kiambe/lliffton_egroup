
import json

import requests
from appuser.Utils import constants
from accounts.models import *

from appuser.models import *
import random
import string
from appuser.models import SelfGeneratedVouchers

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


def saveVoucherToDatabase(code):

    object_ = Voucher(code=code,voucher_issued=True
                       )
    object_.save()
    print("voucher saved")

         


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


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generateRandomInt():
    check = True

    # check if the random rumber is in the database
    while check:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        num4 = random.randint(1, 5)
        num5 = random.randint(1, 7)
        num6 = random.randint(3, 9)
        num7 = random.randint(1, 7)
        num8 = random.randint(2, 9)
        num9 = random.randint(3, 8)
        letter1 = id_generator(size=1)
        letter2 = id_generator(size=1)
        letter3 = id_generator(size=1)

        if num1 == num2 and num2 == num3:
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)
            num3 = random.randint(1, 9)
        if num3 == num4 and num4 == num5:
            num3 = random.randint(1, 9)
            num4 = random.randint(1, 3)
            num5 = random.randint(1, 7)
            letter1 = id_generator(size=1)
            letter2 = id_generator(size=1)
            letter3 = id_generator(size=1)

        number = f"{num3}{num1}{letter2}{num3}{letter3}{num9}{letter1}"

        # number="16924323"
        generated_id_results = SelfGeneratedVouchers.objects.filter(
            ticket_id=number)
        if len(generated_id_results) != 0:
            # check = False
            print(f"Number is already in db {generated_id_results}")
            pass

           
        else:
            data_to_save = SelfGeneratedVouchers(ticket_id=number)
            data_to_save.save()
            print("saved...")
            check = False

    return number


# def checkIFAmountIsNumeric(string)
#     x = string.isnumeric()
#     if x === False:
#         return "Amount is not numeric. Please try again."