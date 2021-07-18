import re
from ..nmea import Message
from .validation import verbs_params


class Command:
    '''Compose command NMEA message'''

    def __init__(self, verb, parameters=[]):
        '''Constructor

        @parameters:

        verb (str): command verb (DT,Fv,TD..)
        parameters (list): command parameters (?,@,300 ..), all parameters will be converted to string
        '''
        self.verb = verb
        self.parameters = parameters

    @property
    def verb(self):
        return self.__verb

    @verb.setter
    def verb(self, value):
        if value not in verbs_params:
            raise ValueError(f'Unknow command verb {value}')
        self.__verb = value

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, values):
        str_values = [str(value) for value in values]
        verb_patterns = verbs_params.get(self.verb)
        if len(verb_patterns) != len(str_values):
            raise ValueError(
                f'{self.verb} command should have {len(verb_patterns)} parameter(s)')
        if not all(re.match(verb_patterns[i], str_values[i]) for i in range(len(verb_patterns))):
            raise ValueError(f'One of the parameters is not well formatted')
        self.__parameters = str_values

    @property
    def parameters_str(self):
        '''convert parameters list to a string

        returns:
        comma separated string of parameters: [1,2] => '1,2'
        '''
        parameters = [str(parameter) for parameter in self.parameters]
        return ','.join(parameters)

    @property
    def sentence(self):
        '''compose command sentence

        returns:
        string of the format 'verb[ parameters_str]' '''
        return f'{self.verb} {self.parameters_str}' if self.parameters else self.verb

    @property
    def nmea_sentence(self):
        '''compose nmea message

        returns:

        string of the format '$sentence*checksum' '''
        message = Message(self.sentence)
        return str(message)
