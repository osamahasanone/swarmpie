class NMEAMessageBadFormatError(Exception):
    """Exception raised for NMEA message pattern ignored

    parameters:
        nmea_message: nmea message which caused the error
        message: explanation of the error
    """

    def __init__(self, nmea_message, message=''):
        self.message = message if message else f'"{nmea_message}" is not well formatted NMEA message'
        super().__init__(self.message)


class ChecksumError(Exception):
    """Exception raised when a NMEA message has an incorrect checksum

    parameters:
        sentence: sentence from which the check sum is calculated
        received_checksum: checksum as received in nmea message
        message: explanation of the error
    """

    def __init__(self, sentence, received_checksum, message=''):
        self.message = message if message else f'"{sentence}" has been received with invalid checksum {received_checksum}'
        super().__init__(self.message)
