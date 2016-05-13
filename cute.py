#! python3

from xcute import cute, Bump, Version

cute(
	test = 'readme_build',
	test_err = ["readme_show", "exit 1"],
	bump_pre = 'test',
	bump = Bump("ptt_article_parser/__init__.py"),
	bump_post = ['dist', 'release', 'publish', 'install'],
	dist = 'python setup.py sdist bdist_wheel',
	release = [
		'git add .',
		'git commit -m "Release v{version}"',
		'git tag -a v{version} -m "Release v{version}"'
	],
	publish = [
		'twine upload dist/*{version}[.-]*',
		'git push --follow-tags'
	],
	publish_err = 'start https://pypi.python.org/pypi/ptt-article-parser/',
	install = 'pip install -e .',
	install_err = 'elevate -c -w pip install -e .',
	readme_build = "python setup.py --long-description > %temp%/ld && rst2html --no-raw --exit-status=1 --verbose %temp%/ld %temp%/ld.html",
	readme_show = "start %temp%/ld.html",
	readme = "readme_build",
	readme_err = 'readme_show',
	readme_post = 'readme_show',
	version = [Version('ptt_article_parser/__init__.py'), 'echo {version}']
)
