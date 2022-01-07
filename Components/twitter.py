from Components.request import Site
from Components.text import timestamp, nice, bad
import tweepy
from Components import auth  # arquivo com 5 variaveis, indicando as chaves do seu twitter
from Components.tweet_log import log

authBot = tweepy.OAuthHandler(auth.API_KEY, auth.API_SECRET_KEY)
authBot.set_access_token(auth.ACCESS_TOKEN, auth.ACCESS_TOKEN_SECRET)
api = tweepy.API(authBot)

try:
  api.verify_credentials()
  print("Authentication OK")
except:
  print("Error during authentication")
  quit()

pesquisa = api.search_tweets(q = "a", result_type = "recent", count = 1)
last_tweet = pesquisa[0].id

def ping_and_post(site : Site):
  online_old = site.online
  online_new = site.isOnline()

  if online_new is not online_old:
    message = f"O {site.name} {'voltou' if site.online else 'caiu'}! - {timestamp}"
    try:
      api.update_status(message)
    except:
      log(f"Tweet failed: {message}")

def search_and_answer(site):
  global last_tweet
  pesquisa = api.search_tweets("@CaiuUnb status", since_id = last_tweet)
  if (len(pesquisa) > 0):
    last_tweet = pesquisa[0].id

    for tweet in pesquisa:
      user = tweet.user.screen_name
      log(f"Mencao respondida, @{user}")
      message = f"@{user}\nO {site.name} está {f'Online {nice}' if site.online else f'Offline {bad}'}"        
      api.update_status(message, in_reply_to_status_id = tweet.id)