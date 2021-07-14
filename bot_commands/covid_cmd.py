from bs4 import BeautifulSoup
import requests

# COVID-19 data will come from "https://www.worldometers.info/coronavirus/" 
# via webscraping as it has the most current live-statistics for COVID-19.

def webscrape_coronavirus_data(country_name):

    country_name = country_name.lower()
    # This if statement is necessary because of the website's URL pattern
    if country_name == "america" or country_name == "usa" or country_name == "united states":
        country_name = "us"

    try:
        # To match the URL pattern of the worldometers.info website
        data = requests.get("https://www.worldometers.info/coronavirus/country/" + country_name + "/")   
        soup = BeautifulSoup(data.text, "html.parser")

        aggregate_coronavirus_info = soup.find_all("div", {"class": "maincounter-number"})
        # print(aggregate_coronavirus_info)

        # ----- SCRAPE CASES

        # This loop actually finds 3 elements. 1st element is the actual 
        # number I'm looking for (Coronavirus cases total globally),
        # 2nd element is None, 3rd element is also None. I only want the 1st element.
        # Thus I will append all results to a temporary list then print only the 1st one
        temp_list = []
        for i in aggregate_coronavirus_info:
            tempFinder = i.find("span", {"style": "color:#aaa"})           
            temp_list.append(tempFinder)                                        
                                                                                
        cases = temp_list[0].text
        cases = str(cases)            # Making it a string just so that it is clear in the future
        cases = cases.strip()
        # print(cases)

        # ----- SCRAPE DEATHS

        # This loop finds 3 elements, we only want the 2nd element,
        # thus I will once again append everything to a temporary list, 
        # then print only the 2nd element in the temporary list
        temp_list2 = []
        for i in aggregate_coronavirus_info:                                   
            temp_list2.append(i)                          

        deaths = temp_list2[1].text
        deaths = str(deaths)
        deaths = deaths.strip()       # Remove whitespace using the built-in .strip()
        # print(deaths)

        # ----- SCRAPE RECOVERIES

        # This loop finds 3 elements, we only want the 3rd element,
        # thus I will once again append everything to a temporary list, 
        # then print only the 3rd element in the temporary list
        temp_list3 = []
        for i in aggregate_coronavirus_info:                                    
            temp_list3.append(i)                                                

        recoveries = temp_list3[2].text
        recoveries = str(recoveries)
        recoveries = recoveries.strip()    # Remove whitespace using the built-in .strip()
        # print(recoveries)

        # ----- SCRAPE LAST UPDATED TIME

        temp_list4 = []
        last_updated = soup.find_all("div", {"style": "font-size:13px; color:#999; text-align:center"})
        for i in last_updated:
            temp_list4.append(i)

        last_updated = temp_list4[0].text
        last_updated = str(last_updated)
        # print(last_updated)

        # Need to remove the commas in the numbers so mathematical operations can be performed on them
        cases = cases.replace(",", "")
        deaths = deaths.replace(",", "")           
        recoveries = recoveries.replace(",", "")

        cases = int(cases)
        deaths = int(deaths)
        recoveries = int(recoveries)

        fatality_rate = ( float(deaths) / (float(deaths) + float(recoveries) )) * 100.0
        fatality_rate = str(round(fatality_rate, 4)) + "%"


        # When the user inputs "canada" for instance, it will become "Canada", without the quotations
        country_name = country_name.title()            


        cases = (f"{cases:,}")
        deaths = (f"{deaths:,}")
        recoveries = (f"{recoveries:,}")
        return(country_name, cases, deaths, recoveries, fatality_rate, last_updated)
    except:
        return("```Error. Example of proper usage:\n\n%covid canada```")