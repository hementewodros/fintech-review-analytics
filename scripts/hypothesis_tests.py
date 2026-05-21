from scipy.stats import ttest_ind

def run_ttest(group_a, group_b):
    stat, p = ttest_ind(
        group_a,
        group_b,
        nan_policy='omit'
    )

    return stat, p