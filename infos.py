infos = {
    'name': '~', 
    'gender': '~',
    'date': {
        'year': 1900,
        'month': 1,
        'day': 1
        },
    'time': {
        'hour': 0,
        'minute': 0
        },
    'program': '~',
    'order': '~',
    'type': '~',
    'acupoint_title': '~',
    'acupoint': '~',
    'output': {
        'date_gan': '~',
        'date_zhi': '~',
        'date_idx': 0,
        'hour_gan': '~',
        'hour_zhi': '~',
        'hour_idx': 0,
        'LingGui8': {
            'JiuGongShu' : 0,
            'Hexagram': '~',
            'ZhuXue': '~',
            'PeiXue': '~'
            },
        'FeiTeng8': {
            'GuaWei' : 0,
            'Hexagram': '~',
            'ZhuXue': '~',
            'PeiXue': '~'
            },
        'NaZi': {
            'Bu1': '~',
            'Bu2': '~',
            'Bu3': '~',
            'XieXue': '~',
            'BenXue': '~',
            'YuanXue': '~'
            },
        'NaJia': {
            'ZhuXue': '~',
            'YuanXue': '~',
            'TodayHuYongXue': '~',
            'AdditionalXue': '~',
            'SpatialXue': []
            }
        }
    }

def get_hexagram_str(hexagram):
    hexagram_map = {
    '乾': '\u2630',
    '兑': '\u2631',
    '离': '\u2632',
    '震': '\u2633',
    '巽': '\u2634',
    '坎': '\u2635',
    '艮': '\u2636',
    '坤': '\u2637',
    }

    return f'{hexagram}{hexagram_map[hexagram]}' if hexagram in hexagram_map else hexagram

