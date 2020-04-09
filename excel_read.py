import pandas as pd
import numpy as np

def read_excel(s):
    data = pd.read_excel(s)
    head = data.head(0)
    if '位置 X' in head and '位置 Y' in head:
        x = data['位置 X']
        y = data['位置 Y']
        if x.shape == y.shape:
            p = np.asarray(list(zip(x,y)))
            # print(p.shape)
        return p
    else:
        return None


def main():

    read_excel('./a.xls')

if __name__ == '__main__':
    main()