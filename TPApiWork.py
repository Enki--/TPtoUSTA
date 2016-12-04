import requests
import argparse

parser = argparse.ArgumentParser(description='Pull TP data')
parser.add_argument('-u', dest='user', type=str, required=True,
                    help='TP Username')
parser.add_argument('-p', dest='pwd', type=str, required=True,
                    help='TP Password')
parser.add_argument('-s', dest='start', type=str,
                    help='startDate', default='2016-11-30')
parser.add_argument('-d', dest='end', type=str,
                    help='endDate', default='2016-11-30')

args = parser.parse_args()

proxies = {
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080'
}
with requests.session() as session:
    session.get('http://trainingpeaks.com/', verify=False, proxies=proxies)
    session.get('https://home.trainingpeaks.com/refresh', verify=False, proxies=proxies)

    paramsGet = {"aliaspath":"/Login"}
    paramsPost = {"submit":"","Username":args.user,"Password":args.pwd}
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:32.0) Gecko/20100101 Firefox/32.0","Referer":"https://home.trainingpeaks.com/login","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded"}
    response = session.post("https://home.trainingpeaks.com/login", data=paramsPost, params=paramsGet, headers=headers, proxies=proxies, verify=False)


    headers = {"Origin":"https://app.trainingpeaks.com","Accept":"application/json, text/javascript, */*; q=0.01","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:32.0) Gecko/20100101 Firefox/32.0","Referer":"https://app.trainingpeaks.com/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate","Content-Type":"application/json"}
    response = session.get("https://tpapi.trainingpeaks.com/fitness/v1/athletes/301395/workouts/" + args.start + "/" + args.end + "/", headers=headers, proxies=proxies, verify=False)

    print("Status code:", response.status_code)
    print("Response body:", response.json())
