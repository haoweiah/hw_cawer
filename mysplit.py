import requests
import json

def acrn_url_info(url):
    # request data
    response = requests.get(url)
    return json.loads(response.text)

def determine_doc(num):
    url = 'https://api.github.com/repos/projectacrn/acrn-hypervisor/pulls/%s/files' % num
    # file_mod = ['hypervisor', 'devicemodel', 'tools', 'scripts', 'Makefile']
    try:
        file_list = acrn_url_info(url)
        print(file_list)
        for file in file_list:
            file_type = file['filename'].split('/', 1)[0]
            print(file_type)
            if file_type != 'doc':
                return True
    except Exception as e:
        print(e)
    else:
        return False


if __name__ == '__main__':
    type = determine_doc('1120')
    print(type)
