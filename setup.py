from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='gastonSyslogFW',
      version='1.0',
      long_description=readme(),
      url='https://github.com/ybovard/gastonSyslogFW',
      author='Yves Bovard',
      author_email='ybovard@gmail.com',
      packages=['gastonSyslogFW'],
      install_requires=[ 'requests', ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
