import sys
import urllib.request as url

if(len(sys.argv)<2):
    print('pass in the user id')
else:
    try:
        url.urlretrieve("https://graph.facebook.com/"+ sys.argv[1] +"/picture?width=600","photo.jpg")
        print("saved as photo.jpg")
    except:
        print("couldn't get the photo. is the uid correct?")

