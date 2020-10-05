import os
import scipy.stats as st
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_probability as tfp
import seaborn as sns
sns.set()
COOKED_TRACE_FOLDER = './mahimahi_traces/NG_fixed_20/'

def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


def load_trace(cooked_trace_folder=COOKED_TRACE_FOLDER):
    cooked_files = os.listdir(cooked_trace_folder)
    all_data = []
    for cooked_file in cooked_files:
        #print(cooked_file)
        file_path = cooked_trace_folder + cooked_file

        with open(file_path, 'rb') as f:
            for line in f:
                parse = line.split()
                all_data.append(float(parse[0]))

    return np.array(all_data)


def get_best_distribution(data):
    dist_names = ["gamma", "beta", "rayleigh", "norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"]
    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(st, dist_name)
        param = dist.fit(data)

        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for "+dist_name+" = "+str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

    print("Best fitting distribution: "+str(best_dist))
    print("Best p value: "+ str(best_p))
    print("Parameters for the best fit: "+ str(params[best_dist]))

    return best_dist, best_p, params[best_dist]


def main():
    data = load_trace(cooked_trace_folder=COOKED_TRACE_FOLDER)
    get_best_distribution(data)

    # rv1 = st.gamma.pdf(457, 6659)
    # rv2 = st.gamma.pdf(3315, 2456)
    # kld = st.entropy(rv1, rv2)
    # print(kld)

    # x = np.linspace(-100000, 20000000, 100000000)
    # LTE: gamma, Parameters for the best fit: (1.006031842637728, -0.024452183805613266, 415840.02118790004)
    # 3G: gamma, Parameters for the best fit: (1123.1594741497684, -8732433.687507316, 8236.689775775005)
    # Pensieve: gamma, Parameters for the best fit: (34699.80269295926, -17049718.304862432, 495.9379781808127)
    # NG_low: gamma, Parameters for the best fit: (268966.9337305024, -447356334.7991879, 1668.8199288599267)
    # NG_high: gamma, Parameters for the best fit: (30309.77824643263, -149405581.62948757, 4978.59415741171)
    # NG_middle: gamma, Parameters for the best fit: (683063.6000044076, -713098470.137234, 1046.164664936136)
    # NG_middle: beta, (1.012356958067902, 1.0035547501693838, -6.098050997040092, 2999579.9628792526)
    # NG_low: beta, (1.04217286591102, 1.0284725392799454, -15539.235027695817, 3015040.3601162564)
    # NG_fixed: gamma,  (6.4497123321677226, -885912.873406837, 346361.3846503063)


    # y1 = st.gamma.pdf(x, a=1.006, scale=418540)
    # y2 = st.gamma.pdf(x, a=1123.2, scale=8237)
    # y3 = st.gamma.pdf(x, a=34670, scale=496)
    # plt.plot(x, y1, "-", color='red', label=('new_LTE_test'))
    # plt.plot(x, y2, "-", color='blue', label=('new_3G_test'))
    # plt.plot(x, y3, "-", color='green', label=('Pensieve_training'))
    # plt.title("Network traces distribution")
    #
    # # plt.ylim([0, 0.08] )
    # # plt.xlim( [0, 150] )
    # plt.legend(loc='upper center')
    # plt.show()

if __name__ == '__main__':
    main()
