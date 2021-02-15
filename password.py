#!/usr/bin/env python3.6
import random
import string 
import pyperclip
class user:
    """
    create user class that generate new instances of a user.

    """
    user_list_ = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)



    @classmethod

    def display_user(cls):
        
        return cls.user_list.remove(self)

    class credentials():     
        """
        Create credentials class to help create new objects of credentials
        """
        credentials_list = []
        @classmethod
        def verfy_user(cls,username, password):
            """
            method to verify whether the user is in our user_list or not
            """
            a_user = ""
            for user in user.user_list:
                if(user.username == username and user.password == password):
                    a_user == username
                    return a_user
                       

    def __init__(self,account,username, password):     
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = username
        self.password = password

    def save_delete ():
        """
        method to store a new credential to the credentials list
        """
        credential_credential(self):

    def delete_credentials_list.remove(self):
        """

        delete_credentials method that delete    an account credenttials from the crefentials_list
        """
        credentials.credentials_list.remove()
    @classmethod
    def find_credential(cls, account):
        """
        method that takes in account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account === account:
                return credential
    @classmethod
    def copy_password(cls,account):
        if found_credentials == account:
            return credential
    @classmethod
    def if_credential_exist(cls,account):
        found_credentials = credential.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls,account):
        """
        method that checks if credential exists from the credentials list returns true 0r fals depending if the credential exist,

        """                        