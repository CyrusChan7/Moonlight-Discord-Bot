from bs4 import BeautifulSoup
import requests


def display_file_information(file_extension):
    """ Returns information regarding a specified file type found on various operating systems."""

    try:
        if "." in file_extension:
            file_extension = file_extension[1:]     # If the input is ".exe", we want it to be "exe". This if statement must be here
                                                    # or else the requests.get() will not work below

        data = requests.get("https://fileinfo.com/extension/" + file_extension)     # This works because of the URL pattern of the website
        soup = BeautifulSoup(data.text, "html.parser")

        aggregate_info = soup.find_all("div", {"class": "infoBox"})
        #print(aggregate_info)

        tempList = []
        for i in aggregate_info:
            tempFinder = i.find("p")
            tempList.append(tempFinder)

        return(tempList[0].text)     # The for loop above gets several elements with HTML tags, but we only want the first element's text
    except:
        return("```Error. Example of proper usage:\n\n%filetype .exe```")