# File          : L00163434_Q2_File_2
# Author        : K. Snehal
# Version       : v1.0.0
# Licencing     : (C) 2021 Snehal Khairnar, LYIT
#                 Available under GNU Public License (GPL)
# Description   : Webpage Heading, word count
# ----------------------------------


import re
import requests
from bs4 import BeautifulSoup


def read_header():
    """ target url """
    url = 'http://192.168.147.128/'

    """making requests instance """
    res = requests.get(url)

    """ using the BeautifulSoup module """
    soup = BeautifulSoup(res.text, 'html.parser')

    print("Headings of the page are :")
    str1 = soup.find_all("span")
    for line in str1:
        """ Printing heading of the webpage """
        print(line.get_text().lstrip())

    str2 = soup.find_all('div', class_="section_header")
    for row in str2:
        str3 = row.get_text()
        print(str3.strip())

    """ Printing heading of the webpage """
    print("{0}".format(str3[0]))

    """Printing Apache2 word count on the webpage """
    print("Apache2 word count : {} ".format(len(soup.find_all(string=re.compile("Apache2")))))
    print("")

    bold_line = soup.find_all("b")
    bold_line1 = soup.find_all("a")

    print("Bold lines on the webpage are :")

    for lines in bold_line:
        """ printing the bold lines on the webpage """
        print("{}".format(lines.get_text()))

    for row1 in bold_line1:
        val1 = row1.get_text()
        """ printing the bold lines on the webpage """
        print("{}".format(val1))


if __name__ == "__main__":
    '''
          Main method of application 
          Printing webpage heading , word count 
          Parameters:
           none
          Returns:
           none
       '''

    read_header()
