import requests



class Yunpian(object):
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    def send_sms(self,code,mobile):
        parmas = {
            'apikey':self.api_key,
            'mobile':mobile,
            'text':'【李智伟】您的验证码是{code}。如非本人操作，请忽略本短信'.format(code=code)
        }
        response = requests.post(self.single_send_url,data=parmas)
        import json
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == '__main__':
    yun_pian = Yunpian('320e7b1e52338c18facb36db6fcf2aa4')
    yun_pian.send_sms('2017','17634912005')