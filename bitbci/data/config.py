config_dict = {
    'time_size' : 128, # row count for 1 sec
    'offset' : 0.75, # Отместване в секунди на началото на всяка епоха; ! Cqlo chislo ili gurmi
    'epoch' : 3, # Дължина на епохата по време на експеримента в сек
    
    # Да се добавят стойности
    'chunk_duration_sec_IN' : None, # Дължина на епохата по време на експеримента
    'epoch_duration_IN' : None, # дължина на епохата в редове

    'names' : ['Time128Hz', 'Epoch', 'AF3', 'F7', 'F3', 'F5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4', 'EventId', 'EventDate', 'EventDuration'],
    'channel_columns' : ['AF3', 'F7', 'F3', 'F5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4'],
    'channel_data' : ['Epoch', 'AF3', 'F7', 'F3', 'F5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4', 'EventId'],
    'input_file_url' : 'https://raw.githubusercontent.com/YYx00xZZ/at-UniBIT/master/data/input/1_GD_Standart_14ch_24.01.2020.csv',
    'input_file' : 'D:\\UniBIT-BCI-Study\\data\\input\\1_GD_Standart_14ch_24.01.2020.csv',
    'path_write':'D:\\UniBIT-BCI-Study\\data\\output\\', # 'path_write' : 'D:\\UniBIT-BCI-Study\\data\\output',
    'path_open_class': 'D:\\wondering-python\\BCI\\results\\index_sort_result.csv',
    'test_path' : 'Empty',
    'train_path' : 'Empty',
    'direction' : 'Left',
    'columns_to_test' : 'All',
    'rows_to_chunk_tests' : 12,
    'columns' : 'All',
    'left_event_ID' : 33025,
    'right_event_ID' : 33026,
    'event_ID_after_event_ID' : 'Empty',
    'number_action' : 3,

    'filter_order' : 4,
    'fs' : 128,
    'lowcut' : 8,
    'highcut' : 30
}