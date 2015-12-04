## notification handlers


from config import *

notifier_list = []

if 'osx_nc' in NOTIFICATIONS:
	from pync import Notifier as osx_notifier

	def osx_nc_notification(text):
		osx_notifier.notify(text, title='BroScanner')

	notifier_list.append(osx_nc_notification)


def notify(text):
	print text
	for n in notifier_list:
		n(text)
