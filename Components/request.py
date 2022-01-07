import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class Site:
  def __init__(self, name, url):
    self.name = name
    self.url = url
    self.double_check = True   # evita report de falsa queda
    self.online = self.isOnline()

  def isOnline(self):
    # todo : adicionar condicao especial para caso o computador nao tenha internet
    try:
      r = requests.get(self.url, verify=False).status_code
    except:
      r = 503

    if r == 200:
      self.double_check = False
      self.online = True
      return True

    else:
      if self.double_check is True:
        return False
      
      self.double_check = True
      return True

  