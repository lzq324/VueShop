import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=3429809891, re_url=redirect_url)

    print(auth_url)

def get_access_token(code="c407f9e6334718ef7f5159ae4d01a484"):
    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    re_dict = requests.post(access_token_url,data={
        'client_id':3429809891,
        'client_secret':'bb48aba0b49f5e09309e38ec2b4e8133',
        'grant_type':'authorization_code',
        'code':code,
        'redirect_uri': "http://127.0.0.1:8000/complete/weibo/"
    })
    # '{"access_token":"2.00w9QcCI4OIHkD2cce7e3ad00GgmJL","remind_in":"157679999","expires_in":157679999,"uid":"7367735090","isRealName":"true"}'
    pass

def get_user_info(access_token='',uid=''):
     user_url = 'https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}'.format(token=access_token,uid=uid)
     print(user_url)


if __name__ == "__main__":
    # get_auth_url()
    # get_access_token(code="c407f9e6334718ef7f5159ae4d01a484")
    get_user_info(access_token='2.00w9QcCI4OIHkD2cce7e3ad00GgmJL',uid='7367735090')