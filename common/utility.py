from os import system
from typing import Any, Hashable, Iterable




def search(data_list: list[dict], key: Hashable, val: Any) -> list[dict]:
    res = []

    for data in data_list:
        if data.get(key) == val:
            res.append(data)

    return res

