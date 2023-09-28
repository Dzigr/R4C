from json import JSONDecodeError, loads

from django.http import JsonResponse


def validate_json(json_data):
    """
    Validate JSON data.

    Parameters: json_data (str): JSON data to be validated.

    Returns: dict or JsonResponse: Valid JSON data or an error JsonResponse.
    """
    try:
        valid_json = loads(json_data)

    except JSONDecodeError as err:
        return JsonResponse(
            data={'error': f'Invalid JSON data: {err}'},
            status=400,
        )

    return valid_json
