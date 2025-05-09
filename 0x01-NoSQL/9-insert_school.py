#!/usr/bin/env python3

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    result =  mongo_collection.insert_one(mongo_collection, kwargs)
    return result.inserted_id
