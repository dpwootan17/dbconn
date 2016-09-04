from dbconn.sessionmanager import SessionManager


def get_engine():
	return SessionManager()


def verify_session_closed():
	sm = SessionManager()
	with sm:
		print('just got a new session\n')


def main():
	get_engine()
	verify_session_closed()

if __name__ == '__main__':
	main()
