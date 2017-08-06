from builtins import object
from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass


class EncryptionKey(with_metaclass(ABCMeta, object)) :

	@abstractmethod
	def encrypt( self, plain ) : pass
	@abstractmethod
	def decrypt( self, crypt ) : pass
