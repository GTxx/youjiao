# -*- coding: utf-8 -*-
from collections import namedtuple


Book = namedtuple('Book', 'name, chief_editor, executive_editor, publisher, book_size, level, category, price, image_array')
book_list = [
    Book(u'清凉一夏', 'tanweihong', 'gaodi', u'江西幼教出版社', u'16开', u'小班', u'幼教教材', '30',
         [
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/1.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/2.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/3.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/4.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/5.jpg',
         ]),
    Book(u'有趣的手影', 'tanweihong', 'gaodi', u'江西幼教出版社', u'16开', u'中班', u'幼教教材', '30',
         [
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/6.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/2.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/3.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/4.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/5.jpg',
         ]),
    Book(u'你好秋天', 'tanweihong', 'gaodi', u'江西幼教出版社', u'16开', u'大班', u'幼教教材', '30',
         [
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/7.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/2.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/3.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/4.jpg',
             'http://7xj2zj.com2.z0.glb.qiniucdn.com/5.jpg',
         ])
]

Activity = namedtuple('Activity', 'title, html, status, category')
activity_list = [
    Activity(u'六年了 苹果的键盘和鼠标是否需要一次变革了？',
             u'2009 年，苹果正式发布了一款全新的无线蓝牙鼠标：Magic Mouse，它标配于 iMac，而对于其他 Mac 用户它却单独零售，但你不可否认它早已被 Mac 用户所熟知，主要因为它是世界上首个引入多点触控技术的鼠标，经蓝牙技术连接可以为 Mac 用户提供无与伦比的无线输入体验。',
             True, 'policy'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'policy'),
    Activity(u'苹果iOS 9认可朝鲜“平壤时间”：比韩国晚半小时',
             u'苹果昨天推送了iOS 9系统，它被认为苹果史上最重要的一次系统升级，不过有人说流畅，也有人反应变卡了。除了细节调整和功能改进，iOS 9还有个不为人注意的小地方：iOS 9系统首次认可了朝鲜的平壤时间，该时间比韩国首尔地区的时间晚了半小时，虽然平壤、首尔根本就是一个时区。',
             True, 'policy'),
    Activity(u'六年了 苹果的键盘和鼠标是否需要一次变革了？',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'news'),
    Activity(u'六年了 苹果的键盘和鼠标是否需要一次变革了？',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'news'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'events'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'events'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'research'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'research'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'activity'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'activity'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'policy'),
    Activity(u'[视频]苹果太空船总部最新航拍视频',
             u'自苹果“太空船总部”（Campus 2园区）开工以来，各界人士一直关注着它的施工进展，以至于经常有人每月或隔几周就使用无人机侦查一番。在美国劳动节周末，视频主Above Reno就带来了太空船总部的最新航拍视频，从视频上可以看到环形主楼和多层地下停车场的施工仍在继续，园区西边的次停车场则已近竣工，礼堂的内墙也已经搞得差不多。',
             True, 'policy'),
]