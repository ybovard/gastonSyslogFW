#!/usr/bin/env python3

import re
import logging
import socketserver
import requests
import logging

class SyslogFWHandler(socketserver.BaseRequestHandler):
    def _isInIgnoreList(self,msg):
        #print("checking message: {}".format(msg))
        for regex in self.server.ignoreList:
            if regex.match(msg) is not None:
              return True
        return False


    def _forwardMessage(self, data):
        for dest in self.server.destinationList:
            if dest['type'] == 'http':
                r = requests.post(dest['url'], data = data)


    def handle(self):
        data = {'log': bytes.decode(self.request[0].strip())}
        logging.debug("message recieved: {}".format(data))
        socket = self.request[1]
        if not self._isInIgnoreList(str(data)):
            self._forwardessage(data)
        else:
            logging.debug("message in ignore list. Ignoring")
