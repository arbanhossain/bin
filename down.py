import requests

def main():
    try:
        url = ''
        while(url == ''):
            url = input("Enter URL: ").replace("https://", "").replace("http://","")
        url = "https://" + url
    except KeyboardInterrupt:
        print('glhf')
        exit()
    try:
        req = requests.get(url)
        code = req.status_code
        status = ""
        if(code == 200): print("Up :D")
        else: print("Down :(")
        
    except requests.exceptions.ConnectionError:
        print('Most probably an invalid domain')
    except request.exceptions.HTTPError:
        print('HTTP Error! Probably invalid status code')
    except requests.exceptions.TooManyRedirects:
        print('Too Many Redirects!!')
    except requests.exceptions.Timeout:
        print('Request timeout! Maybe retry?')
    except requests.exceptions.RequestException:
        print('Dunno what went wrong. imma head out')
    main()

main()
    