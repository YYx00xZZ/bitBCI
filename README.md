# UniBIT-BCI-Study

## OpenVibe Codes
    33025 - motor imagery left
    33026 - motor imagery right

###### How is calculated:
  - _offset_in_rows_ **=** time_size __x__ offset_in_sec
  - _epoch_duration_in_row_ **=** time_size __x__ epoch_research_IN

#### Algos
<details>
  <summary>Loop 1</summary>
  
  * <details>
      <summary>Logical def</summary>

      ```
      Read from CSV
      Get EventId as EventID_NEW
      Next Row
      If EventId = null
          Update Row set EventId = EventID_NEW
      Else
          EventID_NEW = EventId
      Loop to Next Row
      WRITE NEW CSV
      ```
    </details>
  * ```python
    def filter_ids(data):
        EventID_NEW = ''
        EventID_TO_SET = ''
        for index, row in data.iterrows(): #итерираме ред по ред с вградения метод iterrows() от pandas
            EventID_NEW = str(row['EventId']) # достъпваме данни чрез име на колона
            if EventID_NEW == '0':
                data.at[index, 'EventId'] = str(EventID_TO_SET)
            else:
                EventID_NEW = str(row['EventId'])
                EventID_TO_SET = str(row['EventId'])
        return data
    ```
</details>

<details>
  <summary>Loop 2</summary>
  
  * <details>
      <summary>Logical def</summary>

      ```
      Read from CSV
      Filter Row "WHERE EventID = 33025 OR EventID = 33026"
      WRITE NEW CSV
      ```
    </details>
  * ```python
    def filter_events(data):
        """
        Функцията очаква pandas.DataFrame;
        Връща DataFrame съдържащ данни само за ляво и дясно
        """
        data = data[(data.EventId == '33025') | (data.EventId == '33026')]
        return data
    ```
</details>

<details>
  <summary>Loop 3</summary>
  
  * <details>
      <summary>Logical def</summary>

      ```
    ID = 25 # offset
    ID_ALL = 300 # общ брой записи
    ID_CHUNK = 120 # оставащите брой записи в chunk
    ID_MINUS = ID_ALL - ID # оставащи записи след отместването
    ABS(ID_COUNT) = ID_MINUS/ID_CHUNK # брой chunk в оставащите записи като абсолютна стойност.
                                      # След като те зе изброят, се преминава към следващия евент
    COLUMN_1 = 0 # Брояч за пореден chunk глобално
    ID_COUNT_LOOP # Брояч за chunk при превъртането - в случая са два chunk

    ID_MOVE = 1
    READ from CSV as DATA
    Go to row OFFSET
    WHILE NOT DATA EOF
        Get EventId as EventID_NEW
        Next Row
            IF EventID_NEW == EventId 
                ID_COUNT_LOOP = 1
                IF ID_MOVE < ID_CHUNK
                    ID_MOVE = ID_MOVE + 1
                    APPEND COLUMN_1 = COLUMN_1 to DATA
                ELSE
                ID_COUNT_LOOP = ID_COUNT_LOOP + 1
                COLUMN_1 = COLUMN_1 + 1
                IF ID_COUNT_LOOP > ID_COUNT
                    BREAK
            Else
            Go to row.index + OFFSET
            EventID_NEW = EventId
      ```
    </details>
  * ```python

    ```
</details>
