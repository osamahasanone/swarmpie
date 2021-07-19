import pytest
from ..nmea import ChecksumCalculator, RequestMessage, ResponseMessage


class TestChecksumCalculator:

    def test_falsy_sentence(self):
        with pytest.raises(ValueError):
            m = ChecksumCalculator(sentence=None)
        with pytest.raises(ValueError):
            m = ChecksumCalculator(sentence="any$any")

    @pytest.fixture
    def checksum_calc(self):
        return ChecksumCalculator(sentence='DT 300')

    def test_unicode(self, checksum_calc):
        assert checksum_calc.unicode() == [68, 84, 32, 51, 48, 48]

    def test_xor(self, checksum_calc):
        assert checksum_calc.xor() == 3

    def test_checksum(self, checksum_calc):
        return checksum_calc.checksum == '03'


class TestRequestMessage:

    @pytest.fixture
    def message(self):
        return RequestMessage(sentence='DT 300')

    def test_str(self, message):
        assert str(message) == '$DT 300*03'


class TestResponseMessage:

    @pytest.fixture
    def message(self):
        return ResponseMessage(sentence='DT 300', received_checksum='03')

    def test_is_valid(self, message):
        assert message.is_valid() == True
