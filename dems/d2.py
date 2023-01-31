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


@dataclass
class Exposure:
    data: Data[Ti, float]
    long_name: Attr[str] = "Sample exposure time"
    units: Attr[str] = "s"


@dataclass
class Interval:
    data: Data[Ti, float]
    long_name: Attr[str] = "Sample interval time"
    units: Attr[str] = "s"


@dataclass
class Bandwidth:
    data: Data[Ch, float]
    long_name: Attr[str] = "Channel band width"
    units: Attr[str] = "Hz"


@dataclass
class Frequency:
    data: Data[Ch, float]
    long_name: Attr[str] = "Channel center frequency"
    units: Attr[str] = "Hz"


@dataclass
class BeamMajor:
    data: Data[Ch, float]
    long_name: Attr[str] = "Beam major axis"
    units: Attr[str] = "deg"


@dataclass
class BeamMinor:
    data: Data[Ch, float]
    long_name: Attr[str] = "Beam minor axis"
    units: Attr[str] = "deg"


@dataclass
class BeamPA:
    data: Data[Ch, float]
    long_name: Attr[str] = "Beam position angle"
    units: Attr[str] = "deg"


@dataclass
class D2MKIDID:
    data: Data[Ch, int]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID ID"


@dataclass
class D2MKIDType:
    data: Data[Ch, str]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID type"


@dataclass
class D2MKIDFreq:
    data: Data[Ch, str]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID center response frequency"
    units: Attr[str] = "Hz"


@dataclass
class D2RoomChopperState:
    data: Data[Ch, str]
    long_name: Attr[str] = "[DESHIMA 2.0] Room chopper state"


@dataclass
class D2SkyChopperIsopen:
    data: Data[Ch, bool]
    long_name: Attr[str] = "[DESHIMA 2.0] Whether sky chopper is open"


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
    ground_temperature: Coordof[GroundTemperature] = 0.0
    cabin_temperature: Coordof[CabinTemperature] = 0.0
    pressure: Coordof[Pressure] = 0.0
    humidity: Coordof[Pressure] = 0.0
    wind_speed: Coordof[WindSpeed] = 0.0
    wind_direction: Coordof[WindDirection] = 0.0
    exposure: Coordof[Exposure] = 0.0
    interval: Coordof[Interval] = 0.0
    bandwidth: Coordof[Bandwidth] = 0.0
    frequency: Coordof[Frequency] = 0.0
    beam_major: Coordof[BeamMajor] = 0.0
    beam_minor: Coordof[BeamMinor] = 0.0
    beam_pa: Coordof[BeamPA] = 0.0
    observation: Attr[str] = ""
    observer: Attr[str] = ""
    project: Attr[str] = ""
    telescope: Attr[str] = ""
    telescope_coords: Attr[Tuple[float, float, float]] = (0.0, 0.0, 0.0)
    telescope_diameter: Attr[float] = 0.0
    d2_mkid_id: Coordof[D2MKIDID] = 0
    d2_mkid_type: Coordof[D2MKIDType] = ""
    d2_mkid_freq: Coordof[D2MKIDFreq] = 0.0
    d2_roomchopper_state: Coordof[D2RoomChopperState] = ""
    d2_skychopper_isopen: Coordof[D2SkyChopperIsopen] = False
