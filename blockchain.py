#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:15:55 2020

@author: mohamedelmi
"""


import datetime
import json
import hashlib
from flask import Flask,jsonify


# Module 1 - Create a Blockchain

class Blockchain:
    
    def __int__(self):
        self.chain = []
        self.create_block(proof = 1,previous_hash = '0')
