import hmac
import hashlib

#device_name = input('请输入device_name:')
#product_key = input('请输入product_key:')
#device_secret = input('请输入device_secret:')

device_name = 'node1'
product_key = 'a1HDTMmVX6c'
device_secret = 'oIvNXW7XGxGbcysRvnSqqGzu6LqgSbgf'

timestamp_srt = '789'
domain = 'iot-as-mqtt.cn-shanghai.aliyuncs.com'

host = product_key + '.' + domain
port = 1883
device_id = product_key + '.' + device_name
client_id = device_id + '|securemode=3,signmethod=hmacmd5,timestamp=' + timestamp_srt + '|'
username = device_name + '&' + product_key

hash_str = 'clientId' + device_id + 'deviceName' + device_name + 'productKey' + product_key + 'timestamp' + timestamp_srt

password = hmac.new(product_key.encode('utf-8'), hash_str.encode('utf-8'), hashlib.md5).hexdigest()

print('host:' + host)
#print('port:' + port)
print('device_id:' + device_id)
print('client_id:' + client_id)
print('username:' + username)
print('password:' + password)
