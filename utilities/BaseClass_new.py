import base64
import inspect
import logging
import requests
import json
import pandas as pd
from pathlib import Path
from resources import *
from configrations import *
from requests import post
import os
path = os.getcwd()
# print(f"path = {path}")


class Base():


    def getAccessToken(self):
        auth_string = '5adc57e52a7c4a70b3878d023dac8e6f' + ':' + 'c284f122884741b8911a10132a7742e0'
        auth_bytes = auth_string.encode("utf-8")
        auth_base64=str(base64.b64encode(auth_bytes), "utf-8")
        url = 'https://accounts.spotify.com/api/token'
        header = {
            'Authorization': 'Basic ' + auth_base64,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={'grant_type': 'client_credentials'}
        result= post(url, headers=header, data=data)
        if result.status_code == 200:
            # print(result.status_code)
            json_result = json.loads(result.content)
            # print(json_result)
            token = json_result["access_token"]
            # print(token)
            return token
        else:
            print('Failed to authenticate '+ result.status_code)
            return result.status_code



    def getResponse(self, url, header, responce_name):
    #def getResponse(self, *args):
        response_json = {}
        try:
            response = requests.get(url, headers=header)

            if response.status_code == 200:

                res = response.json()
                # print(res)
                if responce_name == 'API':
                    response_json = res['data']
                    return response_json
                elif responce_name == 'DEV':
                    # print(res)
                    return res
            else:
                res = response.json()
                response_json = res['data']
                print('Response code is :'+str(response.status_code) + ' -- Test case failed')
                return response_json
        except Exception as e:
            print(e)

    def get_Id(self, file_name):
        #df = pd.read_excel('C:\\Users\\raj0002\\PycharmProjects\\RDX-API-UAT\\Input_files\\Spotify_artistid.xlsx')
        file_path = (str(Path(__file__).parent) + "\\" "..\\Input_files\\" + file_name)
        # print(f'file_name={file_path}')
        df = pd.read_excel(file_path)
        artist_ids = df['artist_id'].values.tolist()
        # print(artist_ids[0])
        return artist_ids


    def get_playlist_Id(self, file_name):
        #df = pd.read_excel('C:\\Users\\raj0002\\PycharmProjects\\RDX-API-UAT\\Input_files\\Spotify_artistid.xlsx')
        file_path = (str(Path(__file__).parent) + "\\" "..\\Input_files\\" + file_name)
        print(f'file_name={file_path}')
        df = pd.read_excel(file_path)
        playlist_id = df['playlistid'].values.tolist()
        print(playlist_id[0])
        return playlist_id

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # print(inspect.stack())
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger



b = Base()
b.getAccessToken()
b.get_Id('Spotify_artistid.xlsx')