PTT Article Parser
==================
一個用來分析 PTT 文章的工具。

Features
--------
* 根據文章標題，重新命名檔案名稱
* 白金緩慢增加中

Todos
-----
* Identify article part and pushes part.
* Disallow multiple spaces after keyword?

Dependencies
------------
Install python 3.
https://www.python.org/

Install `docopt`.
```
pip install docopt
```

Usage
-----
```
Usage:
  pap.py rename [--format=<format>] <file>...
  pap.py --help

Options:
  -h --help             Show this.
  -f --format=<format>  Set output format.
                        [default: [@board] @title by @author.@time.ans]
```
Example:
```
pap.py rename "file1" "file2" "file3"
```

Output screenshot
----------------------
![screenshot](http://i.imgur.com/zISlFeP.png)

Notes
-----
* I love camel case.
* Big5UAO decoder was forked from [andycjw/uao_decode.py][UAO decoder].

[UAO decoder]: https://gist.github.com/andycjw/5617496
