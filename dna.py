#! /usr/bin/env python
# -*- coding: utf-8 -*-
# License: GPLv2
# Author: Shih-Yuan Lee (FourDollars) <fourdollars@gmail.com>

import codecs
import re
import sys

class dna:
    def __init__(self):
        pattern = re.compile('^([0-9]+) (.*)$')
        file = codecs.open('dna.cin', 'r', 'utf-8')
        self.dna = dict()
        for line in file.readlines():
            result = pattern.match(line)
            if result:
                if result.group(1) not in self.dna:
                    chars = list()
                    chars.append(result.group(2))
                    self.dna[result.group(1)] = chars
                else:
                    chars = self.dna[result.group(1)]
                    chars.append(result.group(2))
        file.close()
    def find(self, str):
        if str in self.dna:
            return self.dna[str]
        else:
            return None

if __name__ == "__main__":
    for i in range(len(sys.argv)):
        if i != 0:
            for char in dna().find(sys.argv[i]):
                print char
