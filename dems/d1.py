__all__ = ["MS"]


# standard library
from dataclasses import dataclass
from typing import Any, Literal, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Coord, Data


# type hints
Scalar = Tuple[()]
Time = Literal["t"]
Chan = Literal["ch"]


@dataclass(frozen=True)
class MS(AsDataArray):
    """Measurement set of DESHIMA 1.0."""

    data: Data[Tuple[Time, Chan], Any]
    vrad: Coord[Time, float] = 0.0
    x: Coord[Time, float] = 0.0
    y: Coord[Time, float] = 0.0
    time: Coord[Time, float] = 0.0
    temp: Coord[Time, float] = 0.0
    pressure: Coord[Time, float] = 0.0
    vapor_pressure: Coord[Time, float] = 0.0
    windspd: Coord[Time, float] = 0.0
    winddir: Coord[Time, float] = 0.0
    scantype: Coord[Time, str] = "GRAD"
    scanid: Coord[Time, int] = 0
    masterid: Coord[Chan, int] = 0
    kidid: Coord[Chan, int] = 0
    kidfq: Coord[Chan, float] = 0.0
    kidtp: Coord[Chan, int] = 0
    weight: Coord[Tuple[Time, Chan], float] = 1.0
    coordsys: Coord[Scalar, str] = "RADEC"
    datatype: Coord[Scalar, str] = "Temperature"
    xref: Coord[Scalar, float] = 0.0
    yref: Coord[Scalar, float] = 0.0
    type: Coord[Scalar, str] = "dca"
