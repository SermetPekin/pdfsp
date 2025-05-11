from typing import Callable, Optional, Union ,List,Tuple, Generator
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