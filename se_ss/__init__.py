import csv

from os.path import join, dirname

entries = list(csv.DictReader(open(join(dirname(__file__), "registers.csv"))))
