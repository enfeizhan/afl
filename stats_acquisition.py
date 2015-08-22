import pandas as pd
import requests
import sys
from datetime import datetime
token_url = 'http://www.afl.com.au/api/cfs/afl/WMCTok'
stats_url = 'http://www.afl.com.au/stats/'
stats_api_url_base = 'http://www.afl.com.au/api/cfs/afl/statsCentre/'


def get_team_stats(years=[2001], rds=[1], matches=[1]):
    session = requests.Session()
    session.get(stats_url)
    token = session.post(token_url).json()['token']
    df = pd.DataFrame()
    for year in years:
        for rd in rds:
            for match in matches:
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
                hm_team = data['lists'][0]['team']
                aw_team = data['lists'][1]['team']
                hm_avgs = data['lists'][0]['stats']['averages']
                hm_tots = data['lists'][0]['stats']['totals']
                aw_avgs = data['lists'][1]['stats']['averages']
                aw_tots = data['lists'][1]['stats']['totals']
                row = pd.DataFrame({
                    'year': [year],
                    'round': [rd],
                    'match': [match],
                    'home': [hm_team['teamName']],
                    'hm_score': [
                        hm_tots['behinds'] + 6 * hm_tots['goals']],
                    'hm_avg_behinds': [hm_avgs['behinds']],
                    'hm_tot_behinds': [hm_tots['behinds']],
                    'hm_avg_bounces': [hm_avgs['bounces']],
                    'hm_tot_bounces': [hm_tots['bounces']],
                    'hm_avg_clangers': [hm_avgs['clangers']],
                    'hm_tot_clangers': [hm_tots['clangers']],
                    'hm_avg_centreClearances': [
                        hm_avgs['clearances']['centreClearances']],
                    'hm_tot_centreClearances': [
                        hm_tots['clearances']['centreClearances']],
                    'hm_avg_stoppageClearances': [
                        hm_avgs['clearances']['stoppageClearances']],
                    'hm_tot_stoppageClearances': [
                        hm_tots['clearances']['stoppageClearances']],
                    'hm_avg_totalClearances': [
                        hm_avgs['clearances']['totalClearances']],
                    'hm_tot_totalClearances': [
                        hm_tots['clearances']['totalClearances']],
                    'hm_avg_contestedMarks': [hm_avgs['contestedMarks']],
                    'hm_tot_contestedMarks': [hm_tots['contestedMarks']],
                    'hm_avg_contestedPossessions': [
                        hm_avgs['contestedPossessions']],
                    'hm_tot_contestedPossessions': [
                        hm_tots['contestedPossessions']],
                    'hm_avg_contestedPossessions': [
                        hm_avgs['contestedPossessions']],
                    'hm_tot_contestedPossessions': [
                        hm_tots['contestedPossessions']],
                    'hm_avg_disposalEfficiency': [
                        hm_avgs['disposalEfficiency']],
                    'hm_tot_disposalEfficiency': [
                        hm_tots['disposalEfficiency']],
                    'hm_avg_disposals': [hm_avgs['disposals']],
                    'hm_tot_disposals': [hm_tots['disposals']],
                    'hm_avg_dreamTeamPoints': [hm_avgs['dreamTeamPoints']],
                    'hm_tot_dreamTeamPoints': [hm_tots['dreamTeamPoints']],
                    'hm_avg_freesAgainst': [hm_avgs['freesAgainst']],
                    'hm_tot_freesAgainst': [hm_tots['freesAgainst']],
                    'hm_avg_freesFor': [hm_avgs['freesFor']],
                    'hm_tot_freesFor': [hm_tots['freesFor']],
                    'hm_avg_goalAccuracy': [hm_avgs['goalAccuracy']],
                    'hm_tot_goalAccuracy': [hm_tots['goalAccuracy']],
                    'hm_avg_goalAssists': [hm_avgs['goalAssists']],
                    'hm_tot_goalAssists': [hm_tots['goalAssists']],
                    'hm_avg_goals': [hm_avgs['goals']],
                    'hm_tot_goals': [hm_tots['goals']],
                    'hm_avg_handballs': [hm_avgs['handballs']],
                    'hm_tot_handballs': [hm_tots['handballs']],
                    'hm_avg_hitouts': [hm_avgs['hitouts']],
                    'hm_tot_hitouts': [hm_tots['hitouts']],
                    'hm_avg_inside50s': [hm_avgs['inside50s']],
                    'hm_tot_inside50s': [hm_tots['inside50s']],
                    'hm_avg_interchangeCounts': [
                        hm_avgs['interchangeCounts']],
                    'hm_tot_interchangeCounts': [
                        hm_tots['interchangeCounts']],
                    'hm_avg_kicks': [hm_avgs['kicks']],
                    'hm_tot_kicks': [hm_tots['kicks']],
                    'hm_avg_marks': [hm_avgs['marks']],
                    'hm_tot_marks': [hm_tots['marks']],
                    'hm_avg_marksInside50': [hm_avgs['marksInside50']],
                    'hm_tot_marksInside50': [hm_tots['marksInside50']],
                    'hm_avg_onePercenters': [hm_avgs['onePercenters']],
                    'hm_tot_onePercenters': [hm_tots['onePercenters']],
                    'hm_avg_ranking': [hm_avgs['ranking']],
                    'hm_tot_ranking': [hm_tots['ranking']],
                    'hm_avg_ratingPoints': [hm_avgs['ratingPoints']],
                    'hm_tot_ratingPoints': [hm_tots['ratingPoints']],
                    'hm_avg_rebound50s': [hm_avgs['rebound50s']],
                    'hm_tot_rebound50s': [hm_tots['rebound50s']],
                    'hm_avg_superGoals': [hm_avgs['superGoals']],
                    'hm_tot_superGoals': [hm_tots['superGoals']],
                    'hm_avg_tackles': [hm_avgs['tackles']],
                    'hm_tot_tackles': [hm_tots['tackles']],
                    'hm_avg_totalPossessions': [hm_avgs['totalPossessions']],
                    'hm_tot_totalPossessions': [hm_tots['totalPossessions']],
                    'hm_avg_uncontestedPossessions': [
                        hm_avgs['uncontestedPossessions']],
                    'hm_tot_uncontestedPossessions': [
                        hm_tots['uncontestedPossessions']],
                    'away': [aw_team['teamName']],
                    'aw_score': [
                        aw_tots['behinds'] + 6 * aw_tots['goals']],
                    'aw_avg_behinds': [aw_avgs['behinds']],
                    'aw_tot_behinds': [aw_tots['behinds']],
                    'aw_avg_bounces': [aw_avgs['bounces']],
                    'aw_tot_bounces': [aw_tots['bounces']],
                    'aw_avg_clangers': [aw_avgs['clangers']],
                    'aw_tot_clangers': [aw_tots['clangers']],
                    'aw_avg_centreClearances': [
                        aw_avgs['clearances']['centreClearances']],
                    'aw_tot_centreClearances': [
                        aw_tots['clearances']['centreClearances']],
                    'aw_avg_stoppageClearances': [
                        aw_avgs['clearances']['stoppageClearances']],
                    'aw_tot_stoppageClearances': [
                        aw_tots['clearances']['stoppageClearances']],
                    'aw_avg_totalClearances': [
                        aw_avgs['clearances']['totalClearances']],
                    'aw_tot_totalClearances': [
                        aw_tots['clearances']['totalClearances']],
                    'aw_avg_contestedMarks': [aw_avgs['contestedMarks']],
                    'aw_tot_contestedMarks': [aw_tots['contestedMarks']],
                    'aw_avg_contestedPossessions': [
                        aw_avgs['contestedPossessions']],
                    'aw_tot_contestedPossessions': [
                        aw_tots['contestedPossessions']],
                    'aw_avg_contestedPossessions': [
                        aw_avgs['contestedPossessions']],
                    'aw_tot_contestedPossessions': [
                        aw_tots['contestedPossessions']],
                    'aw_avg_disposalEfficiency': [
                        aw_avgs['disposalEfficiency']],
                    'aw_tot_disposalEfficiency': [
                        aw_tots['disposalEfficiency']],
                    'aw_avg_disposals': [aw_avgs['disposals']],
                    'aw_tot_disposals': [aw_tots['disposals']],
                    'aw_avg_dreamTeamPoints': [aw_avgs['dreamTeamPoints']],
                    'aw_tot_dreamTeamPoints': [aw_tots['dreamTeamPoints']],
                    'aw_avg_freesAgainst': [aw_avgs['freesAgainst']],
                    'aw_tot_freesAgainst': [aw_tots['freesAgainst']],
                    'aw_avg_freesFor': [aw_avgs['freesFor']],
                    'aw_tot_freesFor': [aw_tots['freesFor']],
                    'aw_avg_goalAccuracy': [aw_avgs['goalAccuracy']],
                    'aw_tot_goalAccuracy': [aw_tots['goalAccuracy']],
                    'aw_avg_goalAssists': [aw_avgs['goalAssists']],
                    'aw_tot_goalAssists': [aw_tots['goalAssists']],
                    'aw_avg_goals': [aw_avgs['goals']],
                    'aw_tot_goals': [aw_tots['goals']],
                    'aw_avg_handballs': [aw_avgs['handballs']],
                    'aw_tot_handballs': [aw_tots['handballs']],
                    'aw_avg_hitouts': [aw_avgs['hitouts']],
                    'aw_tot_hitouts': [aw_tots['hitouts']],
                    'aw_avg_inside50s': [aw_avgs['inside50s']],
                    'aw_tot_inside50s': [aw_tots['inside50s']],
                    'aw_avg_interchangeCounts': [
                        aw_avgs['interchangeCounts']],
                    'aw_tot_interchangeCounts': [
                        aw_tots['interchangeCounts']],
                    'aw_avg_kicks': [aw_avgs['kicks']],
                    'aw_tot_kicks': [aw_tots['kicks']],
                    'aw_avg_marks': [aw_avgs['marks']],
                    'aw_tot_marks': [aw_tots['marks']],
                    'aw_avg_marksInside50': [aw_avgs['marksInside50']],
                    'aw_tot_marksInside50': [aw_tots['marksInside50']],
                    'aw_avg_onePercenters': [aw_avgs['onePercenters']],
                    'aw_tot_onePercenters': [aw_tots['onePercenters']],
                    'aw_avg_ranking': [aw_avgs['ranking']],
                    'aw_tot_ranking': [aw_tots['ranking']],
                    'aw_avg_ratingPoints': [aw_avgs['ratingPoints']],
                    'aw_tot_ratingPoints': [aw_tots['ratingPoints']],
                    'aw_avg_rebound50s': [aw_avgs['rebound50s']],
                    'aw_tot_rebound50s': [aw_tots['rebound50s']],
                    'aw_avg_superGoals': [aw_avgs['superGoals']],
                    'aw_tot_superGoals': [aw_tots['superGoals']],
                    'aw_avg_tackles': [aw_avgs['tackles']],
                    'aw_tot_tackles': [aw_tots['tackles']],
                    'aw_avg_totalPossessions': [aw_avgs['totalPossessions']],
                    'aw_tot_totalPossessions': [aw_tots['totalPossessions']],
                    'aw_avg_uncontestedPossessions': [
                        aw_avgs['uncontestedPossessions']],
                    'aw_tot_uncontestedPossessions': [
                        aw_tots['uncontestedPossessions']],
                    })
                df = df.append(row)
    return df


def find_match(stats_df, year, rd, team, home=True):
    if home:
        is_the_match = (
            (stats_df.year == year) &
            (stats_df.round == rd) &
            (stats_df.home == team))
        stats = stats_df.loc[is_the_match]
        assert stats.shape[0] != 0, 'No match found!'
        assert stats.shape[0] <= 1, 'Find multiple matches!'
    else:
        is_the_match = (
            (stats_df.year == year) &
            (stats_df.round == rd) &
            (stats_df.away == team))
        stats = stats_df.loc[is_the_match]
        assert stats.shape[0] != 0, 'No match found!'
        assert stats.shape[0] <= 1, 'Find multiple matches!'
    return stats


def find_last_match(stats_df, start_year, start_round, team, home=True):
    original_start_round = start_round
    for year in range(start_year, 2000, -1):
        if year != start_year:
            start_round = stats_df.loc[
                stats_df.year == year,
                'round'].max()
        for rd in range(start_round, 0, -1):
            try:
                stats = find_match(
                    stats_df=stats_df,
                    year=year,
                    rd=rd,
                    team=team,
                    home=home)
                return stats
            except AssertionError:
                pass
    else:
        raise ValueError(
            'Couldn\'t find the last' +
            ' {home} '.format(home=('home' if home else 'away')) +
            'match back from Round' +
            ' {rd} '.format(rd=original_start_round) +
            'of Year {year}!'.format(year=start_year))


def find_head2head(stats_df, year, rd, hm_team, aw_team):
    is_the_head2head = (
        (stats_df.year == year) &
        (stats_df.round == rd) &
        (stats_df.home == hm_team) &
        (stats_df.away == aw_team))
    stats = stats_df.loc[is_the_head2head]
    assert stats.shape[0] != 0, 'No head-to-head found!'
    assert stats.shape[0] <= 1, 'Find multiple head-to-head\'s!'
    return stats


def find_last_head2head(stats_df, start_year, start_round, hm_team, aw_team):
    original_start_round = start_round
    for year in range(start_year, 2000, -1):
        if year != start_year:
            start_round = stats_df.loc[
                stats_df.year == year,
                'round'].max()
        for rd in range(start_round, 0, -1):
            try:
                stats = find_head2head(
                    stats_df=stats_df,
                    year=year,
                    rd=rd,
                    hm_team=hm_team,
                    aw_team=aw_team)
                return stats
            except AssertionError:
                pass
    else:
        raise ValueError(
            'Couldn\'t find the last head-to-head between home' +
            ' {hm_team} '.format(hm_team=hm_team) +
            'and away' +
            ' {aw_team} '.format(aw_team=aw_team) +
            'back from Round' +
            ' {rd} '.format(rd=original_start_round) +
            'of Year {year}!'.format(year=start_year))


def add_team_stats(stats_file_path, year, rd, match):
    stats_df = pd.read_csv(stats_file_path)
    stats = get_team_stats(years=[year], rds=[rd], matches=[match])
    stats_df = stats_df.append(stats)
    stats_df = stats_df.sort(['year', 'round', 'match'])
    stats_df.to_csv(stats_file_path, index=False)


if __name__ == '__main__':
    data = get_team_stats()
    print(data)
