import requests
import json

# 获取url
url = 'https://iam.myhuaweicloud.com/v3/auth/tokens'

adata = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "domain": {
                        "name": "hw46352545"
                    },
                    "name": "hw46352545",
                    "password": "acmghostmm2"
                }
            }
        },
        "scope": {
            "project": {
                "name": "cn-north-4"
            }
        }
    }
}
 
aheaders = {'Content-Type': 'application/json'}
response = requests.post(url, headers=aheaders, data = json.dumps(adata))
#print(response.text)
token = response.headers['X-Subject-Token']
#print(token)

# 获取访问结果
url = 'https://6975142dda5641d6852621508a439ff1.apig.cn-north-4.huaweicloudapis.com/v1/infers/a937bdf6-7d1e-42a5-ae88-1ee3e2a2bf6c'
url = 'https://6975142dda5641d6852621508a439ff1.apig.cn-north-4.huaweicloudapis.com/v1/infers/791a6314-20e7-44ef-aeca-396847cdc7d2'
headers={'user-agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
'X-Auth-Token':token}
#提交post请求
files = {'file':open('./test/image_0720.jpg','rb')}
result=requests.post(url,headers=headers, files=files)
print(result.text)
