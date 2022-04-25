#!/usr/bin/env python3.9
from credential import Credential

def create_credential(uname,pword):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(uname,pword)
    return new_credential