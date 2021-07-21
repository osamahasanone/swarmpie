import serial


class UART:
    def __init__(self, windows=False):
        if not windows:
            self.__connection = serial.Serial('/dev/ttyS0', 115200)

    def _prepare_message(self, message):
        '''convert a message to a line and encode it'''
        if not message:
            raise ValueError('Empty messages can not be sent to serial')
        return f'{message}\n'.encode()

    def send_line(self, message):
        '''compose a line from a message and send it to port'''
        self.__connection.write(self._prepare_message(message))

    def _parse_line(self, line):
        '''convert a line to a message by decoding it and removing trailing spaces and \n'''
        return line.decode().rstrip()

    def receive_line(self):
        '''receive one line from port and get the decoded striped message it includes'''
        return self._parse_line(self.self.__connection.readline())
