import csv

from os.path import join, dirname
import struct
from typing import Dict

types={'uint32': (2, ">L") , 'uint16': (1, ">H"), 'String(32)': (16,None),
       'String(16)': (8,None), 'int16': (1,">h"), 'acc32': (2,">L")}

class Entry:
    def __init__(self, e):
        self.k = e['Name']
        self.description = e['Description']
        self.addr = int(e['Address'])
        self.sz = int(e['Size'])
        self.unit = e['Units']
        self.type = e['Type']
        self.end_addr = self.addr+self.sz
        self.raw_offset = None

    def replace(self, buff, fragment):
        assert self.sz * 2 >= len(fragment)
        end = self.raw_offset + len(fragment)
        buff[self.raw_offset:end] = fragment

    def extract(self, buff):
        raw = self.raw(buff)
        unpack_fmt = types[self.type][1]
        if unpack_fmt is None:
            end = raw.index(b'\x00')
            return raw[:end].decode('ascii')
        return struct.unpack(unpack_fmt, raw)[0]

    def raw(self, buff):
        end = self.raw_offset + self.sz * 2
        v = buff[self.raw_offset:end]
        return v

    def __str__(self):
        return self.k


entries = list(map(Entry, csv.DictReader(open(join(dirname(__file__), "registers.csv")))))

start_addr = entries[0].addr

entries_by_name:Dict[str,Entry] = {}

for e in entries:
    assert e.k not in entries_by_name, f'Dublicate {e}'
    entries_by_name[e.k]=e
    e.raw_offset = (e.addr - start_addr)*2
    assert e.type in types
    assert types[e.type][0] == e.sz


next_addr = None
for e in entries:
    if next_addr is not None:
        assert next_addr <= e.addr, f'Field overlap:{e} {e.addr}<{next_addr}'
    next_addr = e.end_addr



