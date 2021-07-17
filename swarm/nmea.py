import numpy


class ChecksumCalculator:
    '''Calculate checksum of NMEA message

    @parameters:

    value (str): the sentence to calculate the checksum for (text between $ and * in an NMEA message)
    '''

    def __init__(self, sentence):
        self.sentence = sentence

    @property
    def sentence(self):
        return self.__sentence

    @sentence.setter
    def sentence(self, value):
        if not value:
            raise ValueError('Short message should specified not contain $')
        if '$' in value:
            raise ValueError('Short message should not contain $')
        self.__sentence = value

    def unicode(self):
        '''convert message characters to unicode

        returns:
        list of message characters in unicode form
        '''
        return [ord(ch) for ch in self.sentence]

    def xor(self):
        ''' apply xor on all unicode representation of message characters

        returns:
        unicode result of xor
        '''
        unicode_array = numpy.array(self.unicode())
        return numpy.bitwise_xor.reduce(unicode_array)

    @property
    def checksum(self):
        '''convert xor unicode result to short hexadecimal represention

        returns hexadecimal result after removing '0x' prefix and adding leading zeros to have to characters
        '''
        hex_checksum = hex(self.xor())
        return hex_checksum[2:].zfill(2)


class Message(ChecksumCalculator):
    def __str__(self):
        return f'${self.sentence}*{self.checksum}'
