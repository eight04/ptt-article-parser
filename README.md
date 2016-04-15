PTT Article Parser
==================
�@�ӥΨӤ��R PTT �峹���u��C

Features
--------
* �ھڤ峹���D�A���s�R�W�ɮצW��
* �ժ��w�C�W�[��

Todos
-----
* Identify article part and pushes part.

Dependencies
------------
Install python 3.
https://www.python.org/

Install `docopt`.
```
pip install docopt
```

Install `safeprint`
```
pip install safeprint
```

Usage
-----
```
Usage:
  pap.py rename [--format=<format>] <file>...
  pap.py rename [--format=<format>] --interactive
  pap.py --help
	
Options:
  -h --help             Show this.
  -f --format=<format>  Set output format. 
                        [default: [@board] @title by @author.@time.ans]
  -i --interactive      Use interactive mode, get file name from stdin.
  <file>                File path. You can use glob pattern
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
* Big5UAO decoder was forked from [andycjw/uao_decode.py][UAO decoder].

[UAO decoder]: https://gist.github.com/andycjw/5617496
