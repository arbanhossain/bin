import os
import requests
import json
import urllib.request as fetch

api_key = os.environ.get('TUMBLR_API_KEY')
api_base = 'https://api.tumblr.com/v2/blog/'
blog_name = input('blog name: ')
api_base_url = api_base + blog_name + '/posts/photo?api_key=' + api_key

def retrieve_photos(data, directory, offset, total_posts):
    for i in range(20):
        serial_no = offset+i+1
        print(serial_no)
        try:
            image_url = data['response']['posts'][i]['photos'][0]['original_size']['url']
            #print(offset+i+1, "-" , image_url)
            image_download_path = "./{}/".format(directory) + str(serial_no) + image_url[-4:]
            fetch.urlretrieve(image_url, image_download_path)
            print("Saved {} of {} as {}".format(serial_no, total_posts, image_download_path))
        except IndexError:
            print("\nDone!!\n")
            return -1
        except KeyboardInterrupt:
            print("Interrupted!")
            return -1
        except:
            print("Something went wrong")
    return 0

def main():
    response = requests.get(api_base_url)
    base_data = json.loads(response.content.decode('utf-8'))
    total_posts = base_data['response']['total_posts']
    print("Total posts:", total_posts)

    try:
        os.mkdir(blog_name)
        print("Created Folder: {}".format(blog_name))
    except FileExistsError:
        print("Found Exisitng Folder: {}".format(blog_name))

    offset = 0
    while(offset < total_posts+20):
        url = api_base_url + '&offset=' + str(offset)
        data = json.loads(requests.get(url).content.decode('utf-8'))
        res = retrieve_photos(data, blog_name, offset, total_posts)
        if(res != 0): break
        offset += 20

if __name__ == "__main__":
    main()
