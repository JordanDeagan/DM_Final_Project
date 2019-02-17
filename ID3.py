# =======================================#
# Imports                                #
# =======================================#
# Python Imports
import os

# Module Imports
from src.predictive import *
from src.recurse import *
from Data.preprocess import parse_run_csv

# =======================================#
# Globals & Constants                    #
# =======================================#

BEEF_JERKY_PRIOR = os.path.join(os.getcwd(),'Data','orders_prior_beef_jerky.csv')
BEEF_JERKY_PRIOR_BOUGHT = os.path.join(os.getcwd(),'Data','orders_prior_beef_jerky_bought.csv')
TRAIL_MIX_PRIOR = os.path.join(os.getcwd(),'Data','orders_prior_trail_mix.csv')
TRAIL_MIX_PRIOR_BOUGHT = os.path.join(os.getcwd(),'Data','orders_prior_trail_mix_bought.csv')
PROTEIN_BARS_PRIOR = os.path.join(os.getcwd(),'Data','orders_prior_protein_bars.csv')
PROTEIN_BARS_PRIOR_BOUGHT = os.path.join(os.getcwd(),'Data','orders_prior_protein_bars_bought.csv')
BEEF_JERKY_TEST = os.path.join(os.getcwd(),'Data','orders_test_beef_jerky.csv')
TRAIL_MIX_TEST = os.path.join(os.getcwd(),'Data','orders_test_trail_mix.csv')
PROTEIN_BARS_TEST = os.path.join(os.getcwd(),'Data','orders_test_protein_bars.csv')
BEEF_JERKY_RESULTS = os.path.join(os.getcwd(),'classifier','beef_jerky_results.json')
TRAIL_MIX_RESULTS = os.path.join(os.getcwd(),'classifier','trail_mix_results.json')
PROTEIN_BARS_RESULTS = os.path.join(os.getcwd(),'classifier','protein_bar_results.json')
BEEF_JERKY_RESULTS_B = os.path.join(os.getcwd(),'classifier','beef_jerky_results_b.json')
TRAIL_MIX_RESULTS_B = os.path.join(os.getcwd(),'classifier','trail_mix_results_b.json')
PROTEIN_BARS_RESULTS_B = os.path.join(os.getcwd(),'classifier','protein_bar_results_b.json')

# bj_data = parse_run_csv(BEEF_JERKY_PRIOR)
# tm_data = parse_run_csv(TRAIL_MIX_PRIOR)
pb_data = parse_run_csv(PROTEIN_BARS_PRIOR)
# bj_data_b = parse_run_csv(BEEF_JERKY_PRIOR_BOUGHT)
# tm_data_b = parse_run_csv(TRAIL_MIX_PRIOR_BOUGHT)
pb_data_b = parse_run_csv(PROTEIN_BARS_PRIOR_BOUGHT)
# bj_test = parse_run_csv(BEEF_JERKY_TEST)
# tm_test = parse_run_csv(TRAIL_MIX_TEST)
pb_test = parse_run_csv(PROTEIN_BARS_TEST)
print('ready')
# bj_results = build_tree(bj_data,2,'true', 'false', [0,1])
# tm_results = build_tree(tm_data,2,'true', 'false', [0,1])
# pb_results = build_tree(pb_data,2,'true', 'false', [0,1])
# print('1')
# bj_results_b = build_tree(bj_data_b,2,'true', 'false', [0,1])
# tm_results_b = build_tree(tm_data_b,2,'true', 'false', [0,1])
# pb_results_b = build_tree(pb_data_b,2,'true', 'false', [0,1])
# print('2')

# with open(BEEF_JERKY_RESULTS, 'w') as out_file:
#     json.dump(bj_results, out_file)
# with open(TRAIL_MIX_RESULTS, 'w') as out_file:
#     json.dump(tm_results, out_file)
# with open(PROTEIN_BARS_RESULTS, 'w') as out_file:
#     json.dump(pb_results, out_file)
# print('3')
# with open(BEEF_JERKY_RESULTS_B, 'w') as out_file:
#     json.dump(bj_results_b, out_file)
# with open(TRAIL_MIX_RESULTS_B, 'w') as out_file:
#     json.dump(tm_results_b, out_file)
# with open(PROTEIN_BARS_RESULTS_B, 'w') as out_file:
#     json.dump(pb_results_b, out_file)
# print('4')

# bj_file = open(BEEF_JERKY_RESULTS)
# bj_str = bj_file.read()
# bj_read = json.loads(bj_str)
# bj_file_b = open(BEEF_JERKY_RESULTS_B)
# bj_str_b = bj_file_b.read()
# bj_read_b = json.loads(bj_str_b)
# tester(bj_data, bj_read, 2, 'true', 'false')
# tester(bj_test, bj_read, 2, 'true', 'false')
# tester(bj_data, bj_read_b, 2, 'true', 'false')
# tester(bj_test, bj_read_b, 2, 'true', 'false')

# tm_file = open(TRAIL_MIX_RESULTS)
# tm_str = tm_file.read()
# tm_read = json.loads(tm_str)
# tm_file_b = open(TRAIL_MIX_RESULTS_B)
# tm_str_b = tm_file_b.read()
# tm_read_b = json.loads(tm_str_b)
# tester(tm_data, tm_read, 2, 'true', 'false')
# tester(tm_test, tm_read, 2, 'true', 'false')
# tester(tm_data, tm_read_b, 2, 'true', 'false')
# tester(tm_test, tm_read_b, 2, 'true', 'false')

pb_file = open(PROTEIN_BARS_RESULTS)
pb_str = pb_file.read()
pb_read = json.loads(pb_str)
pb_file_b = open(PROTEIN_BARS_RESULTS_B)
pb_str_b = pb_file_b.read()
pb_read_b = json.loads(pb_str_b)
tester(pb_data, pb_read, 2, 'true', 'false')
tester(pb_test, pb_read, 2, 'true', 'false')
tester(pb_data, pb_read_b, 2, 'true', 'false')
tester(pb_test, pb_read_b, 2, 'true', 'false')