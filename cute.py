#! python3

from xcute import cute

def readme():
    """Live reload readme"""
    from livereload import Server
    server = Server()
    server.watch("README.rst", "py cute.py readme_build")
    server.serve(open_url_delay=1, root="build/readme")

cute(
	pkg_name = "ptt_article_parser",
	test = ["pylint {pkg_name}", 'readme_build'],
	bump_pre = 'test',
	bump_post = ['dist', 'release', 'publish', 'install'],
	dist = 'x-clean build dist && python setup.py sdist bdist_wheel',
	release = [
		'git add .',
		'git commit -m "Release v{version}"',
		'git tag -a v{version} -m "Release v{version}"'
	],
	publish = [
		'twine upload dist/*',
		'git push --follow-tags'
	],
	install = 'pip install -e .',
	readme_build = [
        'python setup.py --long-description | x-pipe build/readme/index.rst',
        ('rst2html5.py --no-raw --exit-status=1 --verbose '
         'build/readme/index.rst build/readme/index.html')
    ],
    readme_pre = "readme_build",
    readme = readme
)
