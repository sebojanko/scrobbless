# scrobbless
A minimal last.fm scrobbler written in Python 3.6



# How to install

```pip install scrobbless```



# How to acquire keys

You must register for an API account on last.fm:
https://www.last.fm/api/account/create

For using the program, two environment variables have to be set:
SCROBBLESS_API_KEY and SCROBBLESS_SECRET_KEY.



# How to use

First, you must request a token:

```
s = Scrobbless()
token = s.get_token()
```

With that token, you auth the user, which will open a browser with a button to click

```s.auth_user(token)```

After that, you will receive the session key, which is passed with every request to the last.fm server:

```
session = s.get_session(token)
session_key = session['session']['key']
```

The session key lasts a long time so it should be saved somewhere and reused.

After completing this process, you can start scrobbling:

```scrobble(artist, track, album, timestamp, session_key)```

scrobbles a song.

```update_np(artist, track, album, session_key)```

sets a song as 'now playing'.



# LICENSE

GNU GPL v3
