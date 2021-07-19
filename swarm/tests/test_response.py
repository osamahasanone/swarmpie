from swarm.nmea import ChecksumCalculator
import pytest
from ..response import Response
from ..errors.response_errors import *


class TestResponse:

    def test_unknown_verb(self):
        with pytest.raises(NMEAMessageBadFormatError):
            r = Response('$XX 300*7f')

    def test_falsy_checksum(self):
        with pytest.raises(ChecksumError):
            r = Response('$DT 300*0f')

    @pytest.fixture
    def true_response(self):
        return Response('$FV 2021-03-23-18:25:40,v1.0.0*7f')

    def test_sentence(self, true_response):
        assert true_response.sentence == 'FV 2021-03-23-18:25:40,v1.0.0'

    def test_checksum(self, true_response):
        assert true_response.checksum == '7f'

    def test_verb(self, true_response):
        assert true_response.verb == 'FV'

    def test_parameters(self, true_response):
        assert true_response.parameters == ['2021-03-23-18:25:40', 'v1.0.0']
