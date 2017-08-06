from builtins import object
from abc import ABCMeta, abstractmethod

from binascii import hexlify
from future.utils import with_metaclass



class CyclingAlgorithm(with_metaclass(ABCMeta, object)) :

	def __init__( self, message ) :
		self.message = message


	def update( self, message ) :
		self.message += message


	@abstractmethod
	def digest( self ) :
		pass


	def hexdigest( self ) :
		bin_ = self.digest()
		return hexlify( bin_ )
