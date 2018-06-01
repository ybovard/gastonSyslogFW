#!/usr/bin/env python3

import re
import logging
import socketserver
import requests

class SyslogUDPHandler(socketserver.BaseRequestHandler):
  # list of destinations represented by strings. For exemple:
  destinationList=[]

  # list of compiled regexp. When matched, the given message will be discarded/ignored
  ignoreList=[]

  def _isInIgnoreList(self,msg):
    for regex in self.ignoreList:
      if regex.match(msg) is not None:
        return True
    return False


  def handle(self):
    data = {'log': bytes.decode(self.request[0].strip())}
    socket = self.request[1]
    if not self._isInIgnoreList(str(data)):
        logging.debug( "{}(sent) : {}".format(self.client_address[0], str(data)))
        for dest in self.destinationList:
            r = requests.post(dest, data = data)
    else:
        logging.debug( "{}(ignored) : {}".format(self.client_address[0], str(data)))
