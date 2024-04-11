class APIResources:
    rdx_artist = '/spotify/v1/artists/'
    native_artist = '/v1/artists/'

    rdx_sevralArtist = '/spotify/v1/artists?ids='
    native_sevralArtist = '/v1/artists?ids='

    rdx_artist_Album = '/spotify/v1/artists/{id}/albums?'
    native_artist_Album = '/v1/artists/{id}/albums?'

    rdx_artist1 = '/spotify/v1/artists/1mjBnx0cvSsEmR4WXfVQyi'
    native_artist1 = '/v1/artists/1Bl6wpkWCQ4KVgnASpvzzA'
    rdx_sevralArtist1 = '/spotify/v1/artists?ids=21YkfPZ2ctHAoZf4ANU5re,1mjBnx0cvSsEmR4WXfVQyi,4AEv9RpfPAr67W04LqWLDb,4KvEeVTVVyMlEhr5ovZBOT,3ZwOn6LXemqwJ0Lfd8KQLF,4dpARuHxo51G3z768sgnrY,2qS6cYzM5ajhprcxQa1Ilc,3NIFl4tsySuu3eu8Yt8c0s,6HZ5IH5ksF7cs4mg0HQlSN,1z2GIqUV62qrl1J5sXalOT'
    native_sevralArtist1 = '/v1/artists?ids=21YkfPZ2ctHAoZf4ANU5re,1mjBnx0cvSsEmR4WXfVQyi,4AEv9RpfPAr67W04LqWLDb,4KvEeVTVVyMlEhr5ovZBOT,3ZwOn6LXemqwJ0Lfd8KQLF,4dpARuHxo51G3z768sgnrY,2qS6cYzM5ajhprcxQa1Ilc,3NIFl4tsySuu3eu8Yt8c0s,6HZ5IH5ksF7cs4mg0HQlSN,1z2GIqUV62qrl1J5sXalOT'

    rdx_Artist_top_track = '/spotify/v1/artists/{id}/top-tracks'
    native_Artist_top_track = '/v1/artists/{id}/top-tracks'

    rdx_playlist = '/spotify/v1/playlists/{id}'
    native_playlist = '/v1/playlists/{id}'

    rdx_related_Artist = '/spotify/v1/artists/{id}/related-artists'
    native_related_Artist = '/v1/artists/{id}/related-artists'