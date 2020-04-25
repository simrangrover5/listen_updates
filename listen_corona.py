

"""This file is for top corona updates you can hear in the morning or anytime with a greet"""
##all together

from gtts import gTTS  #for text to speech conversion
import os #for operating system work
from playsound import playsound
import pandas as pd
import requests
import time

"""Code for greet"""
t = time.ctime().split()[-2][:2]
if int(t)<12:
    greet = "Good Morning"
elif 12<int(t)<17:
    greet = "Good Afternoon"
else:
    greet = "Good Evening"
text = f"{greet} Simran"
language = "en"   #language selected as english


"""Code for top countries and India rank all over the world"""
url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url).content
data = pd.read_html(page)
df = data[0]
country = ""
for i in df[1:6]['Country,Other'].values:
    country+= i + "                 "
sentence1 = f" top five countries suffering is {country}"
india_pos = df[df['Country,Other']=="India"].index.values[0]
india_total = df[df['Country,Other'] == "India"]['TotalCases'].values[0]
sentence2 = f"\n and India is at the position {india_pos} with total cases {india_total}"

"""Code for India updates for to states"""

page = requests.get("https://www.mohfw.gov.in/")
data2 = pd.read_html(page.content)
df2 = data2[0]
index = [32,33,34,35]
for i in index:
    df2.drop(i,inplace=True)
df2['Total Confirmed cases (Including 111 foreign Nationals)'] = df2['Total Confirmed cases (Including 111 foreign Nationals)'].apply(lambda x : int(x))
states = df2.sort_index(by="Total Confirmed cases (Including 111 foreign Nationals)",ascending=False)[:5][['Name of State / UT','Total Confirmed cases (Including 111 foreign Nationals)']].values
sent3 = " Top five states in India with confirmed cases are  "
for i in states:
    sent3 += (i[0]+" "+str(i[1])+"\n")
raj_det = df2[df2['Name of State / UT'] == "Rajasthan"][['Total Confirmed cases (Including 111 foreign Nationals)','Cured/Discharged/Migrated','Death']].values
sent4 = f"In rajasthan the total confirmed cases are {raj_det[0][0]} and death are {raj_det[0][2]}"

final_text ="                                                                          "+text+" "+sentence1+sentence2+sent3+sent4
print(final_text)
mytext = gTTS(text=final_text,lang="en",slow=False)
mytext.save("update.mp3")
playsound("update.mp3")
os.remove("update.mp3")
