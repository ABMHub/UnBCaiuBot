from time import sleep
from Components.twitter import ping_and_post, search_and_answer
from Components.request import Site

aprender3 = Site("aprender3", "https://aprender3.unb.br/login/index.php")

while True:
  print("Ping and Post")
  ping_and_post(aprender3)
  print("Search and Answer")
  search_and_answer(aprender3)
  sleep(60)