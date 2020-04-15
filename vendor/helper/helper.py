""" Helper. """
import os
import json


def getenv():
    """ getenv: for getting application environment. """
    return os.environ.get('ENV', 'development')


def json_to_dict(json_body):
    """ parse_json_body: for parsing json data to dict."""
    return json.loads(json_body) if json_body else {}


def get_serializer_error_message(error_messages):
    """get_serializer_error_message: iterate error message from serializers validator"""
    list_error = []
    for key, value in error_messages.items():
        list_error.append("{} ({})".format(value[0], key))

    return list_error


def get_detail_serializer_error_message(error_messages):
    """get_serializer_error_message: iterate error message from serializers validator"""
    list_error = []
    for key, value in error_messages.items():
        detail_error = {"key": key, "error_message": value[0]}
        list_error.append(detail_error)

    return list_error


def get_detail_serializer_errors(error_messages):
    """get_serializer_error_message: iterate error message from serializers validator"""
    detail_error = {}
    for key, value in error_messages.items():
        detail_error[key] = value[0]

    return detail_error