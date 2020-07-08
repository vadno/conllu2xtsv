#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    author: Noémi Vadász
    last update: 2020.04.16.

    conll-u formátumot konvertál xtsv-re
    beolvassa a conll-u fájlt
    a mezőkből soronként dict-et készít
    majd kiírja az xtsv fájlt
    a mezők sorrendje megegyezik a conll-u mezőkével, de egy header jelzi a tartalmat

"""
import csv
import sys


conllu = ['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel']
# conllu = ['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc']

# TODO sorrendet rendbetenni (a korkor-ban rossz a sorrend)
xtsv_fields = {'id': '_',
               'form': '_',
               'lemma': '_',
               'upostag': '_',
               'xpostag': '_',
               'feats': '_',
               'head': '_',
               'deprel': '_'}


def check_fields(lines):

    for line in lines:
        if isinstance(line, dict):
            for key, value in line.items():
                print(key, value)


def read_conll(file):

    lines = list()

    with open(file) as inf:
        reader = csv.reader(inf, delimiter='\t', quoting=csv.QUOTE_NONE)
        for line in reader:
            if len(line) > 1 and line[0] != '':
                fields = dict()
                for field in conllu:
                    fields[field] = line[conllu.index(field)]
                lines.append(fields)
            elif len(line) == 1 and line[0].startswith('#'):
                pass
            else:
                lines.append('')

    return lines


def print_file(file, lines):

    with open(file, 'w') as ouf:
        header = '\t'.join([key for key, value in xtsv_fields.items()])
        print(header, file=ouf)

        for line in lines:
            if isinstance(line, dict):
                fields = '\t'.join(line[field] for field in line)
                print(fields, file=ouf)
            else:
                print(line, file=ouf)


def main():

    ifile = sys.argv[1]
    ofile = sys.argv[2]

    conll_lines = read_conll(ifile)
    # check_fields(conll_lines)
    print_file(ofile, conll_lines)


if __name__ == "__main__":
    main()
