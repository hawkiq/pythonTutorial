import urllib.request

def download_image(url,file_path,file_name):
    path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,path)

url = input('Enter Image URL: > ')
file_name = input('FileName to save: ')

download_image(url,'images/',file_name)