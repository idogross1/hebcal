import requests
from Date import Date

def main():
    response = requests.get("https://www.hebcal.com/converter?cfg=json&hy=5749&hm=Kislev&hd=25&h2g=1")
    date = response.json()
    print(date['gy'])
    
    year = input("enter hebrew year:")
    month = input("enter hebrew month:")
    day = input("enter hebrew day:")
    heb_date = Date(year, month, day)
    


if __name__ == '__main__':
    main()