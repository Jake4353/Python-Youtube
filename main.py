from youtubesearchpython import *
import urllib.request
import json
import urllib
import webbrowser
import inquirer
import subprocess
def main():
    search_input = input('Video Search: ')
    customSearch = CustomSearch(search_input, VideoSortOrder.uploadDate, limit = 20)
    choices = []
    for i in range(5):

        params = {"format": "json", "url": customSearch.result()['result'][i]['link']}

        url = "https://www.youtube.com/oembed"

        query_string = urllib.parse.urlencode(params)

        url = url + "?" + query_string
        with urllib.request.urlopen(url) as response:

            response_text = response.read()

            data = json.loads(response_text.decode())

        choices.append(f"{data['title']} - {customSearch.result()['result'][i]['link']}")
    questions = [
    inquirer.List('size',
                    message="Video Select",
                    choices=choices,
                ),
    ]
    answers = inquirer.prompt(questions)

    urlout = answers['size'].split(' - ')
    print(urlout[1])
    webopen = [
    inquirer.List('webopen',
                    message="Video Actions:",
                    choices=['Download','Open In Webbrowser', '']
                ),
    ]
    webopenurl = inquirer.prompt(webopen)
    if webopenurl['webopen'] == 'Open In Webbrowser':
        print('\n')
        webbrowser.open(urlout[1])
        print('Done')
    elif webopenurl['webopen'] == 'Download':
            print('\n')
            subprocess.Popen(f'pytube {urlout[1]}')
            print('Done')
            
    else:
        print('\n')
        
while True:
    main()
