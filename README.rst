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

Dependencies
------------

* docopt
* safeprint

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
	  <file>                File path. You can use glob pattern

Example:

::

	pap.py rename "file1" "file2" "file3"

	
Output screenshot
----------------------

.. image:: http://i.imgur.com/zISlFeP.png
   :alt: screenshot

Notes
-----

* Big5UAO decoder was forked from `andycjw/uao_decode.py<https://gist.github.com/andycjw/5617496>`__.

Changelog
---------

* 0.1.0 (Apr 15, 2016)

  - First release.
