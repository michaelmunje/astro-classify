from astroquery.ned import Ned
import astropy.units as u
from astropy.io import ascii

# result_table = Ned.query_region("NGC 4151", radius=1 * u.deg)
# print(result_table)
# data = ascii.read('ngc_4151.tbl')
# result_table = Ned.query_refcode('1990PASJ...42..603S')
# print(result_table)
# result_table = result_table.to_pandas()
# print('This is the length', len(result_table))

# result_table = Ned.query_object("CGMW 1-1")
# print(result_table)

# 866
# result_table = Ned.query_refcode('2013AJ....145..101K')
# print(result_table)
# result_table = result_table.to_pandas()
# print('This is the length', len(result_table))

# 1074
# result_table = Ned.query_refcode('1995AJ....109.1498H')
# result_table = result_table.to_pandas()
# print('This is the length', len(result_table))

# 1
# result_table = Ned.query_refcode('1990PASJ...42..603S')
# result_table = result_table.to_pandas()
# print('This is the length', len(result_table))

##
result_table = Ned.query_object('UGC 5849')
result_table = result_table.to_pandas()
print(result_table)
print('This is the length', len(result_table))
