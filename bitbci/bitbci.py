import pandas as pd
from data.config_reader import configReader
from data.data_preprocess import populate_NaN, populate_ids, filter_events


def main():
    config = configReader()

    df = pd.read_csv(config['input_file_url'], names=config['names'], index_col=False, header=None, sep=',',skiprows=1, dtype={'EventId' : str})
    # зареждаме входния csv файл от Github
    
    dataframe = populate_NaN(df)
    data = filter_events(dataframe)
    print(type(data))
    print(data.shape)
    print(data.EventId.unique())


if __name__ == '__main__':
    main()