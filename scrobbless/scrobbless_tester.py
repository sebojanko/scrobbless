from scrobbless import Scrobbless

s = Scrobbless()

token = s.get_token()
s.auth_user(token)

session_key = ''

while True:
  session = s.get_session(token)

  try:
    if session['session']['key']:
      session_key = session['session']['key']
      break
  except KeyError:
    pass

print(session_key)
