import pytest
from ..uart import UART


class TestUART:

    @pytest.fixture(scope='class')
    def uart(self):
        return UART(windows=True)

    @pytest.mark.parametrize('message', ['', None])
    def test_prepare_empty_message(self, uart, message):
        with pytest.raises(ValueError):
            uart._prepare_message(message) == 'any'

    @pytest.mark.parametrize('message,result', [('s', b's\n'), ('$DT 300*03', b'$DT 300*03\n')])
    def test_prepare_message(self, uart, message, result):
        assert uart._prepare_message(message) == result

    @pytest.mark.parametrize('line,result', [(b's\n', 's'), (b'$DT 300*03\n', '$DT 300*03')])
    def test_parse_line(self, uart, line, result):
        assert uart._parse_line(line) == result
