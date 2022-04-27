#according to Piazza post: Try to write tests that evaluate the output of the functions and try to assert that some features of the output match the expected one (data format, dimensions, evaluations, etc).
#https://piazza.com/class/kykqjx3dgbt406?cid=281


#readligo.py tests
from ligotools import loaddata

strain_H1, time_H1, chan_dict_H1 = loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5", 'H1')
strain_L1, time_L1, chan_dict_L1 = loaddata("data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')

def test_output_strain():
    assert strain_H1[1000] == -1.8525877750615284e-20
    assert strain_L1[1000] == -1.1938409727377925e-18

def test_output_time():
    assert time_H1[1000] == 1126259446.2441406
    assert time_L1[1000] == 1126259446.2441406

def test_data_format_chan_dict():
    assert isinstance(chan_dict_H1, dict)
    assert isinstance(chan_dict_L1, dict)
    
def test_dimensions():
    assert len(strain_H1) == 131072
    assert len(strain_L1) == 131072
    assert len(time_H1) == 131072
    assert len(time_L1) == 131072
    assert len(chan_dict_H1) == 13
    assert len(chan_dict_L1) == 13
    
#utils.py tests


