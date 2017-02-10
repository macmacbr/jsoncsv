#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#__doc__ = "Flattens a Json file with one line per leaf"
# vim: set fileencoding=UTF-8

import sys
import json

def flatten(d, result=None, current_key=None):
    if result is None:
        result = {}
    if isinstance(d, (list, tuple)):
        pad = len(str(len(d)))
        for index, element in enumerate(d):
            if current_key is not None:
                new_key = current_key + stylePre + str(index).zfill(pad) + stylePos
            else:
                new_key = str(index)
            flatten(element, result, new_key)
    elif isinstance(d, dict):
        if not d:
            result[current_key] = ""
        else:
            for key in d:
                value = d[key]
                if current_key is not None:
                    new_key = styleSep.join([current_key, (str(key).replace(" ", ""))])
                else:
                    new_key = str(key).replace(" ", "")
                flatten(value, result, new_key)
    else:
        result[current_key] = str(d).replace("\n", "__")
    return result

filename=None
if len(sys.argv) > 1 and not (""+sys.argv[1]).startswith("-"):
    filename = sys.argv.pop(1)

if len(sys.argv) > 1:
    stylePre = '['
    stylePos = ']'
    styleSep = '.'
else:
    stylePre = '#'
    stylePos = ''
    styleSep = '/'

lines = open(filename) if not filename == None else sys.stdin

data = ""
for line in lines:
    data += line

if data:
    json = json.loads(data)
    for key, value in flatten(json).iteritems():
        print "%s: %s" % (key, value)


