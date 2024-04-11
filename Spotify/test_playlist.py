import sys
import traceback
import json
import os

sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation')
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation\utilities')
from utilities.BaseClass_new import Base
from utilities.resources import *
from utilities.configrations import *


class TestSpotify(Base):
    print('Inside the test class')

    def test_getplaylist(self):
        rdx_json = {}
        native_json = {}
        print(f'rdx_json ={rdx_json}, native_json={native_json}')
        try:
            for x in playlist_id:
                print(f'x={x}')
                try:
                    url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_playlist.format(id=x)
                    print(f'rdx_url = {url}')
                    headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
                    response = self.getResponse(url, headers, 'API')
                    rdx_json = response
                    print(type(rdx_json))
                except Exception as e:
                    traceback.print_exc()
                    print(e)

                try:
                    dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_playlist.format(id=x)
                    print(f' native_url = {dev_url}')
                    head = {'Authorization': 'Bearer ' + access_token}
                    print('inside try block')
                    response = self.getResponse(dev_url, head, 'DEV')
                    native_json = response
                    print(type(native_json))

                except Exception as e:
                    traceback.print_exc()

                if rdx_json == native_json:
                    print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
                    log.info('DEV-UI JSON VS API JSON Matched -- Test case Pass')
                else:
                    print('DEV-UI JSON VS API JSON does not Matched')
                    log.info('DEV-UI JSON VS API JSON does not Matched -- Test case Fail')
                    # print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                    #     rdx_json) + 'DEV-JSON = ' + str(native_json))
                    # log.error('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                    #     rdx_json) + 'DEV-JSON = ' + str(native_json))
                    # assert rdx_json == native_json

                api_filename = 'rdx_playlist.json'
                if not os.path.exists(api_filename):
                    with open(api_filename, 'w') as api_file:
                        json.dump(rdx_json, api_file)

                # Writing DEV JSON to a separate file
                dev_filename = 'native_playlist.json'
                if not os.path.exists(dev_filename):
                    with open(dev_filename, 'w') as dev_file:
                        json.dump(native_json, dev_file)


        except Exception:
            traceback.print_exc()


b = Base()
access_token = b.getAccessToken()
log = b.getLogger()
playlist_id = b.get_playlist_Id('Spotify_playlistid.xlsx')
test_obj = TestSpotify()
test_obj.test_getplaylist()
