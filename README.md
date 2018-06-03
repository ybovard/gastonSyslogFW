# Introduction
GastonSyslogFW is a syslog message forwarder. The goal of this project is to be able on busybox system like Alpine Linux to send syslog message on different destination, for exemple hubot. 

It is also able to filter message, in order not to send every syslog message on the destinations

# Pre-requisite
* python3

# Usage as daemon

# Usage in script
```
    try:
        server = socketserver.UDPServer(('127.0.0.1',514), gastonSyslogFW.SyslogUDPHandler)
        server.destinationList=['https://myhubot.example.com/all/']
        server.ignoreList=['.* sshd\[.*']
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")

```

# Project status
Project in development
