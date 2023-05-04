import pandas as pd
import numpy as np

# define the law for calculating TTC
def calculate_TTC(XL, XF, VL, VF, DL):
    return (XL-XF-DL)/(VL-VF)

# load the trajectories data
T1 = pd.read_csv('T1.csv')
T2 = pd.read_csv('T2.csv')
T2_2 = pd.read_csv('T2_2.csv')
T3 = pd.read_csv('T3.csv')
T4 = pd.read_csv('T4.csv')

# set the vehicle length to 3m
vehicle_length = 3

# calculate the positions of the front bumpers of the vehicles in each trajectory
T1['X'] = np.sqrt((T1['Latitude'] - T1.iloc[0]['Latitude'])**2 + (T1['Longitude'] - T1.iloc[0]['Longitude'])**2)
T2['X'] = np.sqrt((T2['Latitude'] - T2.iloc[0]['Latitude'])**2 + (T2['Longitude'] - T2.iloc[0]['Longitude'])**2)
T2_2['X'] = np.sqrt((T2_2['Latitude'] - T2_2.iloc[0]['Latitude'])**2 + (T2_2['Longitude'] - T2_2.iloc[0]['Longitude'])**2)
T3['X'] = np.sqrt((T3['Latitude'] - T3.iloc[0]['Latitude'])**2 + (T3['Longitude'] - T3.iloc[0]['Longitude'])**2)
T4['X'] = np.sqrt((T4['Latitude'] - T4.iloc[0]['Latitude'])**2 + (T4['Longitude'] - T4.iloc[0]['Longitude'])**2)

# calculate the speeds of the vehicles in each trajectory
T1['V'] = np.append(np.diff(T1['X'])/np.diff(T1['Time (s)']), 0)
T2['V'] = np.append(np.diff(T2['X'])/np.diff(T2['Time (s)']), 0)
T2_2['V'] = np.append(np.diff(T2_2['X'])/np.diff(T2_2['Time (s)']), 0)
T3['V'] = np.append(np.diff(T3['X'])/np.diff(T3['Time (s)']), 0)
T4['V'] = np.append(np.diff(T4['X'])/np.diff(T4['Time (s)']), 0)

# calculate the TTC between each pair of trajectories
T1_T2_TTC = min([calculate_TTC(T2.iloc[i]['X'], T1.iloc[i]['X'], T2.iloc[i]['V'], T1.iloc[i]['V'], vehicle_length) for i in range(min(len(T1), len(T2))) if T1.iloc[i]['X'] < T2.iloc[i]['X']])
T1_T2_2_TTC = min([calculate_TTC(T2_2.iloc[i]['X'], T1.iloc[i]['X'], T2_2.iloc[i]['V'], T1.iloc[i]['V'], vehicle_length) for i in range(min(len(T1), len(T2_2))) if T1.iloc[i]['X'] < T2_2.iloc[i]['X']])
T3_T4_TTC = min([calculate_TTC(T4.iloc[i]['X'], T3.iloc[i]['X'], T4.iloc[i]['V'], T3.iloc[i]['V'], vehicle_length) for i in range(min(len(T3), len(T4))) if T4.iloc[i]['V'] < T3.iloc[i]['V'] and (T4.iloc[i]['V'] - T3.iloc[i]['V']) > 0], default=0)