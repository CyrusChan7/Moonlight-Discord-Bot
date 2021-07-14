from bs4 import BeautifulSoup
import requests


def convert_to_currency(dollar_amount, current_currency, desired_currency):
    # Where dollar_amount is the number of dollars, reals, pesos, etc.
    # Where current_currency is the currency that the user is trying to convert from
    # Where desired_currency is the currency that the user is trying to convert to

    try:                                         
        current_currency = current_currency.lower()         # Ex usd to USD
        desired_currency = desired_currency.lower()         # Ex cad to CAD


        # This works because of the structure of the x-rates.com website
        data = requests.get(f"https://www.x-rates.com/calculator/?"
                            f"from={current_currency}&to={desired_currency}&amount=1")    
        soup = BeautifulSoup(data.text, "html.parser")


        # Ex $1.00 USD = 1.403350 CAD. The website splits the number for some reason so we have to scrape two times
        # for the full 6 decimal places for maximum accuracy.
        # Combining the split conversion rate after scraping them twice
        rate1 = soup.find(class_="ccOutputTrail").previous_sibling             
        rate2 = soup.find(class_="ccOutputTrail").get_text(strip=True)          
        rates_combined = "{}{}".format(rate1, rate2)                            
        rates_combined = float(rates_combined)

        rates_last_updated = soup.find(class_="calOutputTS").get_text(strip=True)

        final_amount = float(dollar_amount) * float(rates_combined)
        final_amount = round(final_amount, 4)
    except:
        return(f"```Error. Example of proper usage:\n\n%convert 50 cad usd```")


    # No matter how weak a currency is the final_amount should never be 0 when dollar_amount isn't 0
    if (float(dollar_amount) != 0 and final_amount == 0) or float(dollar_amount) < 0.0:
        return(f"```Error. Example of proper usage:\n\n%convert 50 cad usd```")
    else:
        # ```text``` is for text formatting in Discord
        return(f"```{dollar_amount} {current_currency.upper()} = "
               f"{final_amount} {desired_currency.upper()}```\nCurrency "
               f"exchange rates last updated {rates_last_updated}")
