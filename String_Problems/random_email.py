import random
import string
from functools import reduce
from itertools import accumulate

random_digit = random.choice(string.digits)


def random_email_via_random_choice(domain='gmail', prefix=None, length=10):
    if prefix is None:
        prefix = 'test'
    if domain is None:
        domain = 'gmail'

    random_str = ''.join([random.choice(string.ascii_letters) for _ in range(length)])
    # random_digit = random.choice(string.digits)
    return prefix + '_' + random_digit + random_str + '@' + domain + '.com'


def random_email_via_random_choices(domain=None, prefix=None, length=5):
    if domain is None:
        domain = 'hotmail.com'

    if prefix is None:
        prefix = 'Test_Automation'

    random_str = "".join(random.choices(string.ascii_letters, k=length))
    # random_digit = random.choice(string.digits)
    return prefix + random_digit + random_str + '@' + domain


def random_email_via_reduce(domain=None, prefix=None, length=5):
    if domain is None:
        domain = 'hotmail.com'

    if prefix is None:
        prefix = 'Test_Automation'

    random_chars_list = [random.choice(string.ascii_letters) for _ in range(length)]
    # random_digit = random.choice(string.digits)
    random_str = reduce(lambda res, letter: res + letter, random_chars_list)
    return prefix + random_digit + random_str + '@' + domain


def random_email_via_accumulate(domain=None, prefix=None, length=5):
    if domain is None:
        domain = 'hotmail.com'
    if prefix is None:
        prefix = 'Test_Automation'

    random_chars_list = [random.choice(string.ascii_letters) for _ in range(length)]
    random_str = list(accumulate(random_chars_list, lambda res, letter: res + letter))[-1]
    # random_digit = random.choice(string.digits)
    return prefix + random_digit + random_str + '@' + domain


print(random_email_via_reduce(prefix="SSQATest", domain="gmail.com", length=3))
print(random_email_via_accumulate(prefix="SSQATest", domain="gmail.com",length=3))
print(random_email_via_random_choices(prefix="SSQATest", domain="gmail.com",length=3))
print(random_email_via_random_choice(prefix="SSQATest", domain="gmail",length=3))