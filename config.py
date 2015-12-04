## config file (python format)

LOGDIR = "/usr/local/bro/spool/bro" # temp directory i found cause the symlinked one in /usr/local/bro/logs/current has issues


if LOGDIR[-1] != '/':
	LOGDIR += '/'


NOTIFICATIONS = ('osx_nc','email')
