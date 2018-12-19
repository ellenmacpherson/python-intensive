#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 16:38:12 2018

@author: ellenmacpherson
"""

####################################################
############# PIN/Security functions ###############
####################################################


def checkPIN_once(truepin): #truepin an integer with pin no.
    attempt = input('Please enter your PIN: ')
    if attempt == str(truepin):
        return True
    else:
        print ("PIN incorrect.")
        return False

def checkPIN(truepin): #Function checking pin a total of three times. If unsuccessful, user will be locked out of account.
    if checkPIN_once(truepin): #Security check 1.
        return True
    else:
        print ("\nPlease try again (2nd attempt. You have one attempt remaining.)")
    if checkPIN_once(truepin): #Runs checkPIN_once again. Security check 2.
        return True
    else:
        print ("Please try again (3rd and final attempt).") #Runs checkPIN_once again. Security check 3.
    if checkPIN_once(truepin):
        return True #Success
    else:
        print ("You have used all your attempts. For security reasons, your account has been locked. Contact customer services for help.") #Locks account
    return False

def DataBundlePurchase(truepin, balance):
    if checkPIN(truepin):
        print ("\nPlease choose your transaction type: ")
        print ("To request a balance, enter 1.")
        print ("To top up a Pay As You Go data bundle, enter 2.")
        print ("To purchase a monthly plan, enter 3.")

        transactionChoice = int(input("Please select an option: ")) #Prompts user to enter an option from the above print lines.

        if transactionChoice == 1:
            print ("Your balance is ", balance, " GBP")
            print ("Thanks for using our service today")
            return "balance-request"

        elif transactionChoice == 2:
            print ("Service unavailable")

        elif transactionChoice == 3:
            print ("Service unavailable")

        else:
            print ("Error: transaction type not recognised.")
            return "transaction-error"

    else:
        print ("\nPIN authorisation failed - exiting.")
        return "PIN-error"
