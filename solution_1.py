import pandas as pd
from math import radians, cos, sin, asin, sqrt

# define a function to calculate the distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))
    return R * c

# read in the trajectory files
T1 = pd.read_csv('T1.csv')
T2 = pd.read_csv('T2.csv')
T2_2 = pd.read_csv('T2_2.csv')
T3 = pd.read_csv('T3.csv')
T4 = pd.read_csv('T4.csv')

# create a list of the pairs of trajectories to consider
pairs = [(T1, T2), (T1, T2_2), (T3, T4)]

# loop through each pair of trajectories
for pair in pairs:
    leader = None
    follower = None
    min_distance = float('inf')
    

        
        
    # loop through each time step
    for t in pair[0]['Time (s)']:
        df1_t = pair[0][pair[0]['Time (s)'] == t]
        df2_t = pair[1][pair[1]['Time (s)'] == t]
        
        if not df1_t.empty and not df2_t.empty:
            lat1, lon1 = df1_t[['Latitude', 'Longitude']].values[0]
            lat2, lon2 = df2_t[['Latitude', 'Longitude']].values[0]
            distance = haversine(lat1, lon1, lat2, lon2)

            # update leader and follower based on distance
            if distance < min_distance:
                min_distance = distance
                if lat1 < lat2:
                    leader = pair[0]
                    follower = pair[1]
                elif lat1 > lat2:
                    leader = pair[1]
                    follower = pair[0]
        else:
            print("No matching time step found for pair:")
            print("\n")
            print(pair)
            print("\n")

        # update leader and follower based on distance
        if distance < min_distance:
            min_distance = distance
            if lat1 < lat2:
                leader = pair[0]
                follower = pair[1]
            elif lat1 > lat2:
                leader = pair[1]
                follower = pair[0]
                
    
    
    print("Leader Is:")
    print("\n")
    print(leader)
    print("\n")
    
    print("Follower Is")
    print("\n")
    print(follower)
    print("\n")