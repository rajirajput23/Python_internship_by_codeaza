import logging

#logging.debug('This is a debug message')
#logging.info('This is an info message')
#logging.warning('This is a warning message')
#logging.error('This is an error message')
#logging.critical('This is a critical message')

#Basic config

#logging.basicConfig(level=logging.DEBUG)
#logging.debug('This will get logged')

#formating file

#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.warning('This will get logged to a file')

#Date and time logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' , level=logging.INFO)
logging.info('Admin logged in')

#logging variable data  
import logging
name = 'John'
logging.error('%s raised an error', name)
