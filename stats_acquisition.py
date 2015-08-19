import requests
token_url = 'http://www.afl.com.au/api/cfs/afl/WMCTok'
stats_url = 'http://www.afl.com.au/stats/'
stats_api_url_base = 'http://www.afl.com.au/api/cfs/afl/statsCentre/'
session = requests.Session()
session.get(stats_url)
token = session.post(token_url).json()['token']


def get_team_stats(year='2001', round='01', match='01'):
    stats_api_url = (
        stats_api_url_base +
        'teams?competitionId=CD_S' + year +
        '014&roundId=CD_R' + year +
        '014' + round + '&matchId=CD_M' +
        year + '014' + round + match)
    data = session.get(stats_api_url, headers={'X-media-mis-token': token})
    return data.json()


if __name__ == '__main__':
    data = get_team_stats()
    print(data)
