def response_dict(data=None, msg="", stats={}, code=200, print_full_logs=False):
    """
    Usage - return JsonResponse(response_dict(data={}, code=200, print_full_logs=False))
    """
    response = {
        "meta": {"code": code, "message": msg, "data_statistics": stats},
        "data": data,
    }

    '''if print_full_logs:
        log.info("{}-{}".format(response["meta"], response["data"]))'''

    return response