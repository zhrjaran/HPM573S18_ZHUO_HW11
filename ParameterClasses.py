from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
#import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEATH = 3
    NON_STROKE_DEATH=4


class Therapies(Enum):
    """ mono vs. combination therapy """
    NONE = 0
    ANTICOAG = 1

class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # annual treatment cost
        if self._therapy == Therapies.NONE:
            self._annualTreatmentCost = 0
        if self._therapy == Therapies.ANTICOAG:
            self._annualTreatmentCost = Data.Anticoag_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        # calculate transition rates and annual cost depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix = list_without[0]
            self._annualStateCosts = Data.HEALTH_COST_WITHOUT
        else:
            self._prob_matrix = list_with[0]
            self._annualStateCosts = Data.HEALTH_COST_WITH

        self._annualStateUtilities = Data.HEALTH_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state in [HealthStats.STROKE_DEATH,HealthStats.NON_STROKE_DEATH]:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state in [HealthStats.STROKE_DEATH,HealthStats.NON_STROKE_DEATH]:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost


def calculate_prob_matrix_without():
    prob_matrix=[]
    # convert back to transition probability matrix, but more frequently, not use "1 year"
    prob_matrix[:],p=MarkovCls.continuous_to_discrete(Data.TRANS_MATRIX_WITHOUT, Data.DELTA_T)

    return [prob_matrix,p]
list_without= calculate_prob_matrix_without()

def calculate_prob_matrix_with():
    prob_matrix = []
    # convert back to transition probability matrix, but more frequently, not use "1 year"
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(Data.TRANS_MATRIX_WITH, Data.DELTA_T)

    return [prob_matrix,p]

list_with=calculate_prob_matrix_with()

print('Upper bound on the probability of two transitions within delta_t without treatment:', list_without[1])
print('Upper bound on the probability of two transitions within delta_t with treatment:', list_with[1])

