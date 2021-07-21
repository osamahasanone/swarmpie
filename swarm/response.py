import re
from .nmea import NMEAMessageChecker
from .constatnts import response_pattern
from .errors.response_errors import *


class Response:
    '''Parse Response NMEA message'''

    def __init__(self, nmea_message):
        self.nmea_message = nmea_message

    @property
    def nmea_message(self):
        return self.__nmea_message

    @nmea_message.setter
    def nmea_message(self, value):
        if not re.match(response_pattern, value):
            raise NMEAMessageBadFormatError(value)
        sentence = value[1:-3]
        received_checksum = value[-2:].lower()
        res_message = NMEAMessageChecker(sentence, received_checksum)
        if not res_message.is_valid():
            raise ChecksumError(sentence, received_checksum)

        self.__nmea_message = value

    @property
    def sentence(self):
        '''everything between $ and *xx'''
        return self.nmea_message[1:-3]

    @property
    def verb(self):
        '''swarm verb like FV,DT..'''
        return self.sentence.split(' ')[0]

    @property
    def parameters(self):
        '''response parameters list'''
        return self.sentence.split(' ')[1].split(',')

    @property
    def checksum(self):
        '''received checksum'''
        return self.nmea_message[-2:].lower()
