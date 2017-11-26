from twisted.internet.defer import Deferred


def myErrback(failure):

	print "Failed"

d = Deferred()
d.addErrback(myErrback)
d.errback()
