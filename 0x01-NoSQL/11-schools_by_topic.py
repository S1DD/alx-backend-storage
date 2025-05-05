#!/usr/bin/env python3

import pymongo


def update_topics(mongo_collection, name, topics):
    """
    returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
