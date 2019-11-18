import pytest

import se_ss
from se_ss.tests import sample


@pytest.mark.parametrize(
    "buff",
    [
        sample("at_night.bin"),
        sample("at_081441.bin"),
        sample("at_081503.bin"),
        sample("at_082848.bin"),
        sample("at_104830.bin"),
        sample("at_131908.bin"),
        sample("at_140452.bin"),
        sample("at_143216.bin"),
        sample("at_151910.bin"),
    ],
)
def test_parse(buff):
    assert se_ss.entries[0].extract(buff) == 0x53756E53
    assert (
        se_ss.entries_by_name["C_Manufacturer"].raw(buff)
        == b"SolarEdge \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    )
    assert (
        se_ss.entries_by_name["C_Model"].raw(buff)
        == b"SE5000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    )
    assert (
        se_ss.entries_by_name["C_Version"].raw(buff)
        == b"0003.2173\x00\x00\x00\x00\x00\x00\x00"
    )
    assert (
        se_ss.entries_by_name["C_SerialNumber"].raw(buff)
        == b"F1234567\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    )
    assert se_ss.entries_by_name["C_Manufacturer"].extract(buff) == "SolarEdge "
    assert se_ss.entries_by_name["C_Model"].extract(buff) == "SE5000"
    assert se_ss.entries_by_name["C_Version"].extract(buff) == "0003.2173"
    assert se_ss.entries_by_name["C_SerialNumber"].extract(buff) == "F1234567"
