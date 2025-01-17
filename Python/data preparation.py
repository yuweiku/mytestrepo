#%%
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import itertools
import os
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)     # Show all rows
pd.set_option('display.max_colwidth', None) # Show full column width
os.getcwd()
#%%
#C:\Users\weile\OneDrive\文件\Python Scripts\Consumer_Risk_Project\Data_Source\application_data.csv
application_data = pd.read_csv(r'C:\Users\weile\OneDrive\文件\Python Scripts\Consumer_Risk_Project\Data_Source\application_data.csv')
previous_application = pd.read_csv(r'C:\Users\weile\OneDrive\文件\Python Scripts\Consumer_Risk_Project\Data_Source\previous_application.csv')
columns_description = pd.read_csv(r'C:\Users\weile\OneDrive\文件\Python Scripts\Consumer_Risk_Project\Data_Source\columns_description.csv',skiprows=1)

#%%

PreA_ID_List = ['SK_ID_CURR']
PreA_Numeric_List= ['CNT_CHILDREN','AMT_INCOME_TOTAL','AMT_CREDIT',	'AMT_ANNUITY','AMT_GOODS_PRICE','REGION_POPULATION_RELATIVE',
               'FLAG_CONT_MOBILE',	'CNT_FAM_MEMBERS','REGION_RATING_CLIENT','REGION_RATING_CLIENT_W_CITY','REG_REGION_NOT_LIVE_REGION',
               'REG_REGION_NOT_WORK_REGION','LIVE_REGION_NOT_WORK_REGION','REG_CITY_NOT_LIVE_CITY','REG_CITY_NOT_WORK_CITY',
               'LIVE_CITY_NOT_WORK_CITY',	'APARTMENTS_AVG','BASEMENTAREA_AVG','COMMONAREA_AVG','ELEVATORS_AVG',	'ENTRANCES_AVG',
               'FLOORSMAX_AVG','FLOORSMIN_AVG','LANDAREA_AVG',	'LIVINGAPARTMENTS_AVG','LIVINGAREA_AVG','NONLIVINGAPARTMENTS_AVG',
               'NONLIVINGAREA_AVG','APARTMENTS_MODE','BASEMENTAREA_MODE','COMMONAREA_MEDI','ELEVATORS_MEDI','ENTRANCES_MEDI',
               'FLOORSMAX_MEDI','FLOORSMIN_MEDI','LANDAREA_MEDI','LIVINGAPARTMENTS_MEDI','LIVINGAREA_MEDI','NONLIVINGAPARTMENTS_MEDI',
               'NONLIVINGAREA_MEDI','TOTALAREA_MODE','OBS_30_CNT_SOCIAL_CIRCLE','DEF_30_CNT_SOCIAL_CIRCLE','OBS_60_CNT_SOCIAL_CIRCLE',
              'DEF_60_CNT_SOCIAL_CIRCLE',	'AMT_REQ_CREDIT_BUREAU_HOUR','AMT_REQ_CREDIT_BUREAU_DAY','AMT_REQ_CREDIT_BUREAU_WEEK',
              'AMT_REQ_CREDIT_BUREAU_MON','AMT_REQ_CREDIT_BUREAU_QRT','AMT_REQ_CREDIT_BUREAU_YEAR']
PreA_time_List = ['DAYS_BIRTH','DAYS_EMPLOYED','DAYS_REGISTRATION',	'DAYS_ID_PUBLISH','OWN_CAR_AGE','WEEKDAY_APPR_PROCESS_START',
             'HOUR_APPR_PROCESS_START','YEARS_BEGINEXPLUATATION_AVG',	'YEARS_BUILD_AVG','YEARS_BEGINEXPLUATATION_MODE','YEARS_BUILD_MODE',
             'DAYS_LAST_PHONE_CHANGE']
PreA_Cat_Multiple_List = ['NAME_CONTRACT_TYPE','CODE_GENDER','NAME_TYPE_SUITE','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS',
                     'NAME_HOUSING_TYPE',	'OCCUPATION_TYPE','ORGANIZATION_TYPE','FONDKAPREMONT_MODE','HOUSETYPE_MODE',	'WALLSMATERIAL_MODE',
                     'EMERGENCYSTATE_MODE']
PreA_Cat_Binomial_List = ['TARGET','FLAG_OWN_CAR','FLAG_OWN_REALTY','FLAG_MOBIL',	'FLAG_EMP_PHONE','FLAG_WORK_PHONE','FLAG_PHONE',	'FLAG_EMAIL',
                     'FLAG_DOCUMENT_2','FLAG_DOCUMENT_3','FLAG_DOCUMENT_4','FLAG_DOCUMENT_5','FLAG_DOCUMENT_6']
PreA_Area_List = ['EXT_SOURCE_1','EXT_SOURCE_2','EXT_SOURCE_3']

#%%

application_data[PreA_ID_List]
application_data[PreA_Numeric_List]
application_data[PreA_time_List]
application_data[PreA_Cat_Multiple_List]
application_data[PreA_Cat_Binomial_List]
application_data[PreA_Area_List]
#%%

#%%
previous_application.columns
#%%