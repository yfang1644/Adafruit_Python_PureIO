from distutils.core import setup
classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Adafruit_PureIO',
      version           = '0.2.3',
	  url               = 'https://github.com/adafruit/Adafruit_Python_PureIO',
      author            = 'Tony DiCola / Adafruit Industries',
      author_email      = 'support@adafruit.com',
      description       = 'Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI.  Drop in replacement for smbus and spidev modules.',
      license           = 'MIT',
      classifiers       = classifiers,
      packages          = ['Adafruit_PureIO']
     )
