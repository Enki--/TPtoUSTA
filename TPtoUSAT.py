import argparse
import requests

parser = argparse.ArgumentParser(description='Transfer data from TP to USAT')
parser.add_argument('-u', dest='user', type=str, required=True,
                    help='USAT Username')
parser.add_argument('-p', dest='pwd', type=str, required=True,
                    help='USAT Password')

args = parser.parse_args()


session = requests.Session()

paramsPost = {"password":args.pwd,"grant_type":"password","client_id":"NCCApp","username":args.user}
headers = {"Origin":"http://ncc.usatriathlon.org","Accept":"application/json, text/plain, */*","Cache-Control":"no-cache","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:32.0) Gecko/20100101 Firefox/32.0","Referer":"http://ncc.usatriathlon.org/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Pragma":"no-cache","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
response = session.post("http://usatauth.usatriathlon.org/token", data=paramsPost, headers=headers)

print("Status code:", response.status_code)
print("Response body:", response.content)
print("JSON:", response.json()['access_token'])
