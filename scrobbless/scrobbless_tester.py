#!/usr/bin/env python
import time

from scrobbless import Scrobbless

s = Scrobbless()

token = s.get_token()

with open(".scrobbless", 'r+') as f:
  session_key = f.readline()

  if not session_key:
    s.auth_user(token)

    while not session_key:
      session = s.get_session(token)

      session_key = session['session']['key']

    f.write(session_key)


s.scrobble('Saves The Day', 'You Vandal', 'Through Being Cool', str(int(time.time())), session_key)
