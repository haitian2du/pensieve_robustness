from scipy.stats import norm
import pandas as pd
import numpy as np
import scipy.stats
import os

def load_trace(cooked_trace_folder):
    cooked_files = os.listdir(cooked_trace_folder)
    all_data = []
    for cooked_file in cooked_files:
        #print(cooked_file)
        file_path = cooked_trace_folder + cooked_file

        with open(file_path, 'r') as f:
            for line in f:
                parse = line.split()
                all_data.append(float(parse[1]))
                #print(all_data)

    return np.array(all_data)


def KL_divergence(p, q):
    sum = p*(np.log(p/q))
    all_value = [x for x in sum if str( x ) != 'nan' and str( x ) != 'inf']  # 除去inf值 return np.sum(all_value)
    return np.sum( all_value )



def KL_div(arr1,arr2,num_bins):
    max0 = max(np.max(arr1),np.max(arr2))
    min0 = min(np.min(arr1),np.min(arr2))
    bins = np.linspace(min0-1e-4, max0-1e-4, num=num_bins)
    PDF1 = pd.cut(arr1,bins).value_counts() / len(arr1)
    PDF2 = pd.cut(arr2,bins).value_counts() / len(arr2)
    return KL_divergence(PDF1.values,PDF2.values)


def JS_divergence(p,q):
    M=(p+q)/2
    return 0.5*scipy.stats.entropy(p, M)+0.5*scipy.stats.entropy(q, M)


def JS_div(arr1,arr2,num_bins):
    max0 = max(np.max(arr1),np.max(arr2))
    min0 = min(np.min(arr1),np.min(arr2))
    bins = np.linspace(min0-1e-4, max0-1e-4, num=num_bins)
    PDF1 = pd.cut(arr1,bins).value_counts() / len(arr1)
    PDF2 = pd.cut(arr2,bins).value_counts() / len(arr2)
    return JS_divergence(PDF1.values,PDF2.values)

#
# pensieve_train = load_trace('./mahimahi_traces/Pensieve/')
# LTE_test = load_trace('./mahimahi_traces/LTE/')
# test_3g = load_trace('./mahimahi_traces/3G/')
# NG_low_test = load_trace('./mahimahi_traces/NG_low_20/')
# NG_middle_test = load_trace('./mahimahi_traces/NG_middle_20/')
# NG_high_test = load_trace('./mahimahi_traces/NG_high_20/')
# NG_fixed_test = load_trace('./mahimahi_traces/NG_fixed_20/')
# puffer_1 = load_trace('./mahimahi_traces/puffer-1-mahimahi/')
# puffer_2 = load_trace('./mahimahi_traces/puffer-2-mahimahi/')
# puffer_3 = load_trace('./mahimahi_traces/puffer-3-mahimahi/')

pensieve_train = load_trace('./cooked_traces/Pensieve_train/')
LTE_test = load_trace('./cooked_traces/LTE/')
test_3g = load_trace('./cooked_traces/3G/')
NG_low_test = load_trace('./cooked_traces/NG_low_sim/')
NG_middle_test = load_trace('./cooked_traces/NG_middle_sim/')
NG_high_test = load_trace('./cooked_traces/NG_high_sim/')
NG_fixed_test = load_trace('./cooked_traces/NG_fixed_sim/')
puffer_1 = load_trace('./cooked_traces/puffer-traces-201908-for-pensieve/puffer-1/')
puffer_2 = load_trace('./cooked_traces/puffer-traces-201908-for-pensieve/puffer-2/')
puffer_3 = load_trace('./cooked_traces/puffer-traces-201908-for-pensieve/puffer-3/')


def main():
    print(str("NG_low: "), KL_div(pensieve_train, NG_low_test, num_bins=20))  # 0.0098
    print(str("NG_middle: "), KL_div(pensieve_train, NG_middle_test, num_bins=20))  # 0.135
    print(str("NG_high: "), KL_div(pensieve_train, NG_high_test, num_bins=20))  # 0.0098
    print(str("NG_fixed: "), KL_div(pensieve_train, NG_fixed_test, num_bins=20))  # 0.135
    print(str("LTE: "), KL_div(pensieve_train, LTE_test, num_bins=20))  # 0.135
    print(str("3G: "), KL_div(pensieve_train, test_3g, num_bins=20))  # 0.135
    print(str("puffer-1: "),  KL_div( pensieve_train, puffer_1, num_bins=20 ) )  # 0.135
    print(str("puffer-2: "),  KL_div( pensieve_train, puffer_2, num_bins=20 ) )  # 0.135
    print(str("puffer-3: "),  KL_div( pensieve_train, puffer_3, num_bins=20 ) )  # 0.135

    # print( str( "NG_low: " ), JS_div( pensieve_train, NG_low_test, num_bins=20 ) )  # 0.0098
    # print( str( "NG_middle: " ), JS_div( pensieve_train, NG_middle_test, num_bins=20 ) )  # 0.135
    # print( str( "NG_high: " ), JS_div( pensieve_train, NG_high_test, num_bins=20 ) )  # 0.0098
    # print( str( "NG_fixed: " ), JS_div( pensieve_train, NG_fixed_test, num_bins=20 ) )  # 0.135
    # print( str( "LTE: " ), JS_div( pensieve_train, LTE_test, num_bins=20 ) )  # 0.135
    # print( str( "3G: " ), JS_div( pensieve_train, test_3g, num_bins=20 ) )  # 0.135
    # print( str( "puffer-1: " ), JS_div( pensieve_train, puffer_1, num_bins=20 ) )  # 0.135
    # print( str( "puffer-2: " ), JS_div( pensieve_train, puffer_2, num_bins=20 ) )  # 0.135
    # print( str( "puffer-3: " ), JS_div( pensieve_train, puffer_3, num_bins=20 ) )  # 0.135



if __name__ == '__main__':
    main()
