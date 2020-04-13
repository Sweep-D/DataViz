import pandas as pd

raw_data = {'names': ['Nick', 'Panda', 'S', 'Ari', 'Valos'],
            'jan_ir': [123, 122, 101, 106, 365],
            'feb_ir': [123, 144, 176, 106, 22],
            'mar_ir': [133, 122, 566, 32, 22]}

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])

df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['march_ir']

print(df)
