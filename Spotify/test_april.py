import json
import os
import traceback
import sys
import time
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation')
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation\utilities')


from utilities.resources import *
from utilities.configrations import *
# from utilities.BaseClass_old import *
from utilities.BaseClass_new import *


class TestSpotify(Base):
    # print('Inside Spotify class')

    def test_getArtistTopTrack(self):
        rdx_json = {}
        native_json = {}
        print(f' rdx_json = {rdx_json}, native_json={native_json}')
        for x in artist_id:
            print(f'x={x}')
            try:
                url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_Artist_top_track.format(id=x)
                print(f'rdx_url = {url}')
                headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
                response = self.getResponse(url, headers, 'API')
                rdx_json = response
            except Exception as e:
                traceback.print_exc()
                print(e)

            try:
                dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_Artist_top_track.format(
                    id=x)
                print(f' native_url = {dev_url}')
                head = {'Authorization': 'Bearer ' + access_token}
                response = self.getResponse(dev_url, head, 'DEV')
                native_json = response
            except Exception as e:
                traceback.print_exc()
                print(e)

            if rdx_json == native_json:
                print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
                log.info('DEV-UI JSON VS API JSON Matched -- Test case Pass')
            else:
                print('DEV-UI JSON VS API JSON does not Matched')
                log.error('DEV-UI JSON VS API JSON does not Matched -- Test case Fail')
                # print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                #     rdx_json) + 'DEV-JSON = ' + str(native_json))
                # log.error('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                #     rdx_json) + 'DEV-JSON = ' + str(native_json))
                # assert True == False
                # time.sleep(5)
                # self.test_getArtistTopTrack()

            api_filename = 'api_response.json'
            if not os.path.exists(api_filename):
                with open(api_filename, 'w') as api_file:
                    json.dump(rdx_json, api_file)

            # Writing DEV JSON to a separate file
            dev_filename = 'dev_response.json'
            if not os.path.exists(dev_filename):
                with open(dev_filename, 'w') as dev_file:
                    json.dump(native_json, dev_file)



b = Base()
access_token = b.getAccessToken()
log = b.getLogger()
artist_id = b.get_Id('Spotify_artistid.xlsx')
test_obj = TestSpotify()
test_obj.test_getArtistTopTrack()