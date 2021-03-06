#!/usr/bin/env python
# coding: utf8

from distutils.core import setup

setup(
        name='mongo-connector-postgresql',
        version='1.1-beta10',
        description='Doc Manager Postgresl for Mongo connector Distribution Utilities',
        keywords=['mongo-connector', 'mongo', 'mongodb', 'postgresql'],
        platforms=["any"],
        author=u'Hugo Lassiège, Maxime Gaudin',
        author_email='hugo@hopwork.com, maxime@hopwork.com',
        install_requires=['mongo_connector >= 2.4', 'psycopg2 >= 2.6.1'],
        license="http://www.apache.org/licenses/LICENSE-2.0.html",
        url='https://github.com/Hopwork/mongo-connector-postgresql',
        packages=["mongo_connector", "mongo_connector.doc_managers"]
)
