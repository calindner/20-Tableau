import pandas as pd
import numpy as np

for year in range(2014, 2020):
   for month  in range(1,13):
       if month < 10:
               load = (f"city_data/{year}0{month}.csv")
               read = pd.read_csv(load)
               file = pd.DataFrame(read)
               c_name = list(file.columns.values)
               file[c_name[0]] = file[c_name[0]].replace(np.NaN, )
               file[c_name[1]] = file[c_name[1]].replace(np.NaN, )
               file[c_name[2]] = file[c_name[2]].replace(np.NaN, )
               file[c_name[3]] = file[c_name[3]].replace(np.NaN, )
               file[c_name[4]] = file[c_name[4]].replace(np.NaN, )
               file[c_name[5]] = file[c_name[5]].replace(np.NaN, )
               file[c_name[6]] = file[c_name[6]].replace(np.NaN, )
               file[c_name[7]] = file[c_name[7]].replace(np.NaN, )
               file[c_name[8]] = file[c_name[8]].replace(np.NaN, )
               file[c_name[9]] = file[c_name[9]].replace(np.NaN, )
               file[c_name[10]] = file[c_name[10]].replace(np.NaN, )
               file[c_name[11]] = file[c_name[11]].replace(np.NaN, )
               file[c_name[12]] = file[c_name[12]].replace(np.NaN, )
               file[c_name[13]] = file[c_name[13]].replace(np.NaN, )
               file[c_name[14]] = file[c_name[14]].replace(np.NaN, )
               file.dropna()
               file.rename(columns = {c_name[0]: 'trip_duration',
                        c_name[1]: 'start_time',
                         c_name[2]: 'stop_time',
                         c_name[3]: 'start_station_id',
                         c_name[4]: 'start_station_name',
                         c_name[5]: 'start_station_latitude',
                         c_name[6]: 'start_station_longitude',
                         c_name[7]: 'end_station_id',
                         c_name[8]: 'end_station_name',
                         c_name[9]: 'end_station_latitude',
                         c_name[10]: 'end_station_longitude',
                         c_name[11]: 'bike_id',
                         c_name[12]: 'user_type',
                         c_name[13]: 'birth_year',
                         c_name[14]: 'gender'}, inplace=True)
               file.to_csv(f"city_data/{year}_{month}_clean.csv", index=False)

       else:
            load = (f"city_data/{year}{month}.csv")
            read = pd.read_csv(load)
            file = pd.DataFrame(read)
            c_name = list(file.columns.values)
            file[c_name[0]] = file[c_name[0]].replace(np.NaN, )
            file[c_name[1]] = file[c_name[1]].replace(np.NaN, )
            file[c_name[2]] = file[c_name[2]].replace(np.NaN, )
            file[c_name[3]] = file[c_name[3]].replace(np.NaN, )
            file[c_name[4]] = file[c_name[4]].replace(np.NaN, )
            file[c_name[5]] = file[c_name[5]].replace(np.NaN, )
            file[c_name[6]] = file[c_name[6]].replace(np.NaN, )
            file[c_name[7]] = file[c_name[7]].replace(np.NaN, )
            file[c_name[8]] = file[c_name[8]].replace(np.NaN, )
            file[c_name[9]] = file[c_name[9]].replace(np.NaN, )
            file[c_name[10]] = file[c_name[10]].replace(np.NaN, )
            file[c_name[11]] = file[c_name[11]].replace(np.NaN, )
            file[c_name[12]] = file[c_name[12]].replace(np.NaN, )
            file[c_name[13]] = file[c_name[13]].replace(np.NaN, )
            file[c_name[14]] = file[c_name[14]].replace(np.NaN, )
            file.dropna()
            file.rename(columns = {c_name[0]: 'trip_duration',
                        c_name[1]: 'start_time',
                         c_name[2]: 'stop_time',
                         c_name[3]: 'start_station_id',
                         c_name[4]: 'start_station_name',
                         c_name[5]: 'start_station_latitude',
                         c_name[6]: 'start_station_longitude',
                         c_name[7]: 'end_station_id',
                         c_name[8]: 'end_station_name',
                         c_name[9]: 'end_station_latitude',
                         c_name[10]: 'end_station_longitude',
                         c_name[11]: 'bike_id',
                         c_name[12]: 'user_type',
                         c_name[13]: 'birth_year',
                         c_name[14]: 'gender'}, inplace=True)
            file.to_csv(f"city_data/{year}_{month}_clean.csv", index=False)

