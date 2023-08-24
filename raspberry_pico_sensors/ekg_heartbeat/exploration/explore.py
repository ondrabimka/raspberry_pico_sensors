# %%
import pandas as pd

data = pd.read_csv("exploration/ekg_data.txt", names=['time','empty_test'])

# %%
data

# %%
data['empty_test'][1000:1200].plot()
# %%
