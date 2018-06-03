#!/usr/bin/env python3

import re
import logging
import socketserver
import requests

class SyslogUDPHandler(socketserver.BaseRequestHandler):

  def _isInIgnoreList(self,msg):
    #print("checking message: {}".format(msg))
    for regex in self.server.ignoreList:
      if regex.match(msg) is not None:
        return True
    return False


  def handle(self):
    data = {'log': bytes.decode(self.request[0].strip())}
    socket = self.request[1]
    if not self._isInIgnoreList(str(data)):
        #print('send : {}'.format(str(data)))
        for dest in self.server.destinationList:
            r = requests.post(dest, data = data)
