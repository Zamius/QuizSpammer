from time import perf_counter, sleep as s
import pyautogui as spammer
import sys

START = perf_counter()
spammer.PAUSE = 0.00001

#REPLACE LIST CONTENT WITH THE CORRECT ANSWERS OF THE QUIZ YOU WANT, THESE ARE FOR
#https://www.jetpunk.com/quizzes/how-many-states-can-you-name
#https://www.jetpunk.com/quizzes/how-many-countries-can-you-name

countries = ['Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia',
             'Bulgaria', 'Croatia', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
             'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg',
             'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Fyrom', 'Norway', 'Poland', 'Portugal',
             'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
             'Uk', 'Ukraine', 'Vatican', 'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan',
             'Brunei', 'Cambodia', 'China', 'Cyprus', 'East Timor', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq',
             'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives',
             'Mongolia', 'Myanmar', 'Nepal', 'NorthKorea', 'Oman', 'Pakistan', 'Philippines', 'Qatar', 'SaudiArabia', 'Singapore',
             'SouthKorea', 'SriLanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Turkey', 'Turkmenistan', 'Uae',
             'Uzbekistan', 'Vietnam', 'Yemen', 'Algeria', 'Angola', 'Benin', 'Botswana', 'BurkinaFaso', 'Burundi',
             'Cameroon', 'CapeVerde', 'Car', 'Chad', 'Comoros', 'Congo', 'Djibouti', 'Egypt', 'EquatorialGuinea', 'Eritrea', 'Eswatini',
             'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'GuineaBissau', 'Cotedivoire', 'Kenya', 'Lesotho', 'Liberia', 'Libya',
             'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
             'Dominica', 'Dr', 'Rwanda', 'Saotome', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia',
             'SouthSudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe', 'Southafrica',
             'Australia', 'Micronesia', 'Fiji','Kiribati','MarshallIslands','Nauru','NZ','Palau','PapuaNewGuinea', 'Samoa',
             'SolomonIslands', 'Tonga', 'Tuvalu', 'Vanuatu', 'Antigua', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'CostaRica',
             'Cuba', 'ElSalvador', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica',
             'Mexico', 'Nicaragua', 'Panama', 'SaintKitts', 'SaintLucia', 'SaintVincent', 'Grenada',
             'Trinidad', 'USA','Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay',
             'Peru', 'Suriname', 'Uruguay', 'Venezuela']

us_states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware',
             'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Massachusetts',
             'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana', 'North Carolina', 'North Dakota', 'Nebraska',
             'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
             'South Carolina','South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']

def alternative():
    global countries
    
    print("Sending: " + str(len(countries) + 1) + " countries!")
   
    s(5) #The seconds you have before the spammer will start, try to time it with the quiz start!
    for c in countries:
        spammer.typewrite(c.lower(), interval=0)

choice = input("Countries of the world quiz or US states quiz? ([C/USA] ~ Default: C): ")
if choice.upper() == "USA":
    print("Sending: 50 states!")
    
    s(5)
    for state in us_states:
        spammer.typewrite(state, interval=0)
    
else:
    alternative()

FINISH = perf_counter()

print(f"Finished in: {round(FINISH-START,2)} seconds!")
input()
