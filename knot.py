#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Shih-Yuan Lee (FourDollars) <fourdollars@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

import codecs
import re
import sys

class knot:
    def __init__(self):
        option = re.compile('^%(\w+)\s+(\S+)$')
        pattern = re.compile('^([0-9]+) (.*)$')
        file = codecs.open('dna.cin', 'r', 'utf-8')
        self.numdef = dict()
        self.chardef = dict()
        mode = 0
        for line in file.readlines():
            if mode == 0:
                result = option.match(line)
                if result and result.group(1) == 'chardef' and result.group(2) == 'begin':
                    mode = 1
            elif mode == 1:
                result = pattern.match(line)
                if result:
                    if result.group(1) not in self.numdef:
                        chars = list()
                        chars.append(result.group(2))
                        self.numdef[result.group(1)] = chars
                    else:
                        chars = self.numdef[result.group(1)]
                        chars.append(result.group(2))
                    self.chardef[result.group(2)] = result.group(1)
                else:
                    result = option.match(line)
                    if result and result.group(1) == 'chardef' and result.group(2) == 'end':
                        mode = 2
        file.close()
    def find(self, str):
        if str in self.numdef:
            return self.numdef[str]
        elif str in self.chardef:
            return self.chardef[str]
        else:
            return None

if __name__ == "__main__":
    obj = knot()
    for i in range(len(sys.argv)):
        if i > 0:
            str = unicode(sys.argv[i], 'utf-8')
            if str.isnumeric():
                list = obj.find(str)
                if list:
                    for char in list:
                        str = str + ' ' + char
                    print str
                else:
                    print str, 'not found.'
            else:
                for char in str:
                    print char, obj.find(char)
