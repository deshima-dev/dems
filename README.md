# dems

[![Release](https://img.shields.io/pypi/v/dems?label=Release&color=cornflowerblue&style=flat-square)](https://pypi.org/project/dems/)
[![Python](https://img.shields.io/pypi/pyversions/dems?label=Python&color=cornflowerblue&style=flat-square)](https://pypi.org/project/dems/)
[![Downloads](https://img.shields.io/pypi/dm/dems?label=Downloads&color=cornflowerblue&style=flat-square)](https://pepy.tech/project/dems)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.8151950-cornflowerblue?style=flat-square)](https://doi.org/10.5281/zenodo.8151950)
[![Tests](https://img.shields.io/github/actions/workflow/status/deshima-dev/dems/tests.yaml?label=Tests&style=flat-square)](https://github.com/deshima-dev/dems/actions)

DESHIMA measurement set by DataArray

## Installation

```shell
pip install dems==2025.6.1
```

## Usage

```python
from dems.d2 import MS


da = MS.new(
    data=[[0.0, ...], ...],
    mask=[[False, ...], ...],
    weight=[[1.0, ...], ...],
    ...
)
```

## DataArray specifications

| Category | Variable name | Variable type | Description | Units | Default | Data type | DataArray dims | DataArray dtype |
|---|---|---|---|---|---|---|---|---|
| Data | data | Data | Data values | - | - | numpy.ndarray | (time, chan) | - |
|  | mask | Coordinate | Data masks | - | False | numpy.ndarray | (time, chan) | bool |
|  | weight | Coordinate | Data weights | - | 1.0 | numpy.ndarray | (time, chan) | float64 |
|  | long_name | Attribute | Data name | - | "Brightness" | str | - | - |
|  | units | Attribute | Data units | - | "K" | str | - | - |
|  | name | Name | DEMS name | - | "DEMS" | str | - | - |
| Dimensions | time | Dimension | Start time in UTC | - | 1970-01-01T00:00:00.000000000 | numpy.ndarray | (time,) | datetime64[ns] |
|  | chan | Dimension | Channel ID | - | 0 | numpy.ndarray | (chan,) | int64 |
| Labels | observation | Coordinate | Observation label | - | "" | numpy.ndarray | (time,) | str (<U16) |
|  | scan | Coordinate | Scan label | - | "" | numpy.ndarray | (time,) | str (<U16) |
|  | subscan | Coordinate | Sub-scan label | - | "" | numpy.ndarray | (time,) | str (<U16) |
|  | state | Coordinate | State label | - | "" | numpy.ndarray | (time,) | str (<U16) |
|  | beam | Coordinate | Beam label | - | "" | numpy.ndarray | (time,) | str (<U16) |
| Telescope pointing | lon | Coordinate | Sky longitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | lat | Coordinate | Sky latitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | lon_origin | Coordinate | Reference sky longitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | lat_origin | Coordinate | Reference sky latitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | frame | Coordinate | Sky coordinate frame | - | "altaz" | numpy.ndarray | () | str (<U16) |
| Weather information | temperature | Coordinate | Ground atmospheric temperature | K | 0.0 | numpy.ndarray | (time,) | float64 |
|  | pressure | Coordinate | Ground atmospheric pressure | hPa | 0.0 | numpy.ndarray | (time,) | float64 |
|  | humidity | Coordinate | Ground relative humidity | % | 0.0 | numpy.ndarray | (time,) | float64 |
|  | pwv | Coordinate | Precipitable water vapor | mm | 0.0 | numpy.ndarray | (time,) | float64 |
|  | wind_speed | Coordinate | Ground wind speed | m s^-1 | 0.0 | numpy.ndarray | (time,) | float64 |
|  | wind_direction | Coordinate | Ground wind direction | deg | 0.0 | numpy.ndarray | (time,) | float64 |
| Data information | bandwidth | Coordinate | Effective channel bandwidth | Hz | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | frequency | Coordinate | Channel center frequency | Hz | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | beam_major | Coordinate | Beam major axis | deg | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | beam_minor | Coordinate | Beam minor axis | deg | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | beam_pa | Coordinate | Beam position angle | deg | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | exposure | Coordinate | Sample exposure time | s | 0.0 | numpy.ndarray | () | float64 |
|  | interval | Coordinate | Sample interval time | s | 0.0 | numpy.ndarray | () | float64 |
| Observation information | observer | Attribute | Observer name | - | "" | str | - | - |
|  | project | Attribute | Project name | - | "" | str | - | - |
|  | object | Attribute | Object name | - | "" | str | - | - |
|  | telescope_name | Attribute | Telescope name | - | "" | str | - | - |
|  | telescope_diameter | Attribute | Telescope dish diameter | m | 0.0 | float | - | - |
|  | telescope_coordinates | Attribute | Telescope ITRS coordinates | m | (0.0, 0.0, 0.0) | "tuple[float, float, float]" | - | - |
| ASTE specific | aste_cabin_temperature | Coordinate | [ASTE] Cabin temperature | K | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_obs_group | Attribute | [ASTE] Observation group | - | "" | str | - | - |
|  | aste_obs_id | Attribute | [ASTE] Observation ID | - | "" | str | - | - |
|  | aste_obs_project | Attribute | [ASTE] Observation project | - | "" | str | - | - |
|  | aste_obs_file | Attribute | [ASTE] Observation instruction (= observation) | - | "" | str | - | - |
|  | aste_obs_user | Attribute | [ASTE] Observer (= observer) | - | "" | str | - | - |
|  | aste_subref_x | Coordinate | [ASTE] Subreflector offset of X axis | mm | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_subref_y | Coordinate | [ASTE] Subreflector offset of Y axis | mm | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_subref_z | Coordinate | [ASTE] Subreflector offset of Z axis | mm | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_subref_xt | Coordinate | [ASTE] Subreflector rotation of X axis | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_subref_yt | Coordinate | [ASTE] Subreflector rotation of Y axis | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_subref_zt | Coordinate | [ASTE] Subreflector rotation of Z axis | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_misti_lon | Coordinate | [ASTE] MiSTI sky longitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_misti_lat | Coordinate | [ASTE] MiSTI sky latitude | deg | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_misti_pwv | Coordinate | [ASTE] MiSTI measured PWV | mm | 0.0 | numpy.ndarray | (time,) | float64 |
|  | aste_misti_frame | Coordinate | [ASTE] MiSTI sky coordinate frame | - | "altaz" | numpy.ndarray | () | str (<U16) |
| DESHIMA 2.0 specific | d2_mkid_id | Coordinate | [DESHIMA 2.0] MKID master ID (= chan) | - | "" | numpy.ndarray | (chan,) | int64 |
|  | d2_mkid_type | Coordinate | [DESHIMA 2.0] MKID type | - | "" | numpy.ndarray | (chan,) | str (<U16) |
|  | d2_mkid_frequency | Coordinate | [DESHIMA 2.0] MKID center frequency | Hz | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | d2_mkid_q | Coordinate | [DESHIMA 2.0] MKID quality factor | - | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | d2_resp_fwd | Coordinate | [DESHIMA 2.0] Forward efficiency | - | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | d2_resp_p0 | Coordinate | [DESHIMA 2.0] Proportional coefficient of responsivity | K^-0.5 | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | d2_resp_t0 | Coordinate | [DESHIMA 2.0] Correction temperature of responsivity | K | 0.0 | numpy.ndarray | (chan,) | float64 |
|  | d2_roomchopper_isblocking | Coordinate | [DESHIMA 2.0] Whether room chopper is blocking sensor | - | False | numpy.ndarray | (time,) | bool |
|  | d2_skychopper_isblocking | Coordinate | [DESHIMA 2.0] Whether sky chopper is blocking sensor | - | False | numpy.ndarray | (time,) | bool |
|  | d2_ddb_version | Attribute | [DESHIMA 2.0] DDB version | - | "" | str | - | - |
|  | d2_demerge_version | Attribute | [DESHIMA 2.0] demerge version | - | "" | str | - | - |
|  | d2_dems_version | Attribute | [DESHIMA 2.0] DEMS version | - | "" | str | - | - |
|  | d2_merge_datetime | Attribute | [DESHIMA 2.0] Date and time of the data merge | - | - | str | - | - |
|  | d2_merge_options | Attribute | [DESHIMA 2.0] Options passed to the data merge | - | {} | dict[str, Any] | - | - |
