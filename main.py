import tweepy

# API keys
api_key = "oFtEvDTIr5RNXApaB16Ilkve5"
api_secrets = "b2XBs8YZZfxW71Wa51hxi04wUdd3yFDIzQMsIbwcTVe884R9Fc"
access_token = "769270874721624064-gH3qwZKSNuZC2M3uz3XtjJBafQVKu0r"
access_secret = "QrCfFYjqkjLrIDKzJKSJqsX57uxhHMmG1SKz4EvuMjSeJ"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

# Making sure that this shit works
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

# khosla ventures latest 5 follows
khoslaventures = api.get_user(screen_name = 'khoslaventures')
khoslaFollows = khoslaventures.friends()
print('Latest Khosla Follows:')
for i in range (0, 5):
    print(str(khoslaFollows[i].screen_name))

# a16z latest 5 follows
a16z = api.get_user(screen_name = 'a16z')
a16zFollows = a16z.friends()
print('Latest a16z Follows:')
for i in range (0, 5):
    print(str(a16zFollows[i].screen_name))


