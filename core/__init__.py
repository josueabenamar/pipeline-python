#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask


build_mode = os.environ['APP_SETTINGS']

if build_mode == "production":
    build_mode = "config.ProductionConfig"
elif build_mode == "development":
    build_mode = "config.DevelopmentConfig"
else:
    build_mode = "config.TestingConfig"

app = Flask(__name__)
app.config.from_object(build_mode)


print(app.config['DEBUG'])
print(app.config['TESTING'])
