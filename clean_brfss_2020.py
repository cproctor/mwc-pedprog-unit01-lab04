# Clean BRFSS 2020
# ----------------
#
# This module documents the process used to clean and simplify the 
# BRFSS data set used in this lab. Students don't need to interact with this.
# Read more about BRFSS at https://www.cdc.gov/brfss/annual_data/annual_2020.html

# First, download and unzip https://www.cdc.gov/brfss/annual_data/2020/files/LLCP2020XPT.zip
# You should now have a file called LLCP2020.XPT

import pandas as pd
df = pd.read_sas("LLCP2020.XPT")
df = df[odf.DISPCODE == 1100]
df["sex"] = df["SEXVAR"].map({1: "male", 2: "female"})
df = df[df.GENHLTH <= 5]
df["health"] = df.GENHLTH.map({1:5, 2:4, 3:3, 4:2, 5:1})
df = df[df.MEDCOST <= 2]
df["no_doctor"] = df.MEDCOST.map({1: True, 2: False})
df = df[df.EXERANY2 <= 2]
df["exercise"] = df.EXERANY2.map({1: True, 2: False})
df = df[df.SLEPTIM1 < 25]
df["sleep"] = df.SLEPTIM1.astype(int)
df = df[df.INCOME2 < 9]
df["income"] = df.INCOME2.astype(int)
df = df[~df.WTKG3.isna()]
df["weight"] = df.WTKG3 / 100
df = df[~df.HTM4.isna()]
df["height"] = df.HTM4 / 100
df = df[(df.SOFEMALE.isin([1, 2, 3, 4, 7, 9])) | (df.SOMALE.isin([1, 2, 3, 4, 7, 9]))]
df["sexual_orientation"] = df.SOFEMALE
df["sexual_orientation"].fillna(df.SOMALE, inplace=True)
df["sexual_orientation"] = df["sexual_orientation"].map({1: "homosexual", 2: "heterosexual", 3: "bisexual", 4: "other", 7: "other", 9: "other"})
df = df[df._EDUCAG.isin([1, 2, 3, 4])]
df["education"] = df._EDUCAG.map({1: "none_completed", 2: "high_school", 3: "some_college", 4: "college"})
df["age"] = df._AGE_G.map({1: 18, 2: 25, 3: 35, 4: 45, 5: 55, 6: 65})
df = df[["age", "sex", "income", "education", "sexual_orientation", "height", "weight", "health", "no_doctor", "exercise", "sleep"]]
df.to_csv("brfss_2020.csv", index=False)
