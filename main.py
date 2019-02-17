# =======================================#
# Imports                                #
# =======================================#
# Python Imports
import os

# Module Imports
from Data.preprocess import *
from Data.grabLists import *
from src.checker import *

# =======================================#
# Globals & Constants                    #
# =======================================#

AISLES_CSV = os.path.join(os.getcwd(), 'Data', 'aisles.csv')
DEPARTMENTS_CSV = os.path.join(os.getcwd(), 'Data', 'departments.csv')
ORDERS_CSV = os.path.join(os.getcwd(), 'Data', 'orders.csv')
PRODUCTS_CSV = os.path.join(os.getcwd(), 'Data', 'products.csv')
PRIOR_ORDER_CSV = os.path.join(os.getcwd(), 'Data', 'order_products_prior.csv')
TEST_ORDER_CSV = os.path.join(os.getcwd(), 'Data', 'order_products_test.csv')
CHAIN_CSV = os.path.join(os.getcwd(), 'Data', 'orders_chain.csv')
CHAIN_DICT = os.path.join(os.getcwd(), 'Data', 'order_chain.json')
NEW_TEST_ORDERS = os.path.join(os.getcwd(), 'Data', 'orders_test.csv')
NEW_PRIOR_ORDERS = os.path.join(os.getcwd(), 'Data', 'orders_prior.csv')
TEST_DICT = os.path.join(os.getcwd(), 'Data', 'order_products_test_dict.json')
PRIOR_DICT = os.path.join(os.getcwd(), 'Data', 'order_products_prior_dict.json')
BEEF_JERKY_CHAIN = os.path.join(os.getcwd(),'Data','chain_test_beef_jerky.csv')
TRAIL_MIX_CHAIN = os.path.join(os.getcwd(),'Data','chain_test_trail_mix.csv')
PROTEIN_BARS_CHAIN = os.path.join(os.getcwd(),'Data','chain_test_protein_bars.csv')

# =======================================#
# Code                                  #
# =======================================#

beef_jerky_ids = product_lists(PRODUCTS_CSV, 'Beef Jerky', ['23'])
trail_mix_ids = product_lists(PRODUCTS_CSV, 'Trail Mix', ['117', '125'])
protein_bars_ids = product_lists(PRODUCTS_CSV, 'Protein Bar', [])

# reorganize_orders(ORDERS_CSV, NEW_PRIOR_ORDERS, NEW_TEST_ORDERS)
# reorganize_products(TEST_ORDER_CSV, PRIOR_ORDER_CSV, TEST_DICT, PRIOR_DICT, NEW_TEST_ORDERS)
# markov_orders(ORDERS_CSV, CHAIN_CSV)
# rechain_products(TEST_ORDER_CSV, PRIOR_ORDER_CSV, CHAIN_DICT, CHAIN_CSV)

# users_and_products(NEW_PRIOR_ORDERS, PRIOR_DICT, beef_jerky_ids, "beef_jerky")
# users_and_products(NEW_PRIOR_ORDERS, PRIOR_DICT, trail_mix_ids, "trail_mix")
# users_and_products(NEW_PRIOR_ORDERS, PRIOR_DICT, protein_bars_ids, "protein_bars")
# users_and_products(NEW_TEST_ORDERS, TEST_DICT, beef_jerky_ids, "beef_jerky")
# users_and_products(NEW_TEST_ORDERS, TEST_DICT, trail_mix_ids, "trail_mix")
# users_and_products(NEW_TEST_ORDERS, TEST_DICT, protein_bars_ids, "protein_bars")
users_and_products(CHAIN_CSV, CHAIN_DICT, beef_jerky_ids, "beef_jerky")
users_and_products(CHAIN_CSV, CHAIN_DICT, trail_mix_ids, "trail_mix")
users_and_products(CHAIN_CSV, CHAIN_DICT, protein_bars_ids, "protein_bars")