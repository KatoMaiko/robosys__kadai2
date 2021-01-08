## robosys__kadai2

## 作成者
上田隆一先生のコードをもとに改変し、自分で作成しました。

## youtube URL
https://youtu.be/tSVnBTGn_rA

## 動作環境
OS:Ubuntu 20.04

## インストール
```
$　cd ~/catkin_ws/src
$ git clone https://github.com/KatiMaiko/robosys_kadai2.git
```
→catkin_wsに置く


## 内容
count.pyにより現在時刻（秒）が出力される
count.pyではえんちゃん0匹と出力されるが、twice.pyではえんちゃん100（id）匹と出力される。
twice.pyではcount.pyで出力したデータとidを受け取り出力する。


## 動作方法
```
端末1$　cd catkin_ws/src
端末2　端末4$ cd catkin_ws/src
端末3$ cd catkin_ws

端末1$ roscore
端末2$ chmod +x count.py
端末2$ rosrun mypkg count.py
端末3$ rosnode list
端末3$ rostopic list
端末3$ rostopic echo /count_up
端末4$ chmod +x twice.py
端末4$ rosrun mypkg twice.py
```

## 協力者
・小村岳都

