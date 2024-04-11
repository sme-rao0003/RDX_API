import traceback
import sys
import requests
import os

sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation')
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation\utilities')
from utilities.resources import *
from utilities.configrations import *

from utilities.BaseClass_new import *

class TestSpotify(Base):
    def test_getRelatedArtist(self):
        access_token = self.getAccessToken()
        log = self.getLogger()
        artist_ids = self.get_Id('Spotify_artistid.xlsx')

        for artist_id in artist_ids:
            print(f'artist_id={artist_id}')
            try:
                rdx_json = self.get_rdx_related_artist(artist_id)
                native_json = self.get_native_related_artist(artist_id, access_token)
                self.compare_json(rdx_json, native_json, log)
            except Exception as e:
                traceback.print_exc()
                print(e)

            api_filename = 'api_response.json'
            if not os.path.exists(api_filename):
                with open(api_filename, 'w') as api_file:
                    json.dump(rdx_json, api_file)

            # Writing DEV JSON to a separate file
            dev_filename = 'dev_response.json'
            if not os.path.exists(dev_filename):
                with open(dev_filename, 'w') as dev_file:
                    json.dump(native_json, dev_file)

    def get_rdx_related_artist(self, artist_id):
        url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_related_Artist.format(id=artist_id)
        print(f'rdx_url={url}')
        headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
        response = self.getResponse(url, headers, 'API')
        return response

    def get_native_related_artist(self, artist_id, access_token):
        dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_related_Artist.format(id=artist_id)
        print(f'dev_url={dev_url}')
        headers = {'Authorization': 'Bearer ' + access_token}
        response = self.getResponse(dev_url, headers, 'DEV')
        return response

    def compare_json(self, rdx_json, native_json, log):
        if rdx_json == native_json:
            # log.info('DEV-UI JSON VS API JSON Matched -- Test case Pass')
            print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
            log.info('DEV-UI JSON VS API JSON Matched -- Test case Pass')
        else:
            print('DEV-UI JSON VS API JSON does not Matched')
            log.info('DEV-UI JSON VS API JSON does not Matched -- Test case Fail')
            # log.error(f"DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = {rdx_json} DEV-JSON = {native_json}")

if __name__ == "__main__":
    test_obj = TestSpotify()
    test_obj.test_getRelatedArtist()
