
# 定义货币类
class CurrencyConverter():
    # 定义货币符号、最小单位和中文名称的映射
    currency_data = {
        'USD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '美元'},
        'EUR': {'symbol': '€', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '欧元'},
        'GBP': {'symbol': '£', 'subunit': 'pence', 'subunit_value': 100, 'chinese_name': '英镑'},
        'JPY': {'symbol': '¥', 'subunit': 'sen', 'subunit_value': 1, 'chinese_name': '日元'},
        'CNY': {'symbol': '¥', 'subunit': 'fen', 'subunit_value': 100, 'chinese_name': '人民币'},
        'CAD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '加拿大元'},
        'AUD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '澳大利亚元'},
        'CHF': {'symbol': 'CHF', 'subunit': 'rappen', 'subunit_value': 100, 'chinese_name': '瑞士法郎'},
        'SGD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '新加坡元'},
        'HKD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '港元'},
        'NZD': {'symbol': '$', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '新西兰元'},
        'SEK': {'symbol': 'kr', 'subunit': 'öre', 'subunit_value': 100, 'chinese_name': '瑞典克朗'},
        'NOK': {'symbol': 'kr', 'subunit': 'øre', 'subunit_value': 100, 'chinese_name': '挪威克朗'},
        'DKK': {'symbol': 'kr', 'subunit': 'øre', 'subunit_value': 100, 'chinese_name': '丹麦克朗'},
        'INR': {'symbol': '₹', 'subunit': 'paise', 'subunit_value': 100, 'chinese_name': '印度卢比'},
        'KRW': {'symbol': '₩', 'subunit': 'jeon', 'subunit_value': 1, 'chinese_name': '韩国元'},
        'RUB': {'symbol': '₽', 'subunit': 'kopek', 'subunit_value': 100, 'chinese_name': '俄罗斯卢布'},
        'ZAR': {'symbol': 'R', 'subunit': 'cent', 'subunit_value': 100, 'chinese_name': '南非兰特'},
        'BRL': {'symbol': 'R$', 'subunit': 'centavo', 'subunit_value': 100, 'chinese_name': '巴西雷亚尔'},
        'MXN': {'symbol': '$', 'subunit': 'centavo', 'subunit_value': 100, 'chinese_name': '墨西哥比索'},
    }

    def __init__(self, code:str, value:float):
        self.code = code
        self.value = value

    def get_symbol(self)->str:
        return self.currency_data[self.code]['symbol'] if self.code in self.currency_data else None

    def get_subunit_value(self)->int:
        if(self.code not in self.currency_data):
            return None
        if(self.value == None):
            return None
        subunit_value = self.currency_data[self.code]['subunit_value']
        total_subunits = int(round(self.value * subunit_value,0))
        return total_subunits
    
    def get_currency_code(self):
        return self.code

    def get_subunit_name(self):
        return self.currency_data[self.code]['subunit'] if self.code in self.currency_data else None
    
    def get_currency_symbol(self):
        return self.currency_data[self.code]['symbol'] if self.code in self.currency_data else None
    
    def get_chinese_name(self):
        return self.currency_data[self.code]['chinese_name'] if self.code in self.currency_data else None


# 示例使用
if __name__ == "__main__":
    currency = CurrencyConverter('USD', 1)
    print(f"货币符号: {currency.get_symbol()}")
    total_subunits = currency.get_subunit_value()
    print(f"最小单位值: {total_subunits} {currency.get_subunit_name()}")
    print(f"货币中文名称: {currency.get_chinese_name()}")
    print(int(round(0.91,0)))