import time

# emojis
nice = '\u2705'
bad = '\u274c'

def timestamp():
  return time.strftime("%d %b %Y %H:%M:%S", time.localtime(time.time()))