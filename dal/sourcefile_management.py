from typing import Literal
from os.path import isfile


def save_data(file: str, user_data: str, mode: Literal["a", "w"] = "a"):
    function_res = {
        "SUCCESS": True,
        "ERR_MSG": {},
        "SUCC_MSG": {},
        "RETURN_DATA": None
    }

    file_object = None

    try:
        file_object = open(file=file, mode=mode)
        file_object.write(user_data)
    except BaseException as err:
        function_res["SUCCESS"] = False
        function_res["RETURN_DATA"] = err
        return function_res
    else:
        return function_res
    finally:
        if file_object and (not file_object.closed):
            file_object.close()


def save_iter_data(file: str, data: list[str], mode: Literal["a", "w"] = "a"):
    function_res = {
        "SUCCESS": True,
        "ERR_MSG": {},
        "SUCC_MSG": {},
        "RETURN_DATA": None
    }
    file_object = None

    try:
        file_object = open(file=file, mode=mode)
        file_object.writelines(data)
    except BaseException as err:
        function_res["SUCCESS"] = False
        function_res["RETURN_DATA"] = err
        return function_res
    else:
        return function_res
    finally:
        if file_object and (not file_object.closed):
            file_object.close()


def load_data(file: str) -> list[str]:
    function_res = {
        "SUCCESS": True,
        "ERR_MSG": {},
        "SUCC_MSG": {},
        "RETURN_DATA": None
    }

    if not isfile(file):
        file_object = None
        try:
            file_object = open(file=file, mode="x")
        except BaseException as err:
            function_res["SUCCESS"] = False
            function_res["RETURN_DATA"] = err
            return function_res
        else:
            function_res["RETURN_DATA"] = []
            return []
        finally:
            if file_object and (not file_object.closed):
                file_object.close()

    file_object = None

    try:
        file_object = open(file=file)
        res = file_object.readlines()
    except BaseException as err:
        function_res["SUCCESS"] = False
        function_res["RETURN_DATA"] = err
        return function_res
    else:
        function_res["RETURN_DATA"] = res
        return function_res
    finally:
        if file_object and (not file_object.closed):
            file_object.close()
