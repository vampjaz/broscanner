## config file (python format)

LOGDIR = "/usr/local/bro/spool/bro" # temp directory i found cause the symlinked one in /usr/local/bro/logs/current has issues


NOTIFICATIONS = ('osx_nc','email') # most notifications currently unimplemented...

##################################################################
# do not touch
if LOGDIR[-1] != '/':
	LOGDIR += '/'
