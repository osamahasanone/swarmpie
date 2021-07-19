import pytest
from ..command import Command


class TestCommand:

    def test_unknown_verb(self):
        with pytest.raises(ValueError):
            c = Command(verb='XX', parameters=[])

    def test_create_no_param_command(self):
        no_params_verbs = ['CS', 'FV', 'PO', 'RS']
        for verb in no_params_verbs:
            with pytest.raises(ValueError):
                c = Command(verb, ['?'])
            c = Command(verb=verb)
            assert c.verb == verb
            assert c.parameters == []

    def test_create_standard_command(self):
        standard_verbs = ['DT', 'GJ', 'GN', 'GS', 'PW', 'RT']
        for verb in standard_verbs:
            with pytest.raises(ValueError):
                c = Command(verb, [])
            with pytest.raises(ValueError):
                c = Command(verb, ['x'])
            with pytest.raises(ValueError):
                c = Command(verb, ['?', 'x'])
            c = Command(verb=verb, parameters=[300])
            assert c.verb == verb
            assert c.parameters == ['300']

    def test_create_gp(self):
        verb_str = 'GP'
        with pytest.raises(ValueError):
            c = Command(verb_str, [])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['@'])
        with pytest.raises(ValueError):
            c = Command(verb_str, [11])
        c = Command(verb=verb_str, parameters=['?'])
        assert c.verb == verb_str
        assert c.parameters == ['?']
        for i in range(11):
            c = Command(verb=verb_str, parameters=[i])
            assert c.verb == verb_str
            assert c.parameters == [str(i)]

    def test_create_mm(self):
        verb_str = 'MM'
        with pytest.raises(ValueError):
            c = Command(verb_str, [])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['C=R'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['D=U'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['M=U'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['N=U'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['R=U'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['C=U', 'x'])
        params = ['C=U', 'C=*', 'D=123', 'D=R', 'D=*', 'M=123',
                  'M=*', 'N=D', 'N=E', 'N=?', 'R=123', 'R=O', 'R=N']
        for param in params:
            c = Command(verb=verb_str, parameters=[param])
            assert c.verb == verb_str
            assert c.parameters == [param]

    def test_create_mt(self):
        verb_str = 'MT'
        with pytest.raises(ValueError):
            c = Command(verb_str, [])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['C=R'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['D=R'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['L=R'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['C=U', 'x'])
        params = ['C=U', 'D=123', 'D=U', 'L=123', 'L=U']
        for param in params:
            c = Command(verb=verb_str, parameters=[param])
            assert c.verb == verb_str
            assert c.parameters == [param]

    def test_create_sl(self):
        verb_str = 'SL'
        with pytest.raises(ValueError):
            c = Command(verb_str, [])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['S=any'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['U=any'])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['x', 'y'])
        params = ['S=3600', 'U=2021-10-01 16:57:55']
        for param in params:
            c = Command(verb=verb_str, parameters=[param])
            assert c.verb == verb_str
            assert c.parameters == [param]

    def test_create_td(self):
        verb_str = 'TD'
        with pytest.raises(ValueError):
            c = Command(verb_str, [])
        with pytest.raises(ValueError):
            c = Command(verb_str, ['L=N', 'y'])
        params = [('HD=123', 'data'), ('ET=123', 'data'), ('', 'data')]
        for param in params:
            c = Command(verb=verb_str, parameters=[param[0], param[1]])
            assert c.verb == verb_str
            assert c.parameters == [param[0], param[1]]

    def test_parameters_str(self):
        c = Command(verb='TD', parameters=['HD=123', 'data'])
        assert c.parameters_str == 'HD=123,data'

    def test_sentence(self):
        c = Command(verb='CS')
        assert c.sentence == 'CS'
        c = Command(verb='DT', parameters=[300])
        assert c.sentence == 'DT 300'

    def test_nmea_message(self):
        c = Command(verb='CS')
        assert c.nmea_message == '$CS*10'
        c = Command(verb='DT', parameters=[300])
        assert c.nmea_message == '$DT 300*03'
