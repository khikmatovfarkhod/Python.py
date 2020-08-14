#!/usr/bin/python
##
#

#Open up a series of web pages

#We need a list of urls that we will open

#Open a web page
#Open up a series of tabs

import webbrowser
import time

socialMediaUrls = ["my.bergen.edu"]



def open_tabs(url_list):
    for element in url_list:
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        webbrowser.open_new_tab(element)
        
def main():
    time.sleep(1)
    open_tabs(socialMediaUrls)

main()
