# itscatoclock-legacy

Back in 2014 or 2015 I decided it would be a great idea to have a Twitter bot telling the time and posting a kitty pic every full hour. I assembled huge collection of cat pics and wrote an ugly Python script to be executed via cron.

I shut down the project due to lack of funds to keep the server running. But I'm working on bringing it back online.

The script is really ugly but it works.

# How do I use this?

The script was written with Python 2.x in mind. Follow the steps below:

1. Assemble your collection of pictures and name them according to the pattern: 000001.jpg, 000002.jpg, 000003.jpg and so on. Leading zeros matter.
2. [Create a Twitter app](https://apps.twitter.com/) and write down your consumer key, consumer secret, access token and access token secret.
3. Copy those details into the script and provide the number of pics in your collection. The script will generate a random number and determine the pic to be uploaded.
4. Set up the script to be executed hourly and you're good to go.

Licensed under [MIT licence](https://bitbucket.org/lwojcik/itscatoclock-legacy/raw/HEAD/LICENSE).