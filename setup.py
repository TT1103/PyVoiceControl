from setuptools import setup

setup(name='PyVoiceControl',
      version='0.0.1',
      packages=['PyVoiceControl'],
      entry_points={
          'console_scripts': [
              'PyVoiceControl = PyVoiceControl.__main__:main'
          ]
      },
      )