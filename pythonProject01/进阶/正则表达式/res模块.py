# Python提供re模块，包含所有正则表达式的功能。由于Python的字符串本身也用\转义，所以要特别注意：
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com
import re
# . 匹配任意字符
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,}$'

def is_valid_email(email):
    return re.match(email_regex, email) is not None  #没匹配上的为空None
#验证email
print(is_valid_email("someone@gmail.com"))         # True
print(is_valid_email("bill.gates@microsoft.com"))  # True
print(is_valid_email("invalid-email@"))            # False
print(is_valid_email("bob@.com"))                  # False


# # 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob

# (?: ... )：这是一个非捕获组
named_email_rxgex = r'^(?:<([^>]+)>)?\s*([a-zA-Z0-9._%+-]+@[^>\s@]+)$'

def extract_name_or_username(email_str):
    match = re.match(named_email_rxgex, email_str)
    if match:
        name = match.group(1)  #括号里的名字
        username = match.group(2).split('@')[0] #用户名部分
        return name or username
    return None
#测试实例
print(extract_name_or_username("<Tom Paris> tom@voyager.org"))  # Tom Paris
print(extract_name_or_username("bob@example.com"))              # bob
print(extract_name_or_username("Alice <alice@example.com>"))    # Alice
print(extract_name_or_username("invalid@"))                     # None