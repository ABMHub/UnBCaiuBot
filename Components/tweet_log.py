def log(text):
  print(text)
  f = open("twitter_log.txt", "a")
  f.write(text + '\n')
  f.close()