#######################################################
# 
# FederateClients.py
# Python implementation of the Class FederateClients
# Generated by Enterprise Architect
# Created on:      12-Sep-2020 10:32:03 PM
# Original author: natha
# 
#######################################################

class FederateClients:
    def __init__(self):
        # list of instances of the Federate Object.
        self.__clientArray = []

    def add_client(self, Federate):
        """add client to federate clients list
        """
        self.__clientArray.append(Federate)

    def remove_client(self, Federate):
        self.__clientArray.remove(Federate)

    def get_all_clients(self):
        return self.__clientArray