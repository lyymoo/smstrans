'''

社保缴存基数：4900
基本住房公积金缴存基数：4900
五险一金汇缴明细  个人应缴部分      单位应缴部分：
养老保险金：      392.00  (8%)     980.00  (20%)
医疗保险金：      98.00   (2%)     465.50  (9.5%)
失业保险金：      24.50   (0.5%)   24.50   (0.5%)
基本住房公积金：  343.00  (7%)     343.00  (7%)
补充住房公积金：  0.00    (0%)     0.00    (0%)
工伤保险金：                       9.80    (0.2%)
生育保险金：                       49.00   (1%)
共计支出：        857.50           1871.80
个人所得税：      计算参照《中华人民共和国个人所得税法》
税后月薪：        工资金额 － 各项社会保险费 － 个人所得税

上海社保、公积金个人缴存比例
养老保险：8%
医疗保险：2%
失业保险：0.5%
工伤保险：0%
生育保险：0%
公积金：7%

十三届全国人大常委会第五次会议31日表决通过关于修改个人所得税法的决定。
决定自2019年1月1日起施行，但工资、薪金所得基本减除费用标准（即“起征点”）
从现行每月3500元提高至每月5000元等部分减税政策，将从2018年10月1日起先行实施，
以尽早释放改革红利。
http://www.npc.gov.cn/npc/xinwen/2018-08/31/content_2060151.htm

个人所得适用
1 不超过36000元的 3
2 超过36000元至144000元的部分 10
3 超过144000元至300000元的部分 20
4 超过300000元至420000元的部分 25
5 超过420000元至660000元的部分 30
6 超过660000元至960000元的部分 35
7 超过960000元的部分 45
经营所得适用
1 不超过30000元的 5
2 超过30000元至90000元的部分 10
3 超过90000元至300000元的部分 20
4 超过300000元至500000元的部分 30
5 超过500000元的部分 35

中华人民共和国个人所得税的计算公式如下：
# 公式1：应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(5000元)
# 方式一
# 公式2：应纳税额 = 应纳税所得额 × 税率 － 速算扣除数
# 方式二
# 公式2：根据应纳税所得额的分布界限按对应征收比率计算

'''
income_all = 16000
social_security_payment_base = 4900
basic_housing_provident_fund_reserve_base = 4900

endowment_insurance = social_security_payment_base * 0.08
medical_insurance = social_security_payment_base * 0.02
unemployment_insurance = social_security_payment_base * 0.005
employment_injury_insurance = 0
maternity_insurance = 0
housing_provident_fund_reserve = basic_housing_provident_fund_reserve_base * 0.07

all_social_security_amount = endowment_insurance + \
medical_insurance + \
unemployment_insurance + \
employment_injury_insurance + \
maternity_insurance + \
housing_provident_fund_reserve

# 公式1
taxable_income = income_all - all_social_security_amount - 5000
# 速算扣除数如下
level_3 = 36000 / 12
level_10 = 144000 / 12
level_20 = 300000 / 12
level_25 = 420000 / 12
level_30 = 660000 / 12
level_35 = 960000 / 12
level_45 = level_35


def table(taxable_income):
    '''速算扣除数 计算方法
    return 1: rate
    return 2: 合并同类项抽象封装

    多项式中运用加法交换律及合并同类项法则进行合并举例：
    (5642.5 - 3600) * 0.1 + 3600 * 0.03
    s = 5642.5 * 0.1  - 3600 * (0.1 - 0.03)

    (13000 - 12000) * 0.2 + (12000 - 3600) * 0.1 + 3600 * 0.03 
    s = 13000 * 0.2 - (12000 * (0.2 - 0.1) + 3600 * (0.1 - 0.03))
    '''
    r1 = level_3 * (0.1 - 0.03)
    r2 = level_10 * (0.2 - 0.1) + r1
    r3 = level_20 * (0.25 - 0.2) + r2
    r4 = level_25 * (0.30 - 0.25) + r3
    r5 = level_30 * (0.35 - 0.30) + r4
    r6 = level_35 * (0.45 - 0.35) + r5
    if level_3 >= taxable_income:
        return 0.03, 0
    elif level_10 >= taxable_income > level_3:
        return 0.1, r1
    elif level_20 >= taxable_income > level_10:
        return 0.2, r2
    elif level_25 >= taxable_income > level_20:
        return 0.25, r3
    elif level_30 >= taxable_income > level_25:
        return 0.30, r4
    elif level_35 >= taxable_income > level_30:
        return 0.35, r5
    elif taxable_income > level_45:
        return 0.45, r6

def table2(taxable_income):
    '''根据应纳税所得额的分布界限按对应征收比率计算 计算方法
    return: tax_payable

    个人所得适用
    1 不超过36000元的 3
    2 超过36000元至144000元的部分 10
    3 超过144000元至300000元的部分 20
    4 超过300000元至420000元的部分 25
    5 超过420000元至660000元的部分 30
    6 超过660000元至960000元的部分 35
    7 超过960000元的部分 45

    方式二 公式2 计算举例：
    (5642.5 - 3600) * 0.1 + 3600 * 0.03

    (13000 - 12000) * 0.2 + (12000 - 3600) * 0.1 + 3600 * 0.03 
    '''
    r1 = level_3 * 0.03
    r2 = (level_10 - level_3) * 0.1 + r1
    r3 = (level_20 - level_10) * 0.2 + r2
    r4 = (level_25 - level_20) * 0.25 + r3
    r5 = (level_30 - level_25) * 0.30 + r4
    r6 = (level_35 - level_30) * 0.35 + r5
    if level_3 >= taxable_income:
        return 0.03 * taxable_income
    elif level_10 >= taxable_income > level_3:
        return 0.1 * (taxable_income - level_3) + r1
    elif level_20 >= taxable_income > level_10:
        return 0.2 * (taxable_income - level_10) + r2
    elif level_25 >= taxable_income > level_20:
        return 0.25 * (taxable_income - level_20) + r3
    elif level_30 >= taxable_income > level_25:
        return 0.30 * (taxable_income - level_25) + r4
    elif level_35 >= taxable_income > level_30:
        return 0.35 * (taxable_income - level_30) + r5
    elif taxable_income > level_45:
        return 0.45 * (taxable_income - level_35) + r6

# 速算扣除数计算
rate, payable_temp = table(taxable_income)
# 方式一：公式2
tax_payable = taxable_income * rate - payable_temp

print(income_all)
print(income_all - all_social_security_amount - tax_payable)
# 方式一与方式二计算结果比较 性能上差异可能性：取决于Python解释器在处理判断内运算（方式二）与判断外运算（方式一）的效率高低的差异性
print(tax_payable == table2(taxable_income))
