from copy import deepcopy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, is_client_error, is_success


class StatusOnly200Mixin(APIView):
    # todo: convert to renderer

    def finalize_response(self, request, response, *args, **kwargs):
        _response = super(StatusOnly200Mixin, self).finalize_response(request, response, *args, **kwargs)
        original_status_code = _response.status_code
        if is_client_error(original_status_code) or is_success(original_status_code):
            _response.status_code = HTTP_200_OK
            if isinstance(_response, Response):
                original_data = deepcopy(_response.data)
                _response.data = {
                    "message": original_data,
                    "code": original_status_code,
                }
        return _response
