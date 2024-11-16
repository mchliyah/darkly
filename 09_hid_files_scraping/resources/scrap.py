import requests
import bs4 as bs
import time

url = "http://10.14.59.253/.hidden/"

session = requests.Session()

def recursive_search(url):
    try:
        r = session.get(url)
        if r.status_code == 200:
            s = bs.BeautifulSoup(r.text, 'html.parser')
            if s is not None:
                links = s.find_all("a")
                with open("results.txt", "a+") as f:
                    for link in links:
                        final_link = link.get('href')
                        if final_link == "README":
                            r = session.get(url + final_link)
                            if "Demande" not in r.text and "Toujours" not in r.text and "Tu" not in r.text and "Non" not in r.text:
                                f.write(r.text)
                            # if "flag" in r.text:
                            #     print(r.text)
                            #     exit(0)
                        elif final_link != "../":
                            recursive_search(url + final_link)
    except requests.exceptions.RequestException as e:
        print(f"Error with URL {url}: {e}")

def main(url):
    print(f"Starting scraping on {url}")
    recursive_search(url)

main(url)