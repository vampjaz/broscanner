## simple passive host discovery

forbidden_types = ['text/x-bash', 'text/scriptlet', 'application/x-opc+zip', 'application/com', 'application/x-msmetafile', 'application/x-shellscript', 'text/x-sh', 'text/x-csh', 'application/x-com', 'application/x-helpfile', 'application/hta', 'application/x-bat', 'application/x-php', 'application/x-winexe', 'application/x-msdownload', 'text/x-javascript', 'application/x-msdos-program', 'application/bat', 'application/x-winhelp', 'application/vnd.ms-powerpoint', 'text/x-perl', 'application/x-javascript', 'application/x-ms-shortcut', 'application/vnd.msexcel', 'application/x-msdos-windows', 'text/x-python', 'application/x-download', 'text/javascript', 'text/x-php', 'application/exe', 'application/x-exe', 'application/x-winhlp', 'application/msword', 'application/zip']

from config import *
import bparser
import notifiers

for i in bparser.parseentries('files.log'):
	#if not i['local_orig']: ## ignore internal transfers
	if i['mime_type'] in forbidden_types: ## scan all of these types
		print
		print "{} downloaded a file from {} via {}".format(i['rx_hosts'],i['tx_hosts'],i['source'])
		print "Filename: {}  length: {}  mime type: {}".format(i['filename'],i['total_bytes'],i['mime_type'])
		print "MD5: {}  SHA1: {}".format(i['md5'],i['sha1'])
