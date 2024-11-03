import pandas as pd
import numpy as np
EC = pd.read_csv('EC.csv', sep=',')
EVP = pd.read_csv('EVP.csv', sep=',')
integral = EC.merge(EVP, on='Brand', how='outer')
describe_pd = integral.describe()
