from enum import Enum
import numpy as np

class ContributionFreq(Enum):
    DAILY = 1
    WEEKLY = 2
    FORTNIGHTLY = 3
    MONTHLY = 4
    YEARLY = 5



def single_run(years, mean, variance):
    return np.random.normal(loc=mean, scale=np.sqrt(variance), size=(years,))


def main():

    starting_value = 40000
    years_until_retirement = 40

    contribution_freq = ContributionFreq.FORTNIGHTLY

    single_run_result = single_run(years_until_retirement, mean=10, variance=15)
    print(single_run_result)

    return 



if (__name__ == "__main__"):
    main()
