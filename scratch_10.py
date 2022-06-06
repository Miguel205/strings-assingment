import random
from termcolor import colored
import time

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

def name__random(name_full_):
    fn = ""
    pos = 0
    while pos < len(name_full_):# while pos is less then the lenght of name full
        if name_full_[pos] == " ":# if name full 
            break
        else:
            fn = fn + name_full_[pos]#add the letter to the fisrt name
        pos = pos + 1# add 1 to pos

    list_of_letters = list(fn)
    (random.shuffle(list_of_letters))

    index = 0
    lower_case_names = ""
    while index < len(list_of_letters):
        letter_in_name = ord(list_of_letters[index])
        if letter_in_name >= 65 and letter_in_name <= 90:
            letter_in_name = letter_in_name + 32
            letter_in_name = chr(letter_in_name)
            lower_case_names = lower_case_names + letter_in_name
        else:
            lower_case_names = lower_case_names + chr(letter_in_name)
        index += 1

    # =======================================================

    middle_name_counter = ""  # by the end fo the while loop middle_name_counter_= frist name

    new_pos = 0  # number location of the space after the frist name

    while new_pos < len(
            name_full_):  # while new pos (number location of the space after the frist name ) is less then the amount of the number of letters in your full name (name full)
        if name_full_[new_pos] == " ":  # if name_full and new postion(counter) are equal break the while loop
            break
        else:
            new_pos = new_pos + 1

    # middle_name_counter2=0 #
    # pos_of_last_letter_of_middle_name=0

    middle_name_finder2 = len(name_full_) - 1  # position of pointer

    while middle_name_finder2 >= 0:
        if name_full_[middle_name_finder2] == " ":
            break
        middle_name_finder2 = middle_name_finder2 - 1

    if 1 == 1:
        middle = (name_full_[new_pos:middle_name_finder2])
        if len(middle) < 2:
            print("no you don't")
        else:
            first_middle_name_space = ""
            pos = 0
            while pos < len(middle):
                if middle[pos] == " ":
                    break
                else:
                    first_middle_name = first_middle_name_space + name_full_[pos]
                pos = pos + 1
    else:
        print("not a valid answer")

    middle = (name_full_[new_pos:middle_name_finder2])
    if len(middle) < 2:
        print("no you don't")
    else:
        first_middle_name_space = ""
        pos = 0
        space_remover = 0
        while pos < len(middle):
            if middle[pos] == " ":
                pos += 1
                space_remover += 1
            else:

                break

    if len(middle) > 1:
        space_remover = 0
        space_remover_nxt = 0
        while middle[space_remover] == " ":
            space_remover_nxt += 1
            space_remover += 1
        middle2 = middle[space_remover:len(middle)]
        x = middle2.split()

    first_middle_name_with_space = x[0]
    second_middle_name_with_space = x[1]

    # end of space remover for the first name

    pos_remover_4_1 = 0  # the frist letter of the frist middle name without a space in front
    while pos_remover_4_1 < len(
            first_middle_name_with_space):  # while the pos_remover_4_1 is less then the length of the frist middle name with space
        if first_middle_name_with_space[
            pos_remover_4_1] == " ":  # if the frist_middle_name_with_space has a space in it
            pos_remover_4_1 += 1  # add 1 to the pos_remover_4_1
        else:
            break  # if not space break the loop

    pos_remover_4_2 = 0  # the first letter of the second middle name without a space in front
    while pos_remover_4_2 < len(
            second_middle_name_with_space):  # while the pos_remover_4_2 is less then the length of the second middle name with space
        if second_middle_name_with_space[
            pos_remover_4_2] == " ":  # if the second_middle_name_with_space has a space in it
            pos_remover_4_2 += 1  # add 1 to the pos_remover_4_2
        else:
            break  # if not space break the loop

    first_middle_name_with_out_space = (first_middle_name_with_space[pos_remover_4_1:len(
        first_middle_name_with_space)])  # the frist middle name with no spaces
    second_middle_name_with_out_space = (second_middle_name_with_space[pos_remover_4_2:len(
        second_middle_name_with_space)])  # the frist middle name with no spaces

    list_of_letters = list(first_middle_name_with_out_space)
    (random.shuffle(list_of_letters))

    index46 = 0
    lower_case_names3 = ""
    while index46 < len(list_of_letters):
        letter_in_name = ord(list_of_letters[index46])
        if letter_in_name >= 65 and letter_in_name <= 90:
            letter_in_name = letter_in_name + 32
            letter_in_name = chr(letter_in_name)
            lower_case_names3 = lower_case_names3 + letter_in_name
        else:
            lower_case_names3 = lower_case_names3 + chr(letter_in_name)
        index46 += 1

    list_of_letters2 = list(second_middle_name_with_space)
    (random.shuffle(list_of_letters2))

    index46 = 0
    lower_case_names4 = ""
    while index46 < len(list_of_letters2):
        letter_in_name2 = ord(list_of_letters2[index46])
        if letter_in_name2 >= 65 and letter_in_name2 <= 90:
            letter_in_name2 = letter_in_name2 + 32
            letter_in_name2 = chr(letter_in_name2)
            lower_case_names4 = lower_case_names4 + letter_in_name2
        else:
            lower_case_names4 = lower_case_names4 + chr(letter_in_name2)
        index46 += 1

    # ================================================================================

    first_letter_of_Last_name = len(name_full_) - 1

    while first_letter_of_Last_name >= 0:
        if name_full_[first_letter_of_Last_name] == " ":
            break
        else:
            first_letter_of_Last_name = first_letter_of_Last_name - 1
    end_of_last_name = len(name_full_)
    last_name = (name_full_[first_letter_of_Last_name:end_of_last_name])
    if len(last_name) < 2:
        print("You didn't type your last name")

    # ====================================================================

    first_last_name_space = ""
    space_remover_pos = 0
    space_remover = 0
    while space_remover_pos < len(last_name):
        if last_name[space_remover_pos] == " ":
            space_remover_pos += 1
            space_remover += 1
        else:
            space_remover_pos += 1
            break
    last_name = (last_name[space_remover:len(last_name)])
    (last_name)

    list_of_letters = list(last_name)
    (random.shuffle(list_of_letters))

    index = 0
    lower_case_names2 = ""
    while index < len(list_of_letters):
        letter_in_name = ord(list_of_letters[index])
        if letter_in_name >= 65 and letter_in_name <= 90:
            letter_in_name = letter_in_name + 32
            letter_in_name = chr(letter_in_name)
            lower_case_names2 = lower_case_names2 + letter_in_name
        else:
            lower_case_names2 = lower_case_names2 + chr(letter_in_name)
        index += 1
    name_list=(lower_case_names, lower_case_names3, lower_case_names4, lower_case_names2)

    return name_list;


def boolean_palindrome(name_full_):
    fn = ""
    pos = 0
    while pos < len(name_full_):
        if name_full_[pos] == " ":
            break
        else:
            fn = fn + name_full_[pos]
        pos = pos + 1

    if fn == (name_full_[::-1]):
        print("true")
    else:
        print("false")


def intals(name_full_):
    frist_intal = ""
    frist_intal = frist_intal + name_full_[0]
    last_intal_position = len(name_full_) - 1
    first_letter_of_Last_name = len(name_full_) - 1
    while first_letter_of_Last_name >= 0:
        if name_full_[first_letter_of_Last_name] == " ":
            break
        else:
            first_letter_of_Last_name = first_letter_of_Last_name - 1
    first_letter_of_Last_name = first_letter_of_Last_name + 1
    both_intals=(frist_intal,name_full_[first_letter_of_Last_name])
    return both_intals


def lowercase_name(name_full_):
    index = 0
    lower_case_names = ""
    while index < len(name_full_):
        letter_in_name = ord(name_full_[index])
        if letter_in_name >= 65 and letter_in_name <= 90:
            letter_in_name = letter_in_name + 32
            letter_in_name = chr(letter_in_name)
            lower_case_names = lower_case_names + letter_in_name
        else:
            lower_case_names = lower_case_names + chr(letter_in_name)
        index += 1
    return lower_case_names

def upper_case_name(name_full_):
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


name_full_ = str(input("what is your full name\n"))  # name of user
print("what do you want from your name please choose from this list")
time.sleep(.25)
print(colored('my name reversed(1)', 'red'), colored('number of vowels (2)', 'green'),colored('number of consonants(3)',('blue')),colored('my first name(4)','cyan'))
time.sleep(.25)
print(colored('my last name(5)', 'yellow'), colored('my middle names(6)', 'magenta'),colored('boolean hyphin(7)',('grey')),colored('lowercase my name(8)','red'))
time.sleep(.25)
print(colored('uppercase my name(9)', 'green'), colored('my name randomized(10)', 'blue'),colored('boolean if palindrome(11)',('cyan')),colored('intials(12)','red'))
time.sleep(.25)
chocie_for_what_program_to_run = input("type the number corisponing to the function you want")  # asks user what part of the
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
    list_of_middle_names=middle_name(name_full_)

    first_middle_name = list_of_middle_names[0]
    second_middle_name = list_of_middle_names[1]
    third_middle_name = list_of_middle_names[2]
    fourth_middle_name = list_of_middle_names[3]
    five_middle_name = list_of_middle_names[4]
    sixth_middle_name = list_of_middle_names[5]

    Final_list_of_middle_names = "Your middle names are "

    if len(first_middle_name) > 1:
        Final_list_of_middle_names += (first_middle_name)

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

    index = 0
    list_of_all_commas = []
    # prgoam has to run through each letter and find the location of certne charrtets
    while index < len(Final_list_of_middle_names):
        if Final_list_of_middle_names[index] == ",":
            list_of_all_commas.append(index)
            index += 1
        else:
            index += 1
    last_comma = list_of_all_commas[len(list_of_all_commas) - 1]
    if len(Final_list_of_middle_names) == 0:
        print("you didnt type your middle name")
    else:
        print((Final_list_of_middle_names[0:last_comma]), ("and"),(Final_list_of_middle_names[last_comma + 1:len(Final_list_of_middle_names)]))
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



