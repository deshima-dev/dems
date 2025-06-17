__all__ = [
    "CUBE_DIMS",
    "MS_DIMS",
    "Cube",
    "MS",
]


# standard library
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal, Tuple


# dependencies
from xarray_dataclasses import AsDataArray, Attr, Coordof, Data, Name
from . import __version__


# type hints
Ti = Literal["time"]
Ch = Literal["chan"]
Lt = Literal["lat"]
Ln = Literal["lon"]


# constants
CUBE_DIMS = "chan", "lat", "lon"
MS_DIMS = "time", "chan"


# sub-specs for dimensions
@dataclass
class Time_:
    data: Data[Ti, Literal["datetime64[ns]"]]
    long_name: Attr[str] = "Start time in UTC"


@dataclass
class Chan_:
    data: Data[Ch, int]
    long_name: Attr[str] = "Channel ID"


@dataclass
class Lat_:
    data: Data[Lt, float]
    long_name: Attr[str] = "Sky latitude"
    units: Attr[str] = "deg"


@dataclass
class Lon_:
    data: Data[Ln, float]
    long_name: Attr[str] = "Sky longitude"
    units: Attr[str] = "deg"


# sub-specs for coordinates
@dataclass
class Mask:
    data: Data[Tuple[Ti, Ch], bool]
    long_name: Attr[str] = "Data masks"


@dataclass
class Weight:
    data: Data[Tuple[Ti, Ch], float]
    long_name: Attr[str] = "Data weights"


@dataclass
class CubeMask:
    data: Data[Tuple[Ch, Lt, Ln], bool]
    long_name: Attr[str] = "Data masks"


@dataclass
class CubeWeight:
    data: Data[Tuple[Ch, Lt, Ln], float]
    long_name: Attr[str] = "Data weights"


@dataclass
class Observation:
    data: Data[Ti, Literal["U16"]]
    long_name: Attr[str] = "Observation label"


@dataclass
class Scan:
    data: Data[Ti, Literal["U16"]]
    long_name: Attr[str] = "Scan label"


@dataclass
class Subscan:
    data: Data[Ti, Literal["U16"]]
    long_name: Attr[str] = "Sub-scan label"


@dataclass
class State:
    data: Data[Ti, Literal["U16"]]
    long_name: Attr[str] = "State label"


@dataclass
class Beam:
    data: Data[Ti, Literal["U16"]]
    long_name: Attr[str] = "Beam label"


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
    data: Data[Ti, float]
    long_name: Attr[str] = "Reference sky longitude"
    units: Attr[str] = "deg"


@dataclass
class LatOrigin:
    data: Data[Ti, float]
    long_name: Attr[str] = "Reference sky latitude"
    units: Attr[str] = "deg"


@dataclass
class Frame:
    data: Data[Tuple[()], Literal["U16"]]
    long_name: Attr[str] = "Sky coordinate frame"


@dataclass
class Temperature:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground atmospheric temperature"
    units: Attr[str] = "K"


@dataclass
class Pressure:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground atmospheric pressure"
    units: Attr[str] = "hPa"


@dataclass
class Humidity:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground relative humidity"
    units: Attr[str] = "%"


@dataclass
class PWV:
    data: Data[Ti, float]
    long_name: Attr[str] = "Precipitable water vapor"
    units: Attr[str] = "mm"


@dataclass
class WindSpeed:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground wind speed"
    units: Attr[str] = "m s^-1"


@dataclass
class WindDirection:
    data: Data[Ti, float]
    long_name: Attr[str] = "Ground wind direction"
    units: Attr[str] = "deg"


@dataclass
class Bandwidth:
    data: Data[Ch, float]
    long_name: Attr[str] = "Effective channel bandwidth"
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
class BeamPa:
    data: Data[Ch, float]
    long_name: Attr[str] = "Beam position angle"
    units: Attr[str] = "deg"


@dataclass
class Exposure:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "Sample exposure time"
    units: Attr[str] = "s"


@dataclass
class Interval:
    data: Data[Tuple[()], float]
    long_name: Attr[str] = "Sample interval time"
    units: Attr[str] = "s"


@dataclass
class AsteCabinTemperature:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Cabin temperature"
    units: Attr[str] = "K"


@dataclass
class AsteSubrefX:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector offset of X axis"
    units: Attr[str] = "mm"


@dataclass
class AsteSubrefY:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector offset of Y axis"
    units: Attr[str] = "mm"


@dataclass
class AsteSubrefZ:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector offset of Z axis"
    units: Attr[str] = "mm"


@dataclass
class AsteSubrefXt:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector rotation of X axis"
    units: Attr[str] = "deg"


@dataclass
class AsteSubrefYt:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector rotation of Y axis"
    units: Attr[str] = "deg"


@dataclass
class AsteSubrefZt:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] Subreflector rotation of Z axis"
    units: Attr[str] = "deg"


@dataclass
class AsteMistiLon:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] MiSTI sky longitude"
    units: Attr[str] = "deg"


@dataclass
class AsteMistiLat:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] MiSTI sky latitude"
    units: Attr[str] = "deg"


@dataclass
class AsteMistiPwv:
    data: Data[Ti, float]
    long_name: Attr[str] = "[ASTE] MiSTI measured PWV"
    units: Attr[str] = "mm"


@dataclass
class AsteMistiFrame:
    data: Data[Tuple[()], Literal["U16"]]
    long_name: Attr[str] = "[ASTE] MiSTI sky coordinate frame"


@dataclass
class D2MkidId:
    data: Data[Ch, int]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID master ID"


@dataclass
class D2MkidType:
    data: Data[Ch, Literal["U16"]]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID type"


@dataclass
class D2MkidFrequency:
    data: Data[Ch, float]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID center frequency"
    units: Attr[str] = "Hz"


@dataclass
class D2MkidQ:
    data: Data[Ch, float]
    long_name: Attr[str] = "[DESHIMA 2.0] MKID quality factor"


@dataclass
class D2RespFwd:
    data: Data[Ch, float]
    long_name: Attr[str] = "[DESHIMA 2.0] Forward efficiency"


@dataclass
class D2RespP0:
    data: Data[Ch, float]
    long_name: Attr[str] = "[DESHIMA 2.0] Proportional coefficient of responsivity"
    units: Attr[str] = "K^-0.5"


@dataclass
class D2RespT0:
    data: Data[Ch, float]
    long_name: Attr[str] = "[DESHIMA 2.0] Correction temperature of responsivity"
    units: Attr[str] = "K"


@dataclass
class D2RoomchopperIsblocking:
    data: Data[Ti, bool]
    long_name: Attr[str] = "[DESHIMA 2.0] Whether room chopper is blocking sensor"


@dataclass
class D2SkychopperIsblocking:
    data: Data[Ti, bool]
    long_name: Attr[str] = "[DESHIMA 2.0] Whether sky chopper is blocking sensor"


@dataclass
class MS(AsDataArray):
    """Measurement set of DESHIMA 2.0."""

    # data
    data: Data[Tuple[Ti, Ch], Any]
    mask: Coordof[Mask] = False
    weight: Coordof[Weight] = 1.0
    long_name: Attr[str] = "Brightness"
    units: Attr[str] = "K"
    name: Name[str] = "DEMS"
    # dimensions
    time: Coordof[Time_] = "1970-01-01T00:00:00"
    chan: Coordof[Chan_] = 0
    # labels
    observation: Coordof[Observation] = ""
    scan: Coordof[Scan] = ""
    subscan: Coordof[Subscan] = ""
    state: Coordof[State] = ""
    beam: Coordof[Beam] = ""
    # telescope pointing
    lon: Coordof[Lon] = 0.0
    lat: Coordof[Lat] = 0.0
    lon_origin: Coordof[LonOrigin] = 0.0
    lat_origin: Coordof[LatOrigin] = 0.0
    frame: Coordof[Frame] = "altaz"
    # weather information
    temperature: Coordof[Temperature] = 0.0
    pressure: Coordof[Pressure] = 0.0
    humidity: Coordof[Humidity] = 0.0
    pwv: Coordof[PWV] = 0.0
    wind_speed: Coordof[WindSpeed] = 0.0
    wind_direction: Coordof[WindDirection] = 0.0
    # data information
    bandwidth: Coordof[Bandwidth] = 0.0
    frequency: Coordof[Frequency] = 0.0
    beam_major: Coordof[BeamMajor] = 0.0
    beam_minor: Coordof[BeamMinor] = 0.0
    beam_pa: Coordof[BeamPa] = 0.0
    exposure: Coordof[Exposure] = 0.0
    interval: Coordof[Interval] = 0.0
    # observation information
    observer: Attr[str] = ""
    project: Attr[str] = ""
    object: Attr[str] = ""
    telescope_name: Attr[str] = ""
    telescope_diameter: Attr[float] = 0.0
    telescope_coordinates: Attr[Tuple[float, float, float]] = 0.0, 0.0, 0.0
    # ASTE specific
    aste_cabin_temperature: Coordof[AsteCabinTemperature] = 0.0
    aste_obs_group: Attr[str] = ""
    aste_obs_id: Attr[str] = ""
    aste_obs_project: Attr[str] = ""
    aste_obs_file: Attr[str] = ""
    aste_obs_user: Attr[str] = ""
    aste_subref_x: Coordof[AsteSubrefX] = 0.0
    aste_subref_y: Coordof[AsteSubrefY] = 0.0
    aste_subref_z: Coordof[AsteSubrefZ] = 0.0
    aste_subref_xt: Coordof[AsteSubrefXt] = 0.0
    aste_subref_yt: Coordof[AsteSubrefYt] = 0.0
    aste_subref_zt: Coordof[AsteSubrefZt] = 0.0
    aste_misti_lon: Coordof[AsteMistiLon] = 0.0
    aste_misti_lat: Coordof[AsteMistiLat] = 0.0
    aste_misti_pwv: Coordof[AsteMistiPwv] = 0.0
    aste_misti_frame: Coordof[AsteMistiFrame] = "altaz"
    # DESHIMA 2.0 specific
    d2_mkid_id: Coordof[D2MkidId] = 0
    d2_mkid_type: Coordof[D2MkidType] = ""
    d2_mkid_frequency: Coordof[D2MkidFrequency] = 0.0
    d2_mkid_q: Coordof[D2MkidQ] = 0.0
    d2_resp_fwd: Coordof[D2RespFwd] = 0.0
    d2_resp_p0: Coordof[D2RespP0] = 0.0
    d2_resp_t0: Coordof[D2RespT0] = 0.0
    d2_roomchopper_isblocking: Coordof[D2RoomchopperIsblocking] = False
    d2_skychopper_isblocking: Coordof[D2SkychopperIsblocking] = False
    d2_ddb_version: Attr[str] = ""
    d2_demerge_version: Attr[str] = ""
    d2_dems_version: Attr[str] = field(init=False)
    d2_merge_datetime: Attr[str] = field(init=False)
    d2_merge_options: Attr[dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Set dynamic attributes."""
        self.d2_dems_version = __version__
        self.d2_merge_datetime = datetime.now(timezone.utc).isoformat()


@dataclass
class Cube(AsDataArray):
    """Spectral cube of DESHIMA 2.0."""

    # data
    data: Data[Tuple[Ch, Lt, Ln], Any]
    mask: Coordof[CubeMask] = False
    weight: Coordof[CubeWeight] = 1.0
    long_name: Attr[str] = "Brightness"
    units: Attr[str] = "K"
    name: Name[str] = "Cube"
    # dimensions
    chan: Coordof[Chan_] = 0
    lon: Coordof[Lon_] = 0.0
    lat: Coordof[Lat_] = 0.0
    # telescope pointing
    frame: Coordof[Frame] = "altaz"
    # data information
    bandwidth: Coordof[Bandwidth] = 0.0
    frequency: Coordof[Frequency] = 0.0
    beam_major: Coordof[BeamMajor] = 0.0
    beam_minor: Coordof[BeamMinor] = 0.0
    beam_pa: Coordof[BeamPa] = 0.0
    # observation information
    observer: Attr[str] = ""
    project: Attr[str] = ""
    object: Attr[str] = ""
    telescope_name: Attr[str] = ""
    telescope_diameter: Attr[float] = 0.0
    telescope_coordinates: Attr[Tuple[float, float, float]] = 0.0, 0.0, 0.0
    # ASTE specific
    aste_obs_group: Attr[str] = ""
    aste_obs_id: Attr[str] = ""
    aste_obs_project: Attr[str] = ""
    aste_obs_file: Attr[str] = ""
    aste_obs_user: Attr[str] = ""
    # DESHIMA 2.0 specific
    d2_mkid_id: Coordof[D2MkidId] = 0
    d2_mkid_type: Coordof[D2MkidType] = ""
    d2_mkid_frequency: Coordof[D2MkidFrequency] = 0.0
    d2_mkid_q: Coordof[D2MkidQ] = 0.0
    d2_resp_fwd: Coordof[D2RespFwd] = 0.0
    d2_resp_p0: Coordof[D2RespP0] = 0.0
    d2_resp_t0: Coordof[D2RespT0] = 0.0
    d2_ddb_version: Attr[str] = ""
    d2_demerge_version: Attr[str] = ""
    d2_dems_version: Attr[str] = ""
    d2_merge_datetime: Attr[str] = ""
    d2_merge_options: Attr[dict[str, Any]] = field(default_factory=dict)
