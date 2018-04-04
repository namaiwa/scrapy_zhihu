import json

t = '{"is_followed": false, "avatar_url_template": "https://pic1.zhimg.com/5fb8f28f4fd2b7e245d3ceeecab8e431_{size}.jpg", "user_type": "people", "answer_count": 10, "is_following": false, "headline": "\u5efa\u7b51\u5b66\u256e(\u256f\u25bd\u2570)\u256d\n\u5b66\u751f?\n\u55ef(\u2299v\u2299)", "url_token": "nie-zi-chuan-98", "id": "4bd6b51dd77bb4c676160e90533708a0", "allow_message": false, "articles_count": 0, "is_blocking": false, "type": "people", "name": "\u5c0f\u76f4\u623f", "url": "http://www.zhihu.com/api/v4/people/4bd6b51dd77bb4c676160e90533708a0", "gender": 1, "is_advertiser": false, "avatar_url": "https://pic1.zhimg.com/5fb8f28f4fd2b7e245d3ceeecab8e431_is.jpg", "is_org": false, "follower_count": 2, "employments": [], "badge": []}'
a = t.split(',')
for w in a:
    s = w.split('":')[0]
    print(s+'"')

