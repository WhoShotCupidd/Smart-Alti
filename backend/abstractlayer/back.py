import random 
import csv
import secret
import itertools


i = 0

predataheader = ['Date', 'Time','deployment', 'exitaltitude', 'freefalltime']
predata = ['05/09/2023', '15:32', '4235', '10245', '63']

recursiveheader = ['altitude', 'speed', 'latitude', 'longitude', 'gyrox', 'gyroy', 'gyroz']
recursicedata = []

altitude = secret.altitude
speed = secret.speed
latitude = secret.l1
longitude = secret.l2
gyrox = secret.x
gyroy = secret.y
gyroz = secret.z



with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    
    writer.writerow(predataheader)
    writer.writerow(predata)
    writer.writerow(recursiveheader)
    
    for (altituded, speedd, latituded, longituded,gyroxd, gyroyd, gyrozd) in zip(altitude, speed, latitude, longitude, gyrox, gyroy, gyroz):
        lis = [altituded, speedd, latituded, longituded, gyroxd, gyroyd, gyrozd]
        writer.writerow(lis)
    