PTT Article Parser
==================

一個用來分析 PTT 文章的工具。

Features
--------

* 根據文章標題或 .DIR 檔案，重新命名檔案名稱
* 白金緩慢增加中

Install
-------

From `pypi <https://pypi.org/project/ptt-article-parser/>`__::

	pip install ptt-article-parser

Usage
-----

::

  PTT Article Parser (PAP)

  Usage:
    pap rename [--format=<format>] [--dir=<file>] <file>...
    pap rename [--format=<format>] [--dir=<file>] --interactive
    pap (--help | --version)

  Options:
    -v --version          Show version.
    -h --help             Show this.
    -f --format=<format>  Set output format.
                          [default: [{board}] {title} [{author}] ({time:%Y%m%d%H%M%S}).ans]
    -d --dir=<file>       Read additional ".DIR" file. The tool always tries to
                          read the ".DIR" file under the parent folder of the
                          article. Use this option to read from other locations.
    -i --interactive      Use interactive mode, get file name from stdin.
    <file>                File path. If the file doesn't exists, pap will try to
                          parse it as glob pattern.

For example:

::

	pap rename ./M.*

Output screenshot
----------------------

.. image:: http://i.imgur.com/zISlFeP.png
   :alt: screenshot

Changelog
---------

* 0.5.0 (Jun 12, 2018)

  - Update dependencies.
  - Fix: handle crlf.
  - Refactor: ptt_article_parser.tools -> ptt_article_parser.rename
  - Drop uao_decode.py, switch to uao.

* 0.4.0 (Feb 19, 2018)

  - Change: automatically find .DIR file.

* 0.3.0 (Dec 5, 2017)

  - Parse .DIR file, use the title by default.

* 0.2.1 (May 14, 2016)

  - Extract author from old_edits.
  - Fix installing issue (maybe more?).

* 0.2.0 (Apr 16, 2016)

  - Change how glob pattern work.
  - Fix same file name bug.
  - Rewrite. Try matching best result.

* 0.1.0 (Apr 15, 2016)

  - First release.
