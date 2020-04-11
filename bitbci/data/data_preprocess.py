# def prepare_df(): # помощна функция
    # """
    # очаква речник с конфигурационни настройки
    # замества всяко NaN с int(0)
    # връща pandas.DataFrame съдържащ готови за обработка данни (ляво/дясно)
    # """
    # df = pd.read_csv(config['input_file_url'], names=config['names'], index_col=False, header=None, sep=',',skiprows=1, dtype={'EventId' : str})
    # зареждаме входния csv файл от Github
    # df.fillna(0, inplace=True)
    # за всички NaN полета задаваме стойност 0
    #     # алг. 1
    #     df = ef.filter_ids(df) # обхожда данните ред по ред, запълва с ID-та всички клетки в колона EventId
    #     # df.to_csv(config['path_write']+'dev_result-from-alg1.csv', sep=',', index=False)
    #     # алг. 2
    #     df = ef.filter_events(df) # изчиства всички събития които не са с ID 33025 или 33026
    #     # df.to_csv(config['path_write']+'dev_result-from-alg2.csv', sep=',', index=False)
    #    return df  


def populate_NaN(dataframe):
    """ за всички NaN полета задаваме стойност 0 """

    dataframe = dataframe.fillna(0)
    return dataframe


def populate_ids(dataframe):
    """ loop1. Замества ID=0 със съответното правилно """
    EventID_NEW = ''
    EventID_TO_SET = ''
    for index, row in dataframe.iterrows(): #итерираме ред по ред с вградения метод iterrows() от pandas
        EventID_NEW = str(row['EventId']) # достъпваме данни чрез име на колона
        if EventID_NEW == '0':
            dataframe.at[index, 'EventId'] = str(EventID_TO_SET)
        else:
            EventID_NEW = str(row['EventId'])
            EventID_TO_SET = str(row['EventId'])
    return dataframe


def filter_events(dataframe):
    """ loop2.
    Изтрива всички редове които не са с id = 33025 или 33026
    Функцията (generator) очаква pandas.DataFrame;
    Връща (generator) DataFrame съдържащ данни само за ляво и дясно
    """
    dataframe = dataframe[(dataframe.EventId == '33025') | (dataframe.EventId == '33026')]
    return dataframe


# def loop3(data):
#     offset_rows = int(config['time_size'] * config['offset'])
#     epoch_rows = int(config['time_size'] * config['epoch'])
#     idChunk = 12 # 1 чънк съдържа 12 реда ? 120
#     offseted_epoch_rows = epoch_rows - offset_rows # оставащи записи след отместването

#     idMinus = int(offseted_epoch_rows / idChunk)
#     idCount = abs(idMinus)
#     print("idMinus", idMinus, type(idMinus))