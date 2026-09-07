#
import numpy as np
import pandas as pd

#read data
parse=pd.read_csv("telemetry_data(in).csv")

#Find anomoly
anomaly=parse[
    (parse["temperature_c"]>85) |
    (parse["vibration_mm_s"]>15)]

print("Turbines with anomalies:")
print(anomaly["turbine_id"].unique())

