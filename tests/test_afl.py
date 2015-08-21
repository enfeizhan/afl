import numpy as np
import pandas as pd
from .context import get_team_stats
np.random.seed(2)


class TestAFL:
    def test_get_team_stats(self):
        stored_team_stats = pd.read_csv('data/team_stats.csv')
        read_team_stats = get_team_stats(matchs=[1, 2, 3])
        read_team_stats = read_team_stats.fillna(0)
        read_team_stats = read_team_stats.reset_index(drop=True)
        is_equal = stored_team_stats.equals(read_team_stats)
        assert is_equal
