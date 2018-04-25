

POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03

DELTA_T = 1/20       # years

# transition matrix of Rate without anticoagulation
TRANS_MATRIX_WITHOUT = [
    [0,     0.0136, 0,      0.0015, 0.0178],   # Well
    [0,     0,      52.14,  0,      0],   # Stroke
    [0,     0.0298, 0,      0.0075, 0.0178],   # Post-Stroke
    [0,     0,      0,      0,      0],   # Stroke Death
    [0,     0,      0,      0,      0],   # Non-Stroke Death
    ]

# transition matrix of Rate with anticoagulation
TRANS_MATRIX_WITH = [
    [0,     0.0136, 0,      0.0015, 0.0187],   # Well
    [0,     0,      52.14,  0,      0],   # Stroke
    [0,     0.0224, 0,      0.0075, 0.0187],   # Post-Stroke
    [0,     0,      0,      0,      0],   # Stroke Death
    [0,     0,      0,      0,      0],   # Non-Stroke Death
    ]


# annual health utility of each health state
HEALTH_UTILITY = [
    1,  # well
    0.2,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9,  # post-stroke
    0,# stroke-death
    0 # non-stroke death

]

# annual cost of each health state without anticoagulation
HEALTH_COST_WITHOUT = [
    0,
    5000,  # stroke
    200,  # post-stroke /year
    0,  # stroke-death
    0 #non stroke-death
]
# annual cost of each health state without anticoagulation
HEALTH_COST_WITH = [
    0,
    5000,  # stroke
    750,  # post-stroke /year
    0,
    0
]
Anticoag_COST=0

