# This file is part of the pdfsp project
# Copyright (C) 2025 Sermet Pekin
#
# This source code is free software; you can redistribute it and/or
# modify it under the terms of the European Union Public License
# (EUPL), Version 1.2, as published by the European Commission.
#
# You should have received a copy of the EUPL version 1.2 along with this
# program. If not, you can obtain it at:
# <https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>.
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# European Union Public License for more details.
#
# Alternatively, if agreed upon, you may use this code under any later
# version of the EUPL published by the European Commission.

from typing import Callable, Optional, Union, List, Tuple , Generator, Dict
from pathlib import Path
import pandas as pd

T_pandas_df = pd.DataFrame


T_Path = Union[str, Path]
T_OptionalPath = Optional[T_Path]
T_OptionalCallable = Optional[Callable]
T_OptionalStr = Optional[str]
T_OptionalInt = Optional[int]
T_OptionalFloat = Optional[float]
T_OptionalBool = Optional[bool]
T_OptionalTuple = Optional[tuple]
T_OptionalList = Optional[list]
T_OptionalDict = Optional[dict]
T_OptionalAny = Optional[any]
T_OptionalBytes = Optional[bytes]
T_OptionalSet = Optional[set]
T_callable = Callable

T_List_str = List[str]
T_List_path = List[Path]
T_Tuple_str = Tuple[str]
