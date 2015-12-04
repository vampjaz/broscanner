## parsing classes:


import os, sys
import tailer
import time

from config import *


def readfile(fn):
	while 1:
		fd = tailer.Tailer(open(LOGDIR + fn), end=False)
		for i in fd.follow():
			i = i.strip()
			if i[0] != '#': ## ignore comments
				j = i.split('\t') # split by tabs
				yield j


def convert(entry,fmt,empty,unset,sep):
	try:
		if entry in (empty,unset):
			return None
		if 'set[' in entry:
			ret = []
			ifmt = entry.split('[')[-1].split(']')[0]
			for i in entry.split(sep):
				ret.append(convert(i,ifmt,empty,unset,sep))
			return ret
		if 'vector[' in entry:
			ret = []
			ifmt = entry.split('[')[-1].split(']')[0]
			for i in entry.split(sep):
				ret.append(convert(i,ifmt,empty,unset,sep))
			return ret
		if fmt in ('port','count'):
			return int(entry)
		elif fmt in ('bool',):
			return entry == 'T'
		elif fmt in ('interval','time'):
			return float(entry)
		else:
			return entry
	except:
		return None

def parseentries(fn):
	while 1:
		try:
			fd = tailer.Tailer(open(LOGDIR + fn), end=False)
			separator = '\x09'
			set_separator = ','
			empty_field = '(empty)'
			unset_field = '-'
			fields = []
			types = []
			for i in fd.head(10): ## should be in first 10
				a = i.split(separator)
				if a[0] == '#separator':
					separator = a[1]
				elif a[0] == '#set_separator':
					set_separator = a[1]
				elif a[0] == '#empty_field':
					empty_field = a[1]
				elif a[0] == '#unset_field':
					unset_field = a[1]
				elif a[0] == '#fields':
					fields = a[1:]
				elif a[0] == '#types':
					types = a[1:]
			for i in readfile(fn):
				row = {}
				for idx,j in enumerate(i):
					k = convert(j,types[idx],empty_field,unset_field,separator)
					row[fields[idx]] = k
				yield row
		except (IOError, OSError):
			time.sleep(5)
