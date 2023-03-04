#@title Plotting: Seaborn style and matplotlib params
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.ticker import MaxNLocator
import matplotlib.patches as mpatches
import seaborn as sns
from rliable import library as rly
from rliable import metrics
from rliable import plot_utils
import collections
import numpy as np
import matplotlib.patches as patches
import sys
import pickle
import pandas as pd
import copy
import functools
import json
import os

import itertools as it
import random
import inspect
import scipy.stats
 
import getpass
import os.path as osp
List = [[0.0, 0.0033333333333333335, 0.006666666666666667, 0.006666666666666667, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.013333333333333334, 0.013333333333333334, 0.013333333333333334, 0.013333333333333334, 0.013333333333333334, 0.013333333333333334, 0.013333333333333334, 0.016666666666666666, 0.016666666666666666, 0.02, 0.02, 0.02, 0.02, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.023333333333333334, 0.02666666666666667, 0.02666666666666667, 0.02666666666666667, 0.02666666666666667, 0.02666666666666667, 0.02666666666666667, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03333333333333333, 0.03666666666666667, 0.03666666666666667, 0.04, 0.043333333333333335, 0.043333333333333335, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.04666666666666667, 0.05, 0.05, 0.05333333333333334, 0.05333333333333334, 0.05333333333333334, 0.05333333333333334, 0.05333333333333334], [0.25, 0.55, 0.55, 0.16666666666666666, 0.55, 0.14285714285714285, -0.05, -0.05, 0.2, 0.5, 0.5, 0.3333333333333333, -0.05, 0.55, -0.05, 0.5, -0.05, -0.05, 0.16666666666666666, 0.5, 0.55, 0.3333333333333333, 0.55, 0.2, 0.2, -0.05, 0.55, 0.14285714285714285, 0.3333333333333333, 0.16666666666666666, -0.05, 0.5, 0.16666666666666666, -0.05, -0.05, 0.55, -0.05, 0.16666666666666666, 0.5, 0.125, 0.16666666666666666, 0.55, 0.16666666666666666, 0.14285714285714285, -0.05, 0.25, 0.5, 0.2, 0.55, 0.55, 0.1, 0.55, 0.55, 0.14285714285714285, 0.55, -0.05, 0.1111111111111111, 0.125, -0.05, -0.05, 0.16666666666666666, 0.16666666666666666, 0.5, 0.14285714285714285, 0.1111111111111111, 0.16666666666666666, 0.55, 0.16666666666666666, 0.55, 0.3333333333333333, 0.5, 0.16666666666666666, -0.05], [-0.05, 1, 1, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, 1, -0.05, 1, -0.05, -0.05, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, 1, 1, -0.05, 1, 1, -0.05, 1, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, -0.05, 1, -0.05, 1, -0.05, -0.05, -0.05, -0.05]]
# atari_200m_normalized_score_dict={}
# atari_200m_normalized_score_dict["SuccessRate"] = List[0]
# atari_200m_normalized_score_dict["TotalReward"] = List[1]
# atari_200m_normalized_score_dict["GlobalReward"] = List[2]
# # Human normalized score thresholds
# atari_200m_thresholds = np.linspace(0.0, 8.0, 81)
# score_distributions, score_distributions_cis = rly.create_performance_profile(
#     atari_200m_normalized_score_dict, atari_200m_thresholds)
# # Plot score distributions
# fig, ax = plt.subplots(ncols=1, figsize=(7, 5))
# plot_utils.plot_performance_profiles(
#   score_distributions, atari_200m_thresholds,
#   performance_profile_cis=score_distributions_cis,
#   colors=dict(zip(algorithms, sns.color_palette('colorblind'))),
#   xlabel=r'Human Normalized Score $(\tau)$',
#   ax=ax)

# print(List[0])
fig = plt.figure()
plt.title("Rewards for different episodes", fontsize='16')	#title
plt.plot(range(0,73), List[1])	#plot the points
plt.xlabel("epoches",fontsize='13')	#adds a label in the x axis
plt.ylabel("Rewards",fontsize='13')	#adds a label in the y axis
plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot

plt.show()