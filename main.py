## BroScanner:
## streaming python data analyzer for the bro network analyzer

import os, sys
import tailer
import time

from config import *
import bparser
import notifiers


for i in bparser.parseentries('known_services.log'):
	print i
	#notifiers.notify(i['msg'])
