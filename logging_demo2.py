import logging

logger = logging.getLogger('dev')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('test.log')
fileHandler.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

logger.info('information message')