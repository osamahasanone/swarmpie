import pytest
from ..command import Command
from ..errors.command_errors import *


class TestCommand:

    @pytest.mark.parametrize('unkown_verb', [None, '', 'XX'])
    def test_init_fail_verb(self, unkown_verb):
        with pytest.raises(UnkownVerbError):
            c = Command(verb=unkown_verb, parameters=[])

    @pytest.mark.parametrize('verb', ['fv', 'FV'])
    def test_success_verb(self, verb):
        c = Command(verb=verb, parameters=[])
        assert c.verb == verb.upper()

    @pytest.fixture(scope='class')
    def no_params_verbs(self):
        return ['CS', 'FV', 'PO', 'RS']

    @pytest.fixture(scope='class')
    def regular_verbs(self):
        return ['DT', 'GJ', 'GN', 'GS', 'PW', 'RT']

    def test_init_fail(self, no_params_verbs, regular_verbs):
        for verb in no_params_verbs:
            with pytest.raises(ParametersCountError):
                c = Command(verb, ['?'])
        for verb in regular_verbs:
            with pytest.raises(ParametersCountError):
                c = Command(verb, [])
            with pytest.raises(ParametersCountError):
                c = Command(verb, ['?', 'x'])
            with pytest.raises(ParameterBadFormatError):
                c = Command(verb, ['x'])

    def test_init_success(self, no_params_verbs, regular_verbs):
        for verb in no_params_verbs:
            c = Command(verb=verb)
            assert c.verb == verb
            assert c.parameters == []
        for verb in regular_verbs:
            c = Command(verb=verb, parameters=[10])
            assert c.verb == verb
            assert c.parameters == ['10']

    @pytest.mark.parametrize('params', [['@'], [11]])
    def test_init_fail_gp(self, params):
        verb_str = 'GP'
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, [])
        with pytest.raises(ParameterBadFormatError):
            c = Command(verb_str, params)

    @pytest.mark.parametrize('params', [['?'], [0], [1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    def test_init_success_gp(self, params):
        verb_str = 'GP'
        c = Command(verb=verb_str, parameters=params)
        assert c.verb == verb_str
        assert c.parameters == [str(param) for param in params]

    @pytest.mark.parametrize('params', [['C=R'], ['D=U'], ['M=U'], ['N=U']])
    def test_init_fail_mm(self, params):
        verb_str = 'MM'
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, [])
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, ['C=U', 'x'])
        with pytest.raises(ParameterBadFormatError):
            c = Command(verb_str, params)

    @pytest.mark.parametrize('params', [['C=U'], ['C=*'], ['D=123'], ['D=R'], ['D=*'], ['M=123'],
                                        ['M=*'], ['N=D'], ['N=E'], ['N=?'], ['R=123'], ['R=O'], ['R=N']])
    def test_init_success_mm(self, params):
        verb_str = 'MM'
        c = Command(verb=verb_str, parameters=params)
        assert c.verb == verb_str
        assert c.parameters == params

    @pytest.mark.parametrize('params', [['C=R'], ['C=Ur'], ['D=R'], ['L=R']])
    def test_init_fail_mt(self, params):
        verb_str = 'MT'
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, [])
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, ['C=U', 'x'])
        with pytest.raises(ParameterBadFormatError):
            c = Command(verb_str, params)

    @pytest.mark.parametrize('params', [['C=U'], ['D=123'], ['D=U'], ['L=123'], ['L=U']])
    def test_init_success_mt(self, params):
        verb_str = 'MT'
        c = Command(verb=verb_str, parameters=params)
        assert c.verb == verb_str
        assert c.parameters == params

    @pytest.mark.parametrize('params', [['S=3600r'], ['S=any'], ['U=any']])
    def test_init_fail_sl(self, params):
        verb_str = 'SL'
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, [])
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, ['x', 'y'])
        with pytest.raises(ParameterBadFormatError):
            c = Command(verb_str, params)

    @pytest.mark.parametrize('params', [['S=3600'], ['U=2021-10-01 16:57:55']])
    def test_init_success_sl(self, params):
        verb_str = 'SL'
        c = Command(verb=verb_str, parameters=params)
        assert c.verb == verb_str
        assert c.parameters == params

    @pytest.mark.parametrize('params', [['L=N', 'y']])
    def test_init_fail_td(self, params):
        verb_str = 'TD'
        with pytest.raises(ParametersCountError):
            c = Command(verb_str, [])
        with pytest.raises(ParameterBadFormatError):
            c = Command(verb_str, params)

    @pytest.mark.parametrize('params', [['HD=123', 'data'], ['ET=123', 'data'], ['', 'data']])
    def test_init_fail_td(self, params):
        verb_str = 'TD'
        c = Command(verb=verb_str, parameters=params)
        assert c.verb == verb_str
        assert c.parameters == params

    @pytest.mark.parametrize('verb,params,result', [('TD', ['HD=123', 'data'], 'HD=123,data'), ('CS', [], '')])
    def test_parameters_str(self, verb, params, result):
        c = Command(verb=verb, parameters=params)
        assert c.parameters_str == result

    @pytest.mark.parametrize('verb,params,result', [('TD', ['HD=123', 'data'], 'TD HD=123,data'), ('CS', [], 'CS')])
    def test_sentence(self, verb, params, result):
        c = Command(verb=verb, parameters=params)
        assert c.sentence == result

    @pytest.mark.parametrize('verb,params,result', [('TD', ['HD=123', 'data'], '$TD HD=123,data*0d'), ('CS', [], '$CS*10')])
    def test_nmea_message(self, verb, params, result):
        c = Command(verb=verb, parameters=params)
        assert c.nmea_message == result
