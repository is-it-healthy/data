"""
This script will initialize everything!
"""

import os
import json
import typing as t

with open(
    os.path.join("development", "ins-original.json"), "r", encoding="utf-8"
) as _file:
    data: t.Dict = json.load(_file)

for key, value in data.items():
    with open(
        os.path.join("development", "original-split-single", f"{key}.json"),
        "w",
        encoding="utf-8",
    ) as _file:
        if value:
            json.dump(value, _file, indent=4)
