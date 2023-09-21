import copy


def money_en_to_cn(money_en):
    '''
    此方法对各种数据验证都通过
    :return:
    '''
    # money_en  = 12345678
    # money_en  = 10100010
    # money_en  = 10101010
    # money_en  = 10100110
    # money_en  = 10100101
    # money_en = 1010101.20
    num_list = [{'0': '零', '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'},
                '拾', '佰', '仟', '万']

    decimal_list = ['角', '分']

    def func(b):
        ns = ''
        for x in range(1, len(b)):
            num = num_list[0][b[x]]
            word = num + (num_list[x] if b[x] != '0' else '')
            ns = word + ns

        return ns + (num_list[0][b[0]] if b[0] != '0' else '')

    NUM_LINE = 10000
    money_cn = ''
    if money_en == 0:
        return '零圆'

    aa = copy.copy(int(money_en))
    unit = '圆'
    while aa % NUM_LINE:
        b = str(aa % NUM_LINE)[::-1]
        if len(str(aa)) > 4 and len(str(b)) != 4:
            b = b + '0'
        money_cn = func(b) + unit + money_cn
        aa = aa // NUM_LINE
        unit = '万' if aa else '圆'

    if isinstance(money_en, float):
        ab = round(money_en, 2)
        ab = str(ab).split('.')[1]
        if ab != "00" and ab != "0":
            for x in range(0, len(ab)):
                num = num_list[0][ab[x]]
                word = num + (decimal_list[x] if ab[x] != '0' else '')
                money_cn += word

    return money_cn

# print(money_en_to_cn(11123))
