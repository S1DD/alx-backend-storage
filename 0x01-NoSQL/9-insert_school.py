#!/usr/bin/env python3

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    return mongo_collection.insert(mongo_collection, kwargs).inserted_id
