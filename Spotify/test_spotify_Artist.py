import json
import requests
import sys
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation')
sys.path.append(r'C:\Users\RAO0003\Documents\RDX_API_AUTOMATION\RDX_API_Automation\utilities')
from utilities.BaseClass_old import Base
from utilities.resources import *
from utilities.configrations import *




class TestSpotify(Base):
    ids=[]
    print(f'id={ids}')
    #def __init__(self):
        #self.ids = self.get_Artist_Id()

    def test_getArtist(self):
        rdx_json = {}
        native_json = {}
        try:
            #print(self.ids[0])
            #print("HI")
            url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_artist + ids[0]
           # print(url)
            headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
            response = self.getResponse(url, headers, 'API')
            rdx_json = response
            print(rdx_json)
            # print(api_json)
        except Exception as e:
            print(e)

        try:
            dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_artist + ids[0]
            head = {'Authorization': 'Bearer ' + accessTaken}
            response = self.getResponse(dev_url, head, 'DEV')
            native_json = response
            print(native_json)
            #print(native_json)
        except Exception as e:
            print(e)

        if rdx_json == native_json:
            print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
            log.info('DEV-UI JSON VS API JSON Matched -- Test case Pass')
        else:
            print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                rdx_json) + 'DEV-JSON = ' + str(native_json))
            log.error('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
                rdx_json) + 'DEV-JSON = ' + str(native_json))
            assert True == False


    # def test_SeveralArtis(self):
    #     rdx_json = {}
    #     native_json = {}
    #     try:
    #         url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_sevralArtist + ', '.join(ids)
    #         #print(url)
    #         headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
    #         response = self.getResponse(url, headers, 'API')
    #         rdx_json = response
    #         print(rdx_json)
    #     except Exception as e:
    #         print(e)
    #
    #     try:
    #         dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_sevralArtist +', '.join(ids)
    #         head = {'Authorization': 'Bearer ' + accessTaken}
    #         response = self.getResponse(dev_url, head, 'DEV')
    #         native_json = response
    #         print(native_json)
    #     except Exception as e:
    #         print(e)
    #
    #     if rdx_json == native_json:
    #         print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
    #     else:
    #         print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
    #             rdx_json) + 'DEV-JSON = ' + str(native_json))
    #         assert True == False



    # def test_SeveralArtis_More_Then_Fifty(self):
    #     rdx_json = {}
    #     native_json = {}
    #     count=len(self.get_Artist_Id())
    #     print(count)
    #     if count > 50:
    #         id = ids[1:51]
    #         try:
    #             url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_sevralArtist + ', '.join(id)
    #             print(url)
    #             headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
    #             response = self.getResponse(url, headers, 'API')
    #             rdx_json = response
    #             print(rdx_json)
    #         except Exception as e:
    #             print(e)
    #
    #         try:
    #             dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_sevralArtist +', '.join(id)
    #             head = {'Authorization': 'Bearer ' + accessTaken}
    #             response = self.getResponse(dev_url, head, 'DEV')
    #             native_json = response
    #             print(native_json)
    #         except Exception as e:
    #             print(e)
    #
    #         if rdx_json == native_json:
    #             print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
    #         else:
    #             print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
    #                 rdx_json) + 'DEV-JSON = ' + str(native_json))
    #             assert True == False
    #     else:
    #         log.error('There are less then 50 artist_id so this test case wont run')
    #         assert True == False

    # def test_SeveralArtis_Less_Then_Fifty(self):
    #     rdx_json = {}
    #     native_json = {}
    #     count = len(self.get_Artist_Id())
    #     print(count)
    #     if count > 48:
    #         id = ids[1:49]
    #         try:
    #             url = getConfigration()['SPOTIFY']['api_endpoint'] + APIResources.rdx_sevralArtist + ', '.join(id)
    #             print(url)
    #             headers = {'x-api-key': 'NWolYdwUTffmMjCcCiVdJKraDZfxYl'}
    #             response = self.getResponse(url, headers, 'API')
    #             rdx_json = response
    #             # print(api_json)
    #         except Exception as e:
    #             print(e)
    #
    #         try:
    #             dev_url = getConfigration()['SPOTIFY']['dev_endpoint'] + APIResources.native_sevralArtist +', '.join(id)
    #             head = {'Authorization': 'Bearer ' + accessTaken}
    #             response = self.getResponse(dev_url, head, 'DEV')
    #             native_json = response
    #             print(native_json)
    #         except Exception as e:
    #             print(e)
    #
    #         if rdx_json == native_json:
    #             print('DEV-UI JSON VS API JSON Matched -- Test case Pass')
    #         else:
    #             print('DEV-UI JSON VS API JSON does not Matched -- Test case fail - API-JSON = ' + str(
    #                 rdx_json) + 'DEV-JSON = ' + str(native_json))
    #             assert True == False
    #
    #     else:
    #         log.error('There are less then 48 artist_id so this test case wont run')
    #         assert True== False







r = TestSpotify()
accessTaken=r.getAccessToken()
log = r.getLogger()
ids=r.get_Artist_Id()

r.test_getArtist()
#r.getSeveralArtis()
#r.getSeveralArtis_More_Then_Fifty()
