"""
Match ratings: Adjusted Goal Score and Adjusted Goal Allowed
"""
# IMPORTANT: 1.37 is for soccer. It should be different for afl!


def get_ccc(htcc, vtcc):
    '''
    Get the CCC (combined competitiveness coefficient).

    Parameters
    ----------
    htcc : float
        Home team competitiveness coefficient.
    vtcc : float
        Visiting team competitiveness coefficient.

    Return
    --------
    ccc : float
        Combined competitiveness coefficient.
    '''
    cc_constant = 1.27
    ccc = htcc * vtcc * cc_constant
    return ccc


def get_adj_goals_scored(
        goals_scored,
        opp_defensive,
        avg_base=1.37,
        ):
    """
    Get the adjusted goals scored.

    Parameters
    -----------
    goals_scored : int
        The raw goals scored by a team in a match.

    opp_defensive : float
        The opponent's defensive strength rating.

    avg_base : float, default: 1.37
        A constant indicating the average number of goals scored
        per game in international competition
        (about 1.37 goals per team per game).
    """
    adj_goals_scored = (
        (goals_scored - opp_defensive)
        / max(0.25, opp_defensive*0.424+0.548)
        * (avg_base * 0.424 + 0.548)
        + avg_base)
    return adj_goals_scored


def get_adj_goals_allowed(
        goals_allowed,
        opp_offensive,
        avg_base=1.37,
        ):
    """
    Get the adjusted goal allowed

    Parameters
    -----------
    goals_allowed : int
        The raw goals allowed by a team in a match.

    opp_offensive : float
        The opponent's offensive strength rating.

    avg_base : float, default: 1.37
        A constant indicating the average number of goals scored
        per game in international competition
        (about 1.37 goals per team per game).
    """
    adj_goals_allowed = (
        (goals_allowed - opp_offensive)
        / max(0.25, opp_offensive*0.424+0.548)
        * (avg_base * 0.424 + 0.548)
        + avg_base)
    return adj_goals_allowed
