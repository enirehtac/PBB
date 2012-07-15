#!/usr/bin/env python
#coding=utf-8

import settings
import pymongo

db = pymongo.Connection(host=settings.mongodb_host,
    port=settings.mongodb_host)[settings.database_name]
db.posts.create_index([('modified', 1), ('node', 1)])
db.replies.create_index([('modified', 1)])