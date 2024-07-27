import requests

def get_data(option="recent_10"):
  print("Getting recent values from the NightScout API")
  
  # nightscout details
  
  # documentation for the API (is not very good)
  #https://nightscout-  test.readthedocs.io/en/latest/Nightscout/EN/Technical%20info/api.html
  
  ns_url = "https://truebell.herokuapp.com/"
  #"https://api.nightscout.com/api/v1/entries/last.json"
  api_version = "/api/v1/"
  # api requests
  recent = "/entries"
  
  # get the data for 10 most recent
  if option == "recent_10":
    url = f"{ns_url}{api_version}{recent}"
  else:
    print("No url for this implelented yet")
    return
  
  response = requests.get(url)
  data = response.content.decode("utf-8").split("\n")
  for row in data:
    tabbed = row.split("\t")
    bg = float(tabbed[2]) / 18.01559 #converson to mmol is 18.01559M
    date_time = tabbed[0].split("T")
    date = date_time[0]
    time = date_time[1]
    arrow = tabbed[3]
    print(round(bg,1),date,time, arrow)
  
  
  