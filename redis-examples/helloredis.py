#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
import time;

ONE_WEEK = 7 * 86400;
VOTE_SOCRE = 432;

pool = redis.ConnectionPool(host='106.54.248.54', port=6379);
conn = redis.Redis(connection_pool=pool)
conn.ping()
conn.set('hp', 'lalal')

#def article_vote(conn, user, article):
#    cutoff = time.time() - ONE_WEEK

import mysql.connector

conn = mysql.connector.connect(host='106.54.248.54', user='poplarli', password='123456', database='Practice')
cursor = conn.cursor()
cursor.execute('select count(*) from t2')
print(cursor.fetchone())