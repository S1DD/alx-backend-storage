#!/usr/bin/env python3

import pymongo


def schools_by_topic(mongo_collection, name, topics):
    """
    returns the list of school having a specific topic
    """
    '''Returns the list of school having a specific topic.
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
