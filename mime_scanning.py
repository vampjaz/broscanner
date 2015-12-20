## simple file type detection.
## if i had unlimited api access, i would send every single md5 to something like VirusTotal

forbidden_types = ['text/x-bash', 'text/scriptlet', 'application/x-opc+zip', 'application/com', 'application/x-msmetafile', 'application/x-shellscript', 'text/x-sh', 'text/x-csh', 'application/x-com', 'application/x-helpfile', 'application/hta', 'application/x-bat', 'application/x-php', 'application/x-winexe', 'application/x-msdownload', 'text/x-javascript', 'application/x-msdos-program', 'application/bat', 'application/x-winhelp', 'application/vnd.ms-powerpoint', 'text/x-perl', 'application/x-javascript', 'application/x-ms-shortcut', 'application/vnd.msexcel', 'application/x-msdos-windows', 'text/x-python', 'application/x-download', 'text/javascript', 'text/x-php', 'application/exe', 'application/x-exe', 'application/x-winhlp', 'application/msword', 'application/zip']

from config import *
import bparser
import notifiers

for i in bparser.parseentries('http.log'):
	print i['resp_mime_types']
