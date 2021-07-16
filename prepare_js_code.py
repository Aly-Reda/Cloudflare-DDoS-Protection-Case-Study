import re
import requests
import re
import js2py
import json
from pyquery import PyQuery as pq

code = open('code.js').read()

b = code.split("'.split")[0].split("b = '")[1].split(',')
all_c = re.findall(r'c\(\'0x[a-z0-9]+\'\)',code)
pre_code = 'b ='+code.split('b = ')[1][:-3]
pre_code = pre_code.split(', d = this || self')[0]
script = js2py.eval_js( pre_code)
new_c = [ [ x , f"""'{script(x.split("'")[1])}'""" ]  for x in  all_c]
for c in  new_c:
      code = code.replace(c[0],c[1])
code = code.replace("e['attachEvent']","")
open("code_after.js", "w+").write(code)
