
from sqlalchemy.orm import sessionmaker
from dbconn.engine import Engine
import logging


class SessionManager(object):
	session = None

	def __init__(self, **kwargs):
		_engine = Engine(**kwargs)
		Session = sessionmaker(bind=kwargs.get('db_name'))
		self.session = Session()

	def __enter__(self):
		return self.session

	def __exit__(self, exc_type, exc_val, exc_tb):
		if isinstance(exc_val, Exception):
			logging.log(level=logging.ERROR, msg=exc_val)
			self.session.rollback()
		else:
			self.session.flush()
			self.session.commit()
		self.session.close()

		print('session closed\n')