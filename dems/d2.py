__all__ = ["MS"]


# standard library
from dataclasses import dataclass
from typing import Any, Literal, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Attr, Coordof, Data, Dataof


# type hints
Ti = Literal["time"]
Ch = Literal["chan"]


@dataclass
class Data_:
    data: Data[Tuple[Ti, Ch], Any]
    long_name: Attr[str] = "Data values"


@dataclass
class Mask:
    data: Data[Tuple[Ti, Ch], bool]
    long_name: Attr[str] = "Data masks"


@dataclass
class Weight:
    data: Data[Tuple[Ti, Ch], float]
    long_name: Attr[str] = "Data weights"


@dataclass
class Chan:
    data: Data[Ch, int]
    long_name: Attr[str] = "Generic channel"


@dataclass
class Time:
    data: Data[Ti, Literal["datetime64[ns]"]]
    long_name: Attr[str] = "Start time in UTC"


@dataclass
class Beam:
    data: Data[Ti, str]
    long_name: Attr[str] = "Beam ID"


@dataclass
class Scan:
    data: Data[Ti, str]
    long_name: Attr[str] = "Scan ID"


@dataclass
class State:
    data: Data[Ti, str]
    long_name: Attr[str] = "State ID"


@dataclass(frozen=True)
class MS(AsDataArray):
    """Measurement set of DESHIMA 2.0."""

    data: Dataof[Data_]
    mask: Coordof[Mask] = False
    weight: Coordof[Weight] = 1.0
    time: Coordof[Time] = "2020-01-01"
    chan: Coordof[Chan] = 0
    beam: Coordof[Beam] = ""
    scan: Coordof[Scan] = ""
    state: Coordof[State] = ""
