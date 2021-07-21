import pytest
from ..nmea import ChecksumCalculator, NMEAMessageComposer, NMEAMessageChecker


class TestChecksumCalculator:

    @pytest.mark.parametrize('sentence', [None, '$any', 'any$any', 'any$'])
    def test_init_fail(self, sentence):
        with pytest.raises(ValueError):
            cc = ChecksumCalculator(sentence)

    def test_init_success(self):
        sentence = 'any'
        cc = ChecksumCalculator(sentence)
        assert cc.sentence == sentence

    @pytest.fixture(scope='class')
    def dummy_checksum_calc(self):
        return ChecksumCalculator('DT 300')

    def test_unicode(self, dummy_checksum_calc):
        assert dummy_checksum_calc.unicode() == [68, 84, 32, 51, 48, 48]

    def test_xor(self, dummy_checksum_calc):
        assert dummy_checksum_calc.xor() == 3

    @pytest.mark.parametrize('sentence,result', [('FV', '10'), ('DT 300', '03'), ('GN 30', '2a')])
    def test_checksum(self, sentence, result):
        cc = ChecksumCalculator(sentence)
        assert cc.checksum == result


class TestNMEAMessageComposer:

    def test_str(self):
        nmea_mc = NMEAMessageComposer(sentence='DT 300')
        assert str(nmea_mc) == '$DT 300*03'


class TestNMEAMessageChecker:

    def test_init_success(self):
        nmea_c = NMEAMessageChecker(sentence='FV', received_checksum=10)
        assert nmea_c.sentence == 'FV'
        assert nmea_c.received_checksum == 10

    @pytest.fixture
    def message(self):
        return NMEAMessageChecker(sentence='DT 300', received_checksum='03')

    @pytest.mark.parametrize('sentence,received_checksum,result', [('DT 300', '03', True), ('FV', '09', False)])
    def test_is_valid(self, sentence, received_checksum, result):
        nmea_c = NMEAMessageChecker(sentence, received_checksum)
        assert nmea_c.is_valid() == result
