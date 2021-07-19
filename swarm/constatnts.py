# if a verb has (n) parameter, it should have list of (n) patterns
_no_params = []
_standard_command = [r'^(\?|@|\d+)$']
verbs_params = {
    'CS': _no_params,
    'DT': _standard_command,
    'FV': _no_params,
    'GJ': _standard_command,
    'GN': _standard_command,
    'GP': [r'^(\?|\d|10)$'],
    'GS': _standard_command,
    'MM': [r'^(C=(U|\*)$)|(D=(\d+|R|\*)$)|(M=(\d+|\*)$)|(N=(D|E|\?)$)|(R=(\d+|O|N)$)',
           ],
    'MT': [r'^(C=U$)|(D=(\d+|U)$)|(L=(\d+|U)$)'],
    'PO': _no_params,
    'PW': _standard_command,
    'RS': _no_params,
    'RT': _standard_command,
    'SL': [r'^(S=\d+$)|(U=[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}$)'],
    'TD': [r'^$|(HD=\d+$)|(ET=\d+$)', r'^.*$']
}

_verbs_re_or = '|'.join(verbs_params.keys())
response_pattern = fr'^\$({_verbs_re_or}) .*\*[0-9a-f][0-9a-f]$'
