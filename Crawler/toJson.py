#-*- coding: utf-8 -*-
__author__ = 'Aladin'

import json

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}], \
"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'



jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums")[1].get("number"))
print "我是中文！"

