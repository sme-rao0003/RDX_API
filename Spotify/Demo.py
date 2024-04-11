from pathlib import Path

import pandas as pd


def get_Artist_Id(*args):
    # df = pd.read_excel('C:\\Users\\raj0002\\PycharmProjects\\RDX-API-UAT\\Input_files\\Spotify_artistid.xlsx')
    path = Path(__file__).parent / "../Input_files/Spotify_artistid.xlsx"
    print(path)
    filee='Spotify_artistid.xlsx'
    base_path = str(Path(__file__).parent )
    file_path = (str(Path(__file__).parent) + "\\" "..\\Input_files\\"+filee)
    #

    #path = Path(__file__).parent / "../Input_files/Spotify_artistid.xlsx" # working
    df = pd.read_excel(file_path)
    artist_ids = df['artist_id'].values.tolist()
    print(artist_ids[0])
    return artist_ids

get_Artist_Id(1,2,3)