#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = False

class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
	
