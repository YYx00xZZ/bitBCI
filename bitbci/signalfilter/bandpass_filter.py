# bandpass филтър
# параметри 
# от конфиг файла
# lowcut - долна граница
# highcut - гора граница
# fs - ???
# order - ред за прилагане н афилтъра

#from scipy.signal import butter, lfilter
import scipy.signal as ss

def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = ss.butter(order, [low, high], btype='band')
    return b, a

# butter филтър - втор афи
# data - данните
# lowcut - долна граница
# highcut - гора граница
# fs - ???
# order - ред за прилагане н афилтъра
def butter_bandpass_filter(data, lowcut, highcut, fs, order):
#     използва горната функция, като тък подаваме вече нашата информация, която искаме да филтрираме
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = ss.lfilter(b, a, data)
    return y

