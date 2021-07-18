'''contains important information about swarm command parameters'''

# if a verb has (n) parameter, it should have list of (n) patterns
_empty = []
_standard = [r'^(\?|@|\d+)$']
verbs_params = {
    'CS': _empty,
    'DT': _standard,
    'FV': _empty,
    'GJ': _standard,
    'GN': _standard,
    'GP': [r'^(\?|\d|10)$'],
    'GS': _standard,
    'MM': [r'^(C=(U|\*))|(D=(\d+|R|\*))|(M=(\d+|\*))|(N=(D|E|\?))|(R=(\d+|O|N))$',
           ],
    'MT': [r'^(C=U)|(D=(\d+|U))|(L=(\d+|U))$'],
    'PO': _empty,
    'PW': _standard,
    'RS': _empty,
    'RT': _standard,
    'SL': [r'^(S=\d+)|(U=[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2})$'],
    'TD': [r'^$|(HD=\d+)|(ET=\d+)$', r'^.*$']
}
