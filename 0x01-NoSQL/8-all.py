#!/usr/bin/env python3
'''Task 8'''
import pymongo


def list_all(mongo_collection):
    '''
    Lists all documents in a collection
    '''
    return [doc for doc in mongo_collection.find()]
