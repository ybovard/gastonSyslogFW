from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='gastonSyslogFW',
      version='1.0',
      description=readme()
      url='https://github.com/ybovard/gastonSyslogFW',
      author='Yves Bovard',
      author_email='ybovard@gmail.com',
      packages=['gastonSyslogFW'],
      install_requires=[ 'requests', ],
      include_package_data=True,
      zip_safe=False)
