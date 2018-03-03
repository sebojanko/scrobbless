#!/usr/bin/env python
import json
import os
import webbrowser
from hashlib import md5

import requests


class Scrobbless:
  def __init__(self):
    self.api_key = os.environ['SCROBBLESS_API_KEY']
    self.secret = os.environ['SCROBBLESS_SECRET_KEY']
    self.base_url = 'http://ws.audioscrobbler.com/2.0/?'
    self.response_format = 'json'

  def get_token(self):
    params = dict(method='auth.getToken', api_key=self.api_key)
    self.update_params(params)

    api_resp = self.send_POST(params)
    return json.loads(api_resp)['token']

  def auth_user(self, token):
    webbrowser.open('http://www.last.fm/api/auth/?api_key={}&token={}'.format(self.api_key, token))

  def get_session(self, token):
    params = dict(method='auth.getSession', api_key=self.api_key, token=token)
    self.update_params(params)

    api_resp = self.send_POST(params)
    return json.loads(api_resp)

  def scrobble(self, artist, track, album, timestamp, session_key):
    params = dict(artist=artist, track=track, album=album, timestamp=timestamp, api_key=self.api_key, sk=session_key,
                  method='track.scrobble')
    self.update_params(params)

    api_resp = self.send_POST(params)
    return json.loads(api_resp)

  def update_np(self, artist, track, album, session_key):
    params = dict(artist=artist, track=track, album=album, api_key=self.api_key, sk=session_key,
                  method='track.updateNowPlaying')
    self.update_params(params)

    api_resp = self.send_POST(params)
    return json.loads(api_resp)

  def update_params(self, params):
    params['api_sig'] = self.create_signature(params)
    params['format'] = self.response_format

  def send_POST(self, params):
    return requests.post(self.base_url, params).text

  def create_signature(self, params):
    sorted_keys = sorted(params.keys())
    signature = ''

    for k in sorted_keys:
      signature += k
      signature += params[k]

    signature += self.secret

    return md5(signature.encode('utf-8')).hexdigest()
