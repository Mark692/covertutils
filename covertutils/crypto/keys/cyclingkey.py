from builtins import object
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass



class CyclingKey(with_metaclass(ABCMeta, object)) :

	def __init__( self, passphrase, **kw ) :
		pass

	@abstractmethod
	def cycle( self, rounds = 1) :
		pass


	@abstractmethod
	def getUUIDBytes( self, length ) :
		pass


	@abstractmethod
	def getKeyBytes( self, length ) :
		pass


	@abstractmethod
	def getKeyLength( self ) :
		"""
:rtype: int
:return: Returns the key length.
		"""
		pass


	@abstractmethod
	def reset( self ) : 	pass


	@abstractmethod
	def setCycle( self, cycle ) :	pass
