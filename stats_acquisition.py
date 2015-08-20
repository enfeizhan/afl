import pandas as pd
import requests
token_url = 'http://www.afl.com.au/api/cfs/afl/WMCTok'
stats_url = 'http://www.afl.com.au/stats/'
stats_api_url_base = 'http://www.afl.com.au/api/cfs/afl/statsCentre/'
session = requests.Session()
session.get(stats_url)
token = session.post(token_url).json()['token']


def get_team_stats(years=[2001], rds=[1], matchs=[1]):
    df = pd.DataFrame()
    for year in years:
        for rd in rds:
            for match in matchs:
                stats_api_url = (
                    stats_api_url_base + 'teams?competitionId=CD_S{year:4d}' +
                    '014&roundId=CD_R{year:4d}014{rd:02d}&matchId=CD_M' +
                    '{year:4d}014{rd:02d}{match:02d}')
                stats_api_url = stats_api_url.format(
                    year=year,
                    rd=rd,
                    match=match)
                data = session.get(
                    stats_api_url,
                    headers={'X-media-mis-token': token}).json()
                home_team = data['lists'][0]['team']
                away_team = data['lists'][1]['team']
                home_avgs = data['lists'][0]['stats']['averages']
                home_tots = data['lists'][0]['stats']['totals']
                away_avgs = data['lists'][1]['stats']['averages']
                away_tots = data['lists'][1]['stats']['totals']
                row = pd.DataFrame({
                    'year': [year],
                    'round': [rd],
                    'home': [data['lists'][0]['team']['teamName']],
                    'away': [data['lists'][1]['team']['teamName']],
                    'hm_avg_behinds': [home_avgs['behinds']],
                    '_tot_behinds': [_tots['behinds']],
                    '_avg_bounces': [_avgs['bounces']],
                    '_tot_bounces': [_tots['bounces']],
                    '_avg_clangers': [_avgs['clangers']],
                    '_tot_clangers': [_tots['clangers']],
                    '_avg_centreClearances': [
                        _avgs['clearances']['centreClearances']],
                    '_tot_centreClearances': [
                        _tots['clearances']['centreClearances']],
                    '_avg_stoppageClearances': [
                        _avgs['clearances']['stoppageClearances']],
                    '_tot_stoppageClearances': [
                        _tots['clearances']['stoppageClearances']],
                    '_avg_totalClearances': [
                        _avgs['clearances']['totalClearances']],
                    '_tot_totalClearances': [
                        _tots['clearances']['totalClearances']],
                    '_avg_contestedMarks': [_avgs['contestedMarks']],
                    '_tot_contestedMarks': [_tots['contestedMarks']],
                    '_avg_contestedPossessions': [
                        _avgs['contestedPossessions']]
                    '_tot_contestedPossessions': [
                        _tots['contestedPossessions']]
                    'aw_avg_behinds': [
                        data['lists'][1]['stats']['averages']['behinds']],
                    })
                df = df.append(row)
    return df


if __name__ == '__main__':
    data = get_team_stats()
    print(data)
