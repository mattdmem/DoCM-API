import json
import os
import requests
import logging
from pyCGA.Exceptions import LoginException, ServerResponseException
from pathlib import Path

__author__ = 'mparker'


class WS:

    def __init__(self, token=None, version="v1", instance="opencga"):

        self.host = "http://docm.genome.wustl.edu"
        self.pre_url = os.path.join(self.host, "api", version)

    @staticmethod
    def check_server_response(response):
        if response == 200 or response == 500:
            return True
        else:
            return False

    def get_result(self, response):
        if response == -1:
            logging.error(response["error"])
            raise ServerResponseException(response["response"][0]["errorMsg"])
        else:
            return response

    def run_ws(self, url, format):
        """

        :param url:
        :return: :raise StandardError:
        """
        response = requests.get(url)
        if self.check_server_response(response.status_code):
            if format == "json":
                return self.get_result(response.json())
            else:
                return self.get_result(response._content)
        else:
            if response.status_code == 404:
               return None
            else:
                logging.error("WS Failed, status: " + str(response.status_code))
                return None
            #raise ServerResponseException("WS Failed, status: " + str(response.status_code))

    def general_method(self, ws_category, format, detail):
        """
        general method for getting results from DOCM

        :param ws_category: variants otherwise list has no category
        :param format: format - for lists the format can be tsv, json, csv
        :param detail: used the list of parameters or for the hgvs
        :return: retrun the WS result
        """
        if ws_category is "list":
            url = os.path.join(self.pre_url, "variants." + format + "?" + detail)
        else:
            url = os.path.join(self.pre_url, ws_category, detail + ".json")
        result = self.run_ws(url, format)
        return result


