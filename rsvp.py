import requests

def main():

    cities_file=open("cities.txt", "r")
    for line in cities_file:
        city = cities_file.readline()
        city = city.strip()
        url = "https://governor.arkansas.gov/" + city + "-town-hall-rsvp/"
        try:
            r = requests.get(url)
            # print(url + "\tStatus: " + str(r.status_code))
            if(r.status_code != 404):
                print(url + " is a valid RSVP link")
            else:
                print(city + " does not have a valid RSVP link")
        except Exception as e:
            print(url + "\tNA FAILED TO CONNECT\t" + str(e))

if __name__ == '__main__':
    main()




