class UnkownVerbError(Exception):
    """Exception raised for unknown swarm verb

    parameters:
        verb: verb which caused the error
        message: explanation of the error
    """

    def __init__(self, verb, message=''):
        self.message = message if message else f'"{verb}" is unknown swarm verb'
        super().__init__(self.message)


class ParametersCountError(Exception):
    """Exception raised when the exact number of parameters is ignored

    parameters:
        verb: swarm verb to which the wrong number of parameters have been passed
        count: wrong count of parameters
        target_count: count of parameters should be passed
        message: explanation of the error
    """

    def __init__(self, verb, count, target_count, message=''):
        self.message = message if message else f'"{verb}" accepts ({target_count}) parameter(s).However, ({count}) have been passed'
        super().__init__(self.message)


class ParameterBadFormatError(Exception):
    """Exception raised for a command parameter pattern is ignored

    parameters:
        verb: swarm verb to which the bad formatted parameter was passed
        parameter: parameter which caused the error
        message: explanation of the error
    """

    def __init__(self, verb, parameter, message=''):
        self.message = message if message else f'"{parameter}" parameter for "{verb}" is not well formatted'
        super().__init__(self.message)
