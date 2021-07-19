import re
from .nmea import NMEAMessageChecker
from .constatnts import response_pattern


class Response:
    def __init__(self, nmea_message):
        self.nmea_message = nmea_message

    @property
    def nmea_message(self):
        return self.__nmea_message

    @nmea_message.setter
    def nmea_message(self, value):
        if not re.match(response_pattern, value):
            raise ValueError(f'Received NMEA message is not well formatted')
        res_message = NMEAMessageChecker(
            sentence=value[1:-3], received_checksum=value[-2:])
        if not res_message.is_valid():
            raise ValueError(
                f'checksum of received NMEA message is incorrect !!')

        self.__nmea_message = value

    @property
    def sentence(self):
        return self.nmea_message[1:-3]

    @property
    def verb(self):
        return self.sentence.split(' ')[0]

    @property
    def parameters(self):
        return self.sentence.split(' ')[1].split(',')

    @property
    def checksum(self):
        return self.nmea_message[-2:]
