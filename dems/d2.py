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


@dataclass
class Lon:
    data: Data[Ti, float]
    long_name: Attr[str] = "Sky longitude"
    units: Attr[str] = "deg"


@dataclass
class Lat:
    data: Data[Ti, float]
    long_name: Attr[str] = "Sky latitude"
    units: Attr[str] = "deg"


@dataclass
class LonOrigin:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "Reference sky longitude"
    units: Attr[str] = "deg"


@dataclass
class LatOrigin:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "Reference sky latitude"
    units: Attr[str] = "deg"


@dataclass
class Frame:
    data: Data[Tuple[()], str]
    long_name: Attr[str] = "Sky coordinate frame"


@dataclass
class TelescopeX:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "ITRS X coordinate of telescope"
    units: Attr[str] = "m"


@dataclass
class TelescopeY:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "ITRS Y coordinate of telescope"
    units: Attr[str] = "m"


@dataclass
class TelescopeZ:
    data: Data[Tuple[()], str]
    long_name: Attr[str] = "ITRS Z coordinate of telescope"
    units: Attr[str] = "m"


@dataclass
class GroundTemperature:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground temperature"
    units: Attr[str] = "K"


@dataclass
class CabinTemperature:
    data: Data[Ti, float]
    long_name: Attr[str] = "Cabin temperature"
    units: Attr[str] = "K"


@dataclass
class Pressure:
    data: Data[Ti, float]
    long_name: Attr[str] = "Atmospheric pressure"
    units: Attr[str] = "Pa"


@dataclass
class Humidity:
    data: Data[Ti, float]
    long_name: Attr[str] = "Relative humidity"
    units: Attr[str] = "%"


@dataclass
class WindSpeed:
    data: Data[Ti, float]
    long_name: Attr[str] = "Wind speed"
    units: Attr[str] = "m/s"


@dataclass
class WindDirection:
    data: Data[Ti, float]
    long_name: Attr[str] = "Wind direction"
    units: Attr[str] = "deg"


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
    lon: Coordof[Lon] = 0.0
    lat: Coordof[Lat] = 0.0
    lon_origin: Coordof[LonOrigin] = 0.0
    lat_origin: Coordof[LatOrigin] = 0.0
    frame: Coordof[Frame] = "altaz"
    telescope_x: Coordof[TelescopeX] = 0.0
    telescope_y: Coordof[TelescopeY] = 0.0
    telescope_z: Coordof[TelescopeZ] = 0.0
    ground_temperature: Coordof[GroundTemperature] = 0.0
    cabin_temperature: Coordof[CabinTemperature] = 0.0
    pressure: Coordof[Pressure] = 0.0
    humidity: Coordof[Pressure] = 0.0
    wind_speed: Coordof[WindSpeed] = 0.0
    wind_direction: Coordof[WindDirection] = 0.0
