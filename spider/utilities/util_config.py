# _*_ coding: utf-8 _*_

"""
util_config.py by xianhu
"""

import re

__all__ = [
    "CONFIG_ERROR_MESSAGE_TM",
    "CONFIG_ERROR_MESSAGE_RE",
    "CONFIG_URL_RE_LEGAL",
    "CONFIG_URL_RE_ILLEGAL",
]

# define the structure of error message for threads_inst/
CONFIG_ERROR_MESSAGE_TM = "priority=%s, keys=%s, deep=%s, url=%s"
CONFIG_ERROR_MESSAGE_RE = re.compile(r"priority=(?P<p>\d+),\s*keys=(?P<k>.+?),\s*deep=(?P<d>\d+),\s*url=(?P<u>.+)$", flags=re.IGNORECASE)

# define the regex for legal urls and illegal urls
CONFIG_URL_RE_LEGAL = re.compile(r"^https?:[^\s]+?\.[^\s]+?", flags=re.IGNORECASE)
CONFIG_URL_RE_ILLEGAL = re.compile(
    r"\.(cab|iso|zip|rar|tar|gz|bz2|7z|tgz|apk|exe|app|pkg|bmg|rpm|deb|dmg|jar|jad|bin|msi|"
    "pdf|doc|docx|xls|xlsx|ppt|pptx|txt|md|odf|odt|rtf|py|java|c|cc|js|css|log|csv|tsv|"
    "jpg|jpeg|png|gif|bmp|xpm|xbm|ico|drm|dxf|eps|psd|pcd|pcx|tif|tiff|"
    "mp3|mp4|swf|mkv|avi|flv|mov|wmv|wma|3gp|mpg|mpeg|mp4a|wav|ogg|rmvb)$", flags=re.IGNORECASE
)
