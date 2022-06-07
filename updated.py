import random
from termcolor import colored
import time
from string import capwords

def name_rev(name_full_):
    # arg1 name_full_ = the full name of the user
    # return name_revers_ = the full name of the user reversed
    name_revers_ = (name_full_[::-1])#reverse the letters of the name
    return name_revers_
def Vowel_counter (name_full_):
    #arg 1 vowel =list of vowels to seach in name full
    #arg 2 Vcounter = number of vowels are in a name
    #return the amount of vowels in a name
    vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")# list of vowels
    A = ("a", "A")#list of a
    E = ("e", "E")#list of e
    I = ("i", "I")#list of i
    O = ("o", "O")#list of o
    U = ("u", "U")#list of u
    Vcounter = 0#counter to add
    for letter in name_full_:
        if letter in vowel:#if there is a letter that is in the vowel list
            Vcounter = Vcounter + 1#add one
    Acounter = 0# counter for a the same prorgram but instead adding a 1 to the counter if it is a specific vowel
    for letter in name_full_:
        if letter in A:
            Acounter = Acounter + 1
    Ecounter = 0
    for letter in name_full_:
        if letter in E:
            Ecounter = Ecounter + 1
    Icounter = 0
    for letter in name_full_:
        if letter in I:
            Icounter = Icounter + 1
    Ocounter = 0
    for letter in name_full_:
        if letter in O:
            Ocounter = Ocounter + 1
    Ucounter = 0
    for letter in name_full_:
        if letter in U:
            Ucounter = Ucounter + 1
    Vowels=(Vcounter,Acounter,Ecounter,Icounter,Ocounter,Ucounter)
    return Vowels
    list_of_names = name_full_.split()
    last_middle_name = len(list_of_names) - 1
    list_of_middle_names = (list_of_names[1:last_middle_name])
    return; list_of_middle_names
def consonant_counter(name_full_):
    consonant = ('b , c , d,  f,  g, h, j, k, l, m ,n ,p, q, r, s, t, v, w, x, z, B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z,')  # list of constants
    Ccounter = 0  # counter for how many constantes there are in a name

    for letter in name_full_:  # for a letter in name_ful
        if letter in consonant:  # if there is a letter that is in the consant list
            Ccounter = Ccounter + 1  # add 1 to Ccounter
    return Ccounter
def frist_name(name_full_):
    fn = ""  # blank verable to and the first name to
    pos = 0  # is the possition of every
    while pos < len(name_full_):  # while the postion is less then the lenth of name_full
        if name_full_[pos] == " ":  # if the chartict in name_full_ based on the possion counter
            break  # break while loop
        else:  # else name_full not space
            fn = fn + name_full_[pos]  # add letter from name_full
        pos = pos + 1  # add 1 to pos counter
    return fn
def middle_name(name_full_):
    list_of_names = name_full_.split()#splits name where the spaces are
    last_middle_name = len(list_of_names) - 1# last middle name is = to the lenth of list of names
    list_of_middle_names = (list_of_names[1:last_middle_name])
    list_of_middle_names.append(" ")#add a space in the list this is for each middle name
    list_of_middle_names.append(" ")
    list_of_middle_names.append(" ")
    list_of_middle_names.append(" ")
    list_of_middle_names.append(" ")
    list_of_middle_names.append(" ")
    return list_of_middle_names
def last_name(name_full_):
    first_letter_of_Last_name = len(name_full_) - 1  # the lenth of the name -1

    while first_letter_of_Last_name >= 0:  # while the first_letter_of_last_name is greater then 0
        if name_full_[first_letter_of_Last_name] == " ":  # if the letter in name full is = space
            break  # break loop
        else:  # else name not = to space
            first_letter_of_Last_name = first_letter_of_Last_name - 1  # subract one
    last_name = (name_full_[first_letter_of_Last_name:len(name_full_)])  # the last name = the frirst letter of the last name and the lenth of the name_full
    return last_name
def hyphin_(name_full_):
    if "-" in name_full_:  # if a - is found in the name_full_
        hyphin=("true")  # print (true)
    else:  # if else
        hyphin=("false")  # print flase
    return hyphin
def boolean_palindrome(name_full_):
    fn=frist_name(name_full_)# first name function
    if fn == (name_full_[::-1]):# if the first name is = to it backwards it is a palindrome
        print("true")
    else:
        print("false")
def intals(name_full_):
    name_list=name_full_.split(" ")#split name were space is
    inta=("")# where intals will go
    for name in name_list:
        inta=inta+name[0].capitalize()+(".")#add the first letter of name capitlized and a .
    return inta
def lowercase_name(name_full_):
    index = 0
    lower_case_names = ""
    while index < len(name_full_):# while index is less then the lenth on name full
        letter_in_name = ord(name_full_[index])# letter name is equal to decmmial value of one of letters from name full
        if letter_in_name >= 65 and letter_in_name <= 90:# if letter is upper case
            letter_in_name = letter_in_name + 32# adds 32 making it upper case
            letter_in_name = chr(letter_in_name)#convert decmaill to letter
            lower_case_names = lower_case_names + letter_in_name# add letter to string
        else:
            lower_case_names = lower_case_names + chr(letter_in_name)#add leter to string
        index += 1
    return lower_case_names
def upper_case_name(name_full_):
    #fuction same accpet instead of adding 32 it subtracts 32
    index2 = 0
    upper_case_name = ""
    while index2 < len(name_full_):
        letter_in_name = ord(name_full_[index2])
        if letter_in_name >= 97 and letter_in_name <= 122:
            letter_in_name = letter_in_name - 32
            letter_in_name = chr(letter_in_name)
            upper_case_name = upper_case_name + letter_in_name
        else:
            upper_case_name = upper_case_name + chr(letter_in_name)
        index2 += 1
    return upper_case_name
def name__random(name_full_):
    name_list=name_full_.split(" ")#split name were space is
    ran_name_lis=[]# where the final names will go
    for name in name_list:# for name in name list
        ran_letter=[]# were letters of each name will go
        for letter in name:#for leter in name
            ran_letter.append(letter)# add the letter to a list
        random.shuffle(ran_letter)# then shuffle siad list
        name=("")# were each name will go
        ran=[]#were the randmi
        for letter in ran_letter:# the random.shuffle only randmizes lists so i have to put the list into a string / for letter in ran letter
            name=name+letter#add letter to name
            ran.append(name)# add name to ran
        ran_name_lis.append(name)# add ran to the final list

    return ran_name_lis;
name_full_ = str(input("what is your full name\n"))  # name of user
print("what do you want from your name please choose from this list")
print(("type"),(colored('1', 'blue')),(" for name reversed"))
time.sleep(.10)
print(("type"),(colored('2', 'blue')),(" for number of vowels"))
time.sleep(.10)
print(("type"),colored('3', 'blue'),(" for number of consonants"))
time.sleep(.10)
print(("type"),colored('4', 'blue'),("for my first name"))
time.sleep(.10)
print(("type"),colored('5', 'blue'),(" for my last name"))
time.sleep(.1)
print(("type"),colored('6', 'blue'),("for my middle name"))
time.sleep(.1)
print(("type"),(colored('7', 'blue')),(" for boolean hyphin"))
time.sleep(.1)
print(("type"),(colored('8', 'blue')),(" for lowercase my name"))
time.sleep(.1)
print(("type"),colored('9', 'blue'),(" for uppercase my name"))
time.sleep(.1)
print(("type"),colored('10', 'blue'),("for my name randomized"))
time.sleep(.1)
print(("type"),colored('11', 'blue'),(" for boolean if palindrome"))
time.sleep(.1)
print(("type"),colored('12', 'blue'),("for intials"))
chocie_for_what_program_to_run = input("type the number corisponing to the function you want")  # asks user what part of the
while chocie_for_what_program_to_run not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
    print("not a vaild answer\ntype either",colored('1,2,3,4,5,6,7,8,9,10,11 or 12','blue'))
    chocie_for_what_program_to_run=input()
# ===============================================================================================================================
if chocie_for_what_program_to_run == ("1"):
    name_rev(name_full_)
    print(name_rev(name_full_))
# -------------------------------------------------------------------------------------------------------------------------
if chocie_for_what_program_to_run == ("2"):
    list_of_Vowel_stuff = (Vowel_counter(name_full_))
    if list_of_Vowel_stuff[0] == 0:
        print("you don't have any vowels in your name ")
    else:
        print("there are", list_of_Vowel_stuff[0], "vowels in your name\nyou have ", list_of_Vowel_stuff[1],
              " a in your name\nyou have ", list_of_Vowel_stuff[2], " e in your name\nyou have ",
              list_of_Vowel_stuff[3], " i in your name\nyou have ", list_of_Vowel_stuff[4],
              " o in your name\nyou have ", list_of_Vowel_stuff[5], " u in your name\n")
# ----------------------------------------------------------------------------------------------------------------------
if chocie_for_what_program_to_run == ("3"):
    number_of_consonamt=consonant_counter(name_full_)
    print("you have",number_of_consonamt,"consonants in your name")
#====================================================================================================================================
if chocie_for_what_program_to_run == ("4"):
    frist_name(name_full_)
    print("Your frist name is ", frist_name(name_full_))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if chocie_for_what_program_to_run == ("5"):
    if len(last_name(name_full_)) < 2:  # if the lenth of the last name is less then 2
        print("You didn't type your last name")
    else:
        print("Your Last name is ", last_name(name_full_))
# ---------------------------------------------------------------------------------------------------------
if chocie_for_what_program_to_run == "6":
        if len(name_full_.split(" ")) < 3:  # while there are only less than three names in the name_full
            print("no middle name was entered")
        else:
            list_of_middle_names = middle_name(name_full_)  # set the function equal to a variable
            first_middle_name = list_of_middle_names[0]  # set a veritable for empty spot in list
            second_middle_name = list_of_middle_names[1]
            third_middle_name = list_of_middle_names[2]
            fourth_middle_name = list_of_middle_names[3]
            five_middle_name = list_of_middle_names[4]
            sixth_middle_name = list_of_middle_names[5]
            Final_list_of_middle_names = "Your middle names are "  # this is were the names will go
            if len(first_middle_name) > 1:  # if the first middle name is greater than one
                Final_list_of_middle_names += (first_middle_name)  # add it to the list
            if len(second_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (second_middle_name)
            if len(third_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (third_middle_name)
            if len(fourth_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (fourth_middle_name)
            if len(five_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (five_middle_name)
            if len(sixth_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (sixth_middle_name)
            print(Final_list_of_middle_names)
# ===========================================================================================================
if chocie_for_what_program_to_run == ("7"):
    hyphin_(name_full_)
    print(hyphin_(name_full_))
#=========================================================================================================
if chocie_for_what_program_to_run == ("8"):
    lowercase_name(name_full_)
    print(lowercase_name(name_full_))
#===============================================================================================
if chocie_for_what_program_to_run == ("9"):
    upper_case_name(name_full_)
    print(upper_case_name(name_full_))
# =================================================================================================
if chocie_for_what_program_to_run == ("10"):
    print(name__random(name_full_))
# ==============================================================================================================
if chocie_for_what_program_to_run == ("11"):
    boolean_palindrome(name_full_)
# =======================================================================================================================================
if chocie_for_what_program_to_run == ("12"):
    intals(name_full_)
    print(intals(name_full_))

#runs program again
print("would you like to run the program again",colored('Yes', 'green'),("or"),colored('No', 'red')) #
user_in=input()
user_in=capwords(user_in)# capitalize
while user_in not in ["Yes", "No"]:# while the users answers is not yes or no
    print("not valid answer type ether yes or no",colored('Yes', 'green'),("or"),colored('No', 'red')) # print not valid answer
    user_in= input()# users input
    user_in = capwords(user_in)#captilize
while user_in=="Yes":#while user anwser continues to be yes run program
    name_full_ = str(input("what is your full name\n"))  # name of user
    print("what do you want from your name please choose from this list")
    print(("type"), (colored('1', 'blue')), (" for name reversed"))
    time.sleep(.25)
    print(("type"), (colored('2', 'blue')), (" for number of vowels"))
    time.sleep(.25)
    print(("type"), colored('3', 'blue'), (" for number of consonants"))
    time.sleep(.25)
    print(("type"), colored('4', 'blue'), ("for my first name"))
    time.sleep(.25)
    print(("type"), colored('5', 'blue'), (" for my last name"))
    time.sleep(.25)
    print(("type"), colored('6', 'blue'), ("for my middle name"))
    time.sleep(.25)
    print(("type"), (colored('7', 'blue')), (" for boolean hyphin"))
    time.sleep(.25)
    print(("type"), (colored('8', 'blue')), (" for lowercase my name"))
    time.sleep(.25)
    print(("type"), colored('9', 'blue'), (" for uppercase my name"))
    time.sleep(.25)
    print(("type"), colored('10', 'blue'), ("for my name randomized"))
    time.sleep(.25)
    print(("type"), colored('11', 'blue'), (" for boolean if palindrome"))
    time.sleep(.25)
    print(("type"), colored('12', 'blue'), ("for intials"))
    chocie_for_what_program_to_run = input(
        "type the number corisponing to the function you want")  # asks user what part of the
    while chocie_for_what_program_to_run not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
        print("not a vaild answer\ntype either", colored('1,2,3,4,5,6,7,8,9,10,11 or 12', 'blue'))
        chocie_for_what_program_to_run = input()
    # ===============================================================================================================================
    if chocie_for_what_program_to_run == ("1"):
        name_rev(name_full_)
        print(name_rev(name_full_))
    # -------------------------------------------------------------------------------------------------------------------------
    if chocie_for_what_program_to_run == ("2"):
        list_of_Vowel_stuff = (Vowel_counter(name_full_))
        if list_of_Vowel_stuff[0] == 0:
            print("you don't have any vowels in your name ")
        else:
            print("there are", list_of_Vowel_stuff[0], "vowels in your name\nyou have ", list_of_Vowel_stuff[1],
                  " a in your name\nyou have ", list_of_Vowel_stuff[2], " e in your name\nyou have ",
                  list_of_Vowel_stuff[3], " i in your name\nyou have ", list_of_Vowel_stuff[4],
                  " o in your name\nyou have ", list_of_Vowel_stuff[5], " u in your name\n")

    # ----------------------------------------------------------------------------------------------------------------------
    if chocie_for_what_program_to_run == ("3"):
        number_of_consonamt = consonant_counter(name_full_)
        print("you have", number_of_consonamt, "consonants in your name")
    # ====================================================================================================================================
    if chocie_for_what_program_to_run == ("4"):
        frist_name(name_full_)
        print("Your frist name is ", frist_name(name_full_))

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    if chocie_for_what_program_to_run == ("5"):
        if len(last_name(name_full_)) < 2:  # if the lenth of the last name is less then 2
            print("You didn't type your last name")
        else:
            print("Your Last name is ", last_name(name_full_))

    # ---------------------------------------------------------------------------------------------------------
    if chocie_for_what_program_to_run == "6":
        if len(name_full_.split(" ")) < 3:  # while there are only less than three names in the name_full
            print("no middle name was entered")
        else:
            list_of_middle_names = middle_name(name_full_)  # set the function equal to a variable
            first_middle_name = list_of_middle_names[0]  # set a veritable for empty spot in list
            second_middle_name = list_of_middle_names[1]
            third_middle_name = list_of_middle_names[2]
            fourth_middle_name = list_of_middle_names[3]
            five_middle_name = list_of_middle_names[4]
            sixth_middle_name = list_of_middle_names[5]
            Final_list_of_middle_names = "Your middle names are "  # this is were the names will go
            if len(first_middle_name) > 1:  # if the first middle name is greater than one
                Final_list_of_middle_names += (first_middle_name)  # add it to the list
            if len(second_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (second_middle_name)
            if len(third_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (third_middle_name)
            if len(fourth_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (fourth_middle_name)
            if len(five_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (five_middle_name)
            if len(sixth_middle_name) > 1:
                Final_list_of_middle_names += (" , ")
                Final_list_of_middle_names += (sixth_middle_name)
            print(Final_list_of_middle_names)
    # ===========================================================================================================
    if chocie_for_what_program_to_run == ("7"):
        hyphin_(name_full_)
        print(hyphin_(name_full_))
    # =========================================================================================================
    if chocie_for_what_program_to_run == ("8"):
        lowercase_name(name_full_)
        print(lowercase_name(name_full_))
    # ===============================================================================================
    if chocie_for_what_program_to_run == ("9"):
        upper_case_name(name_full_)
        print(upper_case_name(name_full_))
    # =================================================================================================
    if chocie_for_what_program_to_run == ("10"):
        print(name__random(name_full_))
    # ==============================================================================================================
    if chocie_for_what_program_to_run == ("11"):
        boolean_palindrome(name_full_)
    # =======================================================================================================================================

    if chocie_for_what_program_to_run == ("12"):
        intals(name_full_)
        print(intals(name_full_))

    print("would you like to run the program again", colored('Yes', 'green'), ("or"), colored('No', 'red'))
    user_in = input()
    user_in = capwords(user_in)
    while user_in not in ["Yes", "No"]:
        print("not valid answer type ether yes or no", colored('Yes', 'green'), ("or"), colored('No', 'red'))
        user_in = input()
        user_in = capwords(user_in)
