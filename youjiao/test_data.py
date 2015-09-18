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