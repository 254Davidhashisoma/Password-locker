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
        user.user_list_.append(self)



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
                pass     