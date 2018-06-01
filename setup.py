from setuptools import setup

setup(name='gastonSyslogFW',
      version='1.0',
      description='Syslog message forwarder',
      url='https://github.com/ybovard/gastonSyslogFW',
      author='Yves Bovard',
      author_email='ybovard@gmail.com',
      packages=['gastonSyslogFW'],
      install_requires=[ 'requests', ],
      zip_safe=False)
