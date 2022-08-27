import tweepy
import gspread
import time

# Sheet being used as db: https://docs.google.com/spreadsheets/d/1gf6DMcryo7ldYNgRPvT6XFQkIBEtcPZwXyWTU1Z4Yyc/edit?usp=sharing
sa = gspread.service_account(filename = "service_account.json")
sh = sa.open("twitterSourcer")
wks = sh.worksheet("Data")
allInvestors = sh.worksheet("Investors")


# set the ID for this week
lastWeeksID = wks.acell('A' + str(wks.row_count)).value
thisWeeksID = int(lastWeeksID) + 1

# API keys for Twitter
api_key = "oFtEvDTIr5RNXApaB16Ilkve5"
api_secrets = "b2XBs8YZZfxW71Wa51hxi04wUdd3yFDIzQMsIbwcTVe884R9Fc"
access_token = "769270874721624064-gH3qwZKSNuZC2M3uz3XtjJBafQVKu0r"
access_secret = "QrCfFYjqkjLrIDKzJKSJqsX57uxhHMmG1SKz4EvuMjSeJ"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Making sure that this shit works
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

numRows = allInvestors.row_count
for i in range (0, numRows):
    # get investor info from sheets
    twitterHandle = allInvestors.acell('A' + str((i + 1))).value
    vcName = allInvestors.acell('B' + str((i + 1))).value
    
    # get latest 5 each investor twitter account follows
    twitterUser = api.get_user(screen_name = twitterHandle)
    twitterFollows = twitterUser.friends()
    
    for i in range (0, 5):
        wks.append_row([thisWeeksID, (str(twitterFollows[i].screen_name) + '_' + vcName), twitterFollows[i].screen_name, vcName, twitterFollows[i].description, str(twitterUser.screen_name), twitterUser.description])
    time.sleep(5)