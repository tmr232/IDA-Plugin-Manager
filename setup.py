from setuptools import setup

setup(
    name='ipm',
    version='0.1',
    packages=['ipm'],
    url='https://github.com/tmr232/IDA-Plugin-Manager',
    license='MIT',
    author='Tamir Bahar',
    author_email='',
    description='IDA Plugin Manager',
    entry_points={
          'console_scripts': [
              'ipm=ipm.ipm:main'
          ]
      },
)
