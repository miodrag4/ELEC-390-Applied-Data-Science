import requests
from bs4 import BeautifulSoup

# Request the website and store the HTML in a variable
http_text = requests.get('https://weather.com/en-CA/weather/tenday/l/63f4de10a8c7b229661a9674a3d0915b9740827451d381e82b730ca1b96bbbf5#detailIndex5').text

# Create a BeautifulSoup object
soup = BeautifulSoup(http_text, 'lxml')

# Finds the div with the class 'DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF'
weather_data = soup.find_all('div', class_="DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF")

count = 0
final_data = []

# Loops through the weather_data and finds the date, max temp, min temp, weather condition, chance of rain, wind direction, and wind speed
for day in weather_data:
    col = []
    
    # Finds the date
    date = day.find('h3', class_="DetailsSummary--daypartName--kbngc").text
    
    # Finds the max temp and min temp
    temp_section = day.find('div', class_="DetailsSummary--temperature--1kVVp")
    span_tags = temp_section.find_all('span')
    max_temp = span_tags[0].text
    min_temp = span_tags[1].text
    # Finds the weather condition
    weather_condition = day.find('div', class_="DetailsSummary--condition--2JmHb").span.text
    chance = day.find('div', class_="DetailsSummary--precip--1a98O").span.text
    
    # Finds the wind direction and wind speed
    wind_section = day.find('div', class_="DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax").span.text
    wind_seperated = wind_section.split()
    wind_direction = wind_seperated[0]
    wind_speed = wind_seperated[1]
    
    # Appends all the data to a list
    data = [date, max_temp, min_temp, weather_condition, chance, wind_direction, wind_speed]
    col.append(data)
    final_data.append(col)
    
################## ORIGINAL OUTOUT ##################

with open('ELEC390_Lab2.txt', 'a') as f:
    print(final_data, file=f)
            
################## OPTIMIZED OUTPUT ##################

with open('ELEC390_Lab2.txt', 'a') as f:
    for col in final_data:
        for data in col:
            print(data, file=f)
        

