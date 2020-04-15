import pandas as pd
import scipy.signal as ss
from data.config_reader import configReader


config = configReader()

def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = ss.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order):
#     използва горната функция, като тък подаваме вече нашата информация, която искаме да филтрираме
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = ss.lfilter(b, a, data)
    return y


def butterWorth_data(data,channel_columns,lowcut,highcut,fs,order):
    frame = {} #initialize empty dict to store filtered cols
    for column in data[channel_columns]:
    #     print(data[column])
        y = butter_bandpass_filter(data[column], lowcut, highcut, fs, order)
        filtered_column = pd.Series(data=y) #, name=str(column)
        frame.update( { str(column) : filtered_column } )
    # print(frame)

    butter_data = pd.DataFrame(frame)
    butter_data.insert(0,'Time128Hz',data['Time128Hz'])
    butter_data.insert(1,'Epoch',data['Epoch'])
    butter_data.insert(16,'EventId',data['EventId'])
    return butter_data


def test():
    print(config)