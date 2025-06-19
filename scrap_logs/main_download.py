import requests
from bs4 import BeautifulSoup
from pprint import pprint


def main():
    baseUrl = "https://logs.eolem.com/"
    response = requests.get(baseUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a = [a for a in soup.find_all('a') if a['href'].endswith('.log')]
    
    # pprint(all_a)
    for a in all_a:
        print(baseUrl+a['href'])
        response = requests.get(baseUrl+a['href'])
        with open(a['href'],"w") as f:
            f.write(response.text)


if __name__=='__main__':
    main()
