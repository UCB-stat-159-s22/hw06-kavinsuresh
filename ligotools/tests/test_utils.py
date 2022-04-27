#according to Piazza post: Try to write tests that evaluate the output of the functions and try to assert that some features of the output match the expected one (data format, dimensions, evaluations, etc).
#https://piazza.com/class/kykqjx3dgbt406?cid=281
    
from ligotools import utils as util
    
#utils.py tests

#test for whiten function
def test_whiten():
    strain_H1_whiten = util.whiten(strain_H1,psd_H1,dt)
    assert strain_H1_whiten[5] = -216.46858087260148
    
    strain_L1_whiten = util.whiten(strain_L1,psd_L1,dt)
    assert strain_L1_whiten[5] = 247.40313201197324

from os.path import splitext

#test for write_wavfile function
def test_write_wavfile():
    file_name,extension = splitext(eventname+"_template_whiten.wav") 
    assert extension == ".wav"

#test for reqshift function
def test_reqshift():
    strain_H1_shifted = util.reqshift(strain_H1_whitenbp)
    assert strain_H1_shifted == -1207.162679046647
    strain_L1_shifted = util.reqshift(strain_L1_whitenbp)
    assert strain_L1_shifted[5] == 742.8116050990639
    
#test for plot_function
#assert erroring out on bad inputs
def test_plot_function():
    try:
        time = [10000,100000]
        timemax = 1000
        SNR = [0, 1]
        pcolor = 'g'
        det = "L1"
        eventname = "GW150914"
        plottype = "png"
        tevent = 1126259462.44
        strain_whitenbp = [0, 1]
        template_match = [0, 1]
        template_fft = [0, 1]
        datafreq = [0, 1]
        d_eff = 999.743130306333
        freqs = [0, 1]
        data_psd = [0, 1]
        fs = 4096
        util.plot_function(time, timemax, SNR, pcolor, det, eventname, 
                                    plottype, tevent, strain_whitenbp, template_match, 
                                    template_fft, datafreq, d_eff, freqs, data_psd, fs)   
        assert False
    except Exception:
        assert True


