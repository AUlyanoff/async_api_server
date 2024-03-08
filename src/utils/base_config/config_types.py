# -*- coding: utf-8 -*-
from enum import IntEnum

from pydantic import FilePath, AfterValidator
from typing_extensions import Annotated

from utils.certificate_utils import validate_cert

X509Certificate = Annotated[
    FilePath,
    AfterValidator(validate_cert)
]
