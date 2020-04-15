import pandas as pd
import numpy as np
from data.config_reader import configReader
from data.data_preprocess import populate_NaN, populate_ids, filter_events
# from scipy.signal import butter, lfilter
# from signalfilter.butterWorth import butterWorth_data
from signalfilter import filtering

def prepare_data(dataframe):
    """ Pipeline """

    df = filter_events(populate_ids(populate_NaN(dataframe)))
    return df

def main():
    config = configReader()

    df = pd.read_csv(config['input_file_url'], names=config['names'], index_col=False, header=None, sep=',',skiprows=1, dtype={'EventId' : str})
    # зареждаме входния csv файл от Github

    data = prepare_data(df)
    data.to_csv('tt.csv', sep=',')
    # dataframe който съдържа само ивенти left/right

    # fdata = filtering.butter_bandpass_filter(
    #     data,
    #     config['lowcut'],
    #     config['highcut'],
    #     config['fs'],
    #     config['filter_order'])

    # print(fdata)

if __name__ == '__main__':
    main()