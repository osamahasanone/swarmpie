import numpy


class ChecksumCalculator:
    '''Calculate checksum of NMEA message'''

    def __init__(self, sentence):
        '''Constructor

        @parameters:

        value (str): the sentence to calculate the checksum for (text between $ and * in an NMEA message)
        '''
        self.sentence = sentence

    @property
    def sentence(self):
        return self.__sentence

    @sentence.setter
    def sentence(self, value):
        if not value:
            raise ValueError('Short message should be specified')
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


class NMEAMessageComposer(ChecksumCalculator):
    def __str__(self):
        return f'${self.sentence}*{self.checksum}'


class NMEAMessageChecker(ChecksumCalculator):
    def __init__(self, sentence, received_checksum):
        super().__init__(sentence)
        self.received_checksum = received_checksum

    @property
    def received_checksum(self):
        return self.__received_checksum

    @received_checksum.setter
    def received_checksum(self, value):
        self.__received_checksum = value

    def is_valid(self):
        return self.checksum == self.received_checksum
