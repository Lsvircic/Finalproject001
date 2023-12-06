import webbrowser
webbrowser.open('https://www.nhl.com/stats/')

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.

#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.nhl.com/stats/' + address)


import requests
res = requests.get('https://www.nhl.com/stats/')
type(res)
class 'requests.models.Response'
res.status_code == requests.codes.ok
True
len(res.text)
178981
print(res.text[:250])




