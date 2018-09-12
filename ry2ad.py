# convert chinese regnal year to A.D.
# at present: from **QING Qianlong Dynasty**

import helper.cn2dig as cn2dig
import helper.process_file as pf
import re

p_src_tb = "./src/ry2AD_sketch.txt"
ll_src_tb = pf.csvintolist(pf.read_file(p_src_tb, coding="utf-16le bom"))
d_src_tb = {m:n for m,n in ll_src_tb}

p = r'('+'|'.join(d_src_tb.keys())+\
    r')([元一二三四五六七八九十][一二三四五六七八九十]?[一二三四五六七八九十]?)年'
c = re.compile(p)

def ry2ad(s):
    m = c.search(s)
    if not m: return -1 # not existed: regnal year
    r = m.group(1)
    y_cn = m.group(2)
    y0_s = d_src_tb.get(r, None)
    if not y0_s: return -2 # not existed: regnal
    y0 = int(y0_s)
    if y_cn == '元':
        y = 1
    else:
        y = cn2dig.cn2dig(y_cn)
    if not y: return -3 # not existed: year
    return y-1+y0

if __name__ == '__main__':
    x = ''
    while x!='exit':
        x = input('> ')
        print(ry2ad(x))




