from django.utils import timezone
from ..models import Response, ResponseParameter
from .rph import get_rph


class ResponseInserter:
    def __init__(self, db_command, response_verb, response_parameters):
        self.db_command = db_command
        self.response_verb = response_verb
        self.response_parameters = response_parameters
        self.__factory = {
            'CS': self._insert_cs_response,
            'DT': self._insert_dt_response,
            'FV': self._insert_fv_response,
            'GJ': self._insert_gj_response,
            'GN': self._insert_gn_response,
            'GP': self._insert_gp_response,
            'GS': self._insert_gs_response,
            'MM': self._insert_mm_response,
            'MT': self._insert_mt_response,
            'PO': self._insert_po_response,
            'PW': self._insert_pw_response,
            'RD': self._insert_rd_response,
            'RS': self._insert_rs_response,
            'RT': self._insert_rt_response,
            'SL': self._insert_sl_response,
        }

    def insert(self):
        self.__factory.get(self.response_verb)()

    # general
    def _insert(self, headers):
        response = Response(command=self.db_command)
        response.ts = timezone.now()
        response.save()
        for i, parameter in enumerate(self.response_parameters):
            rp = ResponseParameter(
                response=response, header=get_rph(headers[i]), value=parameter)
            rp.save()

    # specific
    def _insert_cs_response(self):
        self._insert(['app_id', 'dev_id', 'dev_name'])

    def _insert_dt_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['time', 'flag'])

    def _insert_fv_response(self):
        self._insert(['result'])

    def _insert_gj_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['spoof_state', 'jamming_level'])

    def _insert_gn_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['latitude', 'longitude',
                          'altitude', 'course', 'speed'])

    def _insert_gp_response(self):
        self._insert(['result'])

    def _insert_gs_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['hdop', 'vdop', 'gnss_sats', 'unused', 'fix_type'])

    def _insert_mm_response(self):
        if len(self.response_parameters) == 1:
            if self.response_parameters[0] == 'OK':
                self._insert(['result'])
            else:
                self._insert(['msg_count'])
        elif len(self.response_parameters) == 2:
            if self.response_parameters[0] == 'ERR':
                self._insert(['result', 'result_reason'])
            else:
                self._insert(['result', 'msg_id'])
        else:
            self._insert(['data', 'msg_id', 'es'])

    def _insert_mt_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        elif len(self.response_parameters) == 2:
            self._insert(['result', 'result_reason'])
        else:
            self._insert_special_response(['data', 'msg_id', 'es'])

    def _insert_po_response(self):
        self._insert(['result'])

    def _insert_pw_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['unused', 'unused', 'unused', 'unused', 'temp'])

    def _insert_rd_response(self):
        self._insert(['rssi', 'snr', 'fdev', 'data'])

    def _insert_rs_response(self):
        self._insert(['result'])

    def _insert_rt_response(self):
        if len(self.response_parameters) == 1:
            if 'RSSI' in self.response_parameters[0]:
                self._insert(['rssi_background'])
            else:
                self._insert(['result'])
        else:
            self._insert(['rssi_sat', 'snr', 'fdev', 'time', 'sat_id'])

    def _insert_sl_response(self):
        if len(self.response_parameters) == 1:
            self._insert(['result'])
        else:
            self._insert(['result', 'result_reason'])

    def _insert_td_response(self):
        if len(self.response_parameters) == 2:
            self._insert(['result', 'msg_id'])
        elif len(self.response_parameters) == 3:
            self._insert(['result', 'result_reason', 'msg_id'])
        else:
            self._insert(['rssi_sat', 'snr', 'fdev', 'msg_id'])
