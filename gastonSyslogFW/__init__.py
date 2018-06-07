import sys
import socketserver
import re
import json
import argparse
import logging
from .httpHandler import HTTPHandler

def defaultConfig():
    config={}
    config['listen']='127.0.0.1'
    config['port']=514
    config['destination']=['http://127.0.0.1:8080/hubot/notify/all/']
    config['ignore']=[]
    return config

def readConfigFromFile(configFilePath,config):
    with open(configFilePath, encoding='utf-8-sig') as config_file:
        config_json=json.loads(config_file.read())
        if 'listen' in config_json:
            config['listen']=config_json['listen']
        if 'port' in config_json:
            config['port']=config_json['port']
        if 'destination' in config_json:
            config['destination']=config_json['destination']
        if 'ignore' in config_json:
            for reg in config_json['ignore']:
                config['ignore'].append(re.compile(reg))
    return config


def getConfig(path=None):
    config=defaultConfig()
    if path is None:
        configPath=['./gastonSyslogFW.conf','/etc/gastonSyslogFW.conf','/usr/local/etc/gastonSyslogFW.conf']
    else:
        configPath=[path]

    for cfg in configPath:
        try:
            readConfigFromFile(cfg,config)
            return config
        except FileNotFoundError as e:
            pass

    return config


def main():
    config=getConfig()

    #override with command line parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="verbose debug message", action="store_true")
    args=parser.parse_args()
    
    if args.debug:
        config['debug']=True
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("starting process") 
    try:
        logging.debug("socker server creation") 
        server = socketserver.UDPServer((config['listen'],config['port']), HTTPHandler)
        server.destinationList=config['destination']
        server.ignoreList=config['ignore']

        logging.info("listening") 
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit) as e:
        logging.critical("recieved {}: {}".format(e.__class__.__name__, e))
        raise e
    except KeyboardInterrupt:
        logging.critical("recieved CTRL-C event")

    logging.critical("process stopped")
