from swarm.nmea import ChecksumCalculator
import pytest
from ..response import Response
from ..errors.response_errors import *


class TestResponse:

    @pytest.mark.parametrize('message', ['$XX 300*7f', '$CS30*2a', '$CS30*2A'])
    def test_bad_format(self, message):
        with pytest.raises(NMEAMessageBadFormatError):
            r = Response(message)

    @pytest.mark.parametrize('falsy_checksum_response', ['$GN 15*20', '$DT 300*0f'])
    def test_falsy_checksum(self, falsy_checksum_response):
        with pytest.raises(ChecksumError):
            r = Response(falsy_checksum_response)

    @pytest.mark.parametrize('checksum_response', ['$GN 30*2d', '$GN 30*2D'])
    def test_true_checksum(self, checksum_response):
        with pytest.raises(ChecksumError):
            r = Response(checksum_response)

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
