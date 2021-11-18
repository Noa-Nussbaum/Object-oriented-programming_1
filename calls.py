import csv

import numpy
import numpy as np

class calls:

    # Let's upload the csv file
    def __init__(self, file_name):
        CAddress=open(file_name)
        csvreader = csv.reader(CAddress)
        rows = []
        for row in csvreader:
            rows.append(row)
        CAddress.close
        self.calls = np.array(rows)

    def get_calls(self):
        return self.calls

    def __str__(self):
         return print(self.calls)

    def __int__(self,i,j):
        return print(self.calls[i][j])