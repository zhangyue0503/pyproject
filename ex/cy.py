#-*- coding:utf-8 -*-

import re

v = '''
CMB 招商银行
SRCB 上海农村商业银行
ICBC 中国工商银行
BOB 北京银行
ABC 中国农业银行
CBHB 渤海银行
CCB 中国建设银行
BJRCB 北京农商银行
BOC 中国银行
NJCB 南京银行
SPDB 浦发银行
CEB 中国光大银行
BCOM 中国交通银行
BEA 东亚银行
CMBC 中国民生银行
PSBC 中国邮政
SDB 深圳发展银行
HZB 杭州银行
GDB 广东发展银行
PAB 平安银行
CITIC 中信银行
HSB 徽商银行
HXB 华夏银行
CZB 浙商银行
CIB 兴业银行
SHB 上海银行
NBCB 宁波银行
PSBC 中国邮政储蓄银行
'''

print v.split('\n')
