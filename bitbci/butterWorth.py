# import numpy as np
# butterWorth_data 
# импортва се butter_bandpass_filter
# от файла bandpass_filter.py



def butterWorth_data(data,channel_columns,lowcut,highcut,fs,order):
    import pandas as pd
    from bandpass_filter import butter_bandpass_filter

#    frame - Dictionary което съдържа филтрираните данни по колони 
    frame = {} #initialize empty dict to store filtered cols
#     channel_columns - само колоните, които съдържат данните от предварително избраните от нас канали , посочени в конфиг файла
    for column in data[channel_columns]:
        
#         
# data[column] - избраните колони 
# lowcut - долна граница
# highcut - гора граница
# fs - ???
# order - ред за прилагане на филтъра
    #print(data[column])
#         y - данни за поредната колона от списъка channel_columns
        y = butter_bandpass_filter(data[column], lowcut, highcut, fs, order)
#     filtered_column - образуваме серия, т.е. всяка колона след филтриране я превръщаме в серия - подреден списък, специфичен за пандас
        filtered_column = pd.Series(data=y) #, name=str(column)
# frame.update - упдейтваме , като заместваме данните във всяка пордена филтрирана колона 
        frame.update( { str(column) : filtered_column } )
    #print(frame)

#     извлечените филтрирани колони , използвайки предварително дефинирания фрейм 
 
    butter_data = pd.DataFrame(frame)
#     Добавяме съответно 
#     Time128Hz
#     Epoch
#     EventId
    butter_data.insert(0,'Time128Hz',data['Time128Hz'])
    butter_data.insert(1,'Epoch',data['Epoch'])
    butter_data.insert(16,'EventId',data['EventId'])
        # print(butter_data)
    return butter_data