PTT Article Parser
==================

一個用來分析 PTT 文章的工具。

Features
--------

* 根據文章標題，重新命名檔案名稱
* 白金緩慢增加中

Install
-------

::

	pip install ptt-article-parser

Usage
-----

::

	Usage:
	  pap rename [--format=<format>] <file>...
	  pap rename [--format=<format>] --interactive
	  pap --help
		
	Options:
	  -h --help             Show this.
	  -f --format=<format>  Set output format. 
							[default: [{board}] {title} [{author}] ({time:%Y%m%d%H%M%S}).ans]
	  -i --interactive      Use interactive mode, get file name from stdin.
	  <file>                File path. If the file doesn't exists, pap will try to parse it as glob pattern.

For example:

::

	pap rename ./M.*
	
Output screenshot
----------------------

.. image:: http://i.imgur.com/zISlFeP.png
   :alt: screenshot

Notes
-----

* Big5UAO decoder was forked from `andycjw/uao_decode.py<https://gist.github.com/andycjw/5617496>`__.

Todos
-----

* Identify article part and pushes part.

Dependencies
------------

* docopt
* safeprint

Changelog
---------

* 0.2.0 (Apr 16, 2016)

  - Change how glob pattern work.
  - Fix same file name bug.
  - Rewrite. Try matching best result.

* 0.1.0 (Apr 15, 2016)

  - First release.
