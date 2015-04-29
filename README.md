PTT Article Parser
==================
�@�ӥΨӤ��R PTT �峹���u��C

Features
--------
* �ھڤ峹���D�A���s�R�W�ɮצW��
* �ժ��w�C�W�[��

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

Notes
-----
* I love camel case.
* Big5UAO decoder was forked from [andycjw/uao_decode.py][UAO decoder].

[UAO decoder]: https://gist.github.com/andycjw/5617496
