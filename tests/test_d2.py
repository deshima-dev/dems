# dependencies
from dems.d2 import CUBE_DIMS, MS_DIMS, Cube, MS


# test functions
def test_ms_creation() -> None:
    da = MS.zeros([5, 5])
    assert da.dims == MS_DIMS


def test_cube_creation() -> None:
    da = Cube.zeros([5, 4, 3])
    assert da.dims == CUBE_DIMS
