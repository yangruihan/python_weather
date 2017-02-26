#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import json
import requests


KEY = ''
API = 'https://api.thinkpage.cn/v3/weather/daily.json'


def fetch_weather(location, start=0, days=7):
    params = {
        'key': KEY,
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c',
        'start': start,
        'days': days
    }

    result = requests.get(API, params)
    return result.text


def parse_daily(daily_weather):
    result = ''
    result += '日期: %s\n' % daily_weather['date']
    result += '\t温度: %s°-%s°\n' % (daily_weather['low'], daily_weather['high'])
    result += '\t白天: %s\t夜间: %s\n' % (
        daily_weather['text_day'], daily_weather['text_night'])

    return result


def parse_result(result):
    result = json.loads(result)
    string = ""

    location = result['results'][0]['location']['name']
    string += location + "天气预报：\n\n"

    daily_weather = result['results'][0]['daily']
    string += '\n'.join(map(parse_daily, daily_weather))
    return string


def get_result(location):
    return parse_result(fetch_weather(location))


def main():
    location = 'wuhan'
    parse_result(get_result(location))


if __name__ == '__main__':
    main()
