#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from weather_helper import *
from mail_helper import *

TARGET = [
    ('shenzhen', 'yangruihan@vip.qq.com')
]


def main():
    suc_count = 0
    for (index, (location, email)) in enumerate(TARGET):
        print("开始查询第%s条天气" % (index + 1))
        try:
            result = get_result(location)
            send_mail([email], '天气', result)
            suc_count += 1
            print("第%s条天气查询完毕" % (index + 1))
        except Exception as e:
            print(e)
            print("第%s条天气出现异常" % (index + 1))

    print("\n全部执行完毕，共查询%s条天气" % suc_count)


if __name__ == '__main__':
    main()
