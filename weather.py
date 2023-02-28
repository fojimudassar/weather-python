import pandas as pd
import os


folder_path = '/home/muddassirrazzaq/Drive_D/Python/weatherfiles'
for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'r') as f:
        file_contents = f.read()

        print(file_contents)