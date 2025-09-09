# # Instagram Scraping using python

# # Module install --> pip install Beautifulsoup4

# from bs4 import BeautifulSoup
# import requests
# import instaloader

# URL = "https://www.instagram.com/{}/"

# def parse_data(s):
#     data={}

#     s = s.plit("-")[0]

#     s = s.split(" ")

#     data['Followers']=s[0]
#     data['Following']=s[2]
#     data['Posts']=s[4]
#     return data


# def scrape_data(username):
#     r = requests.get(URL.format(username))
#     s = BeautifulSoup(r.text,"html.parser")

    

#     meta = s.find("meta",property="og:description")
#     return parse_data(meta).attrs['content']

# if __name__ == "__main__":
#     print(30*"=", "Instagram", 30*"=")
#     username = input("enter the Id:")
#     data = scrape_data(username)
#     print()
#     print(username, "having",data["Followers"],"followers")
#     print(username, "having", data["Following"],"following")
#     print(username,"having", data["Posts"],"post")
#     print(65*"=")

# Nans = instaloader.Instaloader()

# Nans.download_profile(username,profile_pic_only = True)




# Instagram Scraping using Python

# Module install --> pip install BeautifulSoup4 instaloader

from bs4 import BeautifulSoup
import requests
import instaloader

URL = "https://www.instagram.com/{}/"

def parse_data(s):
    data = {}
    s = s.split("-")[0]  # Assuming the format is correct
    s = s.split(" ")

    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape_data(username):
    r = requests.get(URL.format(username))
    
    # Check if the request was successful
    if r.status_code != 200:
        print(f"Failed to retrieve data for {username}. Status code: {r.status_code}")
        return None

    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property="og:description")

    # Check if the meta tag was found
    if meta is None:
        print(f"No meta tag found for username: {username}")
        return None

    # Extract content directly from the meta tag
    return parse_data(meta['content']) # type: ignore
    

if __name__ == "__main__":
    print(30 * "=", "Instagram", 30 * "=")
    username = input("Enter the Id: ")
    data = scrape_data(username)

    if data:  # Check if data is not None
        print()
        print(username, "having", data["Followers"], "followers")
        print(username, "having", data["Following"], "following")
        print(username, "having", data["Posts"], "posts")
        print(65 * "=")

        # Download profile picture using Instaloader
        Nans = instaloader.Instaloader()
        Nans.download_profile(username, profile_pic_only=True)