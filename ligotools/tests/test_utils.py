#according to Piazza post: Try to write tests that evaluate the output of the functions and try to assert that some features of the output match the expected one (data format, dimensions, evaluations, etc).
#https://piazza.com/class/kykqjx3dgbt406?cid=281
    
from ligotools import utils as util
    
#utils.py tests

def test_whiten():
    strain_H1_whiten = util.whiten(strain_H1,psd_H1,dt)
    assert strain_H1_whiten[5] = -216.46858087260148
    
    strain_L1_whiten = util.whiten(strain_L1,psd_L1,dt)
    assert strain_L1_whiten[5] = 247.40313201197324

from os.path import splitext
def test_write_wavfile():
    file_name,extension = splitext(eventname+"_template_whiten.wav") 
    assert extension == ".wav"

def test_reqshift(data,fshift=100,sample_rate=4096):





