#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import tweepy
import os
from datetime import datetime
from pytz import timezone

def do_the_magic():

    # twitter app config

    consumer_key        = "XXXXXXXXXXXXXXXXXXXXXXXXXXX" # obtain from twitter
    consumer_secret     = "XXXXXXXXXXXXXXXXXXXXXXXXXXX" # obtain from twitter

    access_token        = "XXXXXXXXXXXXXXXXXXXXXXXXXXX" # obtain from twitter
    access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXX" # obtain from twitter

    number_of_images_available = 3134 # unfortunately it really needs to be done by hand

    # hand-shaking

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # choosing the file to upload

    image_number_to_upload = str(random.randint(1, number_of_images_available)).zfill(6)
    random_choice = image_number_to_upload+".jpg"

    # determining timezones and building the status content

    current_status = ""
    time_format = "%H:%M"

    timezonelist = {
        "London": "Europe/London",
        "Warsaw": "Europe/Warsaw",
        "New York": "America/New_York",
        "Sydney": "Australia/Sydney"
    }

    for city, zone in sorted(timezonelist.items()):
        current_status += city + ": " + (datetime.now(timezone(zone))).strftime(time_format) + "\n"

    # figuring out the time and building the string

    while True:
        if (os.path.isfile(random_choice)):
            api.update_with_media(random_choice, current_status)
            break
        else:
            image_number_to_upload = str(random.randint(1, number_of_images_available)).zfill(5)
            random_choice = "/path/to/pics" + image_number_to_upload + ".jpg"
            pass

def main():
    do_the_magic()

if __name__ == "__main__":
    main()