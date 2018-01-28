
import numpy as np
import pandas as pd

_line_sep = "="

df = pd.read_csv("train.csv")

print _line_sep * 80
print "DataFrame created ...."
print "list of columns"
print df.columns

print "Sample first lines"

