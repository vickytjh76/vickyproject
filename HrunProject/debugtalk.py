import pdb
import time

def sleep(n_secs):
    time.sleep(n_secs)

def base_url():
    url = 'https://www.21cake.com'
    return url

def get_url(**kwargs):
    pop_url = kwargs.pop('url')
    # pdb.set_trace()
    r_url = pop_url + '?'
    for k,v in kwargs.items():
        if isinstance(v,int):
            v = str(v)
        r_url = r_url + k + '=' + v + '&'
    return r_url[:-1]

#从URL中获取商品的id
#Referer_url = 'https://www.21cake.com/goods-1095.html'
def get_goods_id(Referer_url):
    goods = Referer_url[29:]
    good_id = goods[:4]
    return good_id

