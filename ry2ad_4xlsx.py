# This py is used to convert all regnal years in an excel column
ry_col = 3 # start from 0
p = './test/text.txt'

import ry2ad
import helper.process_file as pf

def main():
    result = []
    ll = pf.csvintolist(pf.read_file(p, 'utf-16le bom'))
    for l in ll:
        ry_s = l[ry_col]
        print(ry_s)
        result.append(ry2ad.ry2ad(ry_s))
    s = '\n'.join(str(r) for r in result)
    pf.write_into_file(p+'.out.txt', s)
    return 0

if __name__ == "__main__":
    main()

