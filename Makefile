build: clean
	python bootstrap.py
	./bin/buildout -v

clean:
	rm -rf .env .installed.cfg .mr.developer.cfg
	rm -rf parts eggs develop-eggs bin externals-src
	rm -f runserver syncdb
	find src/wwcw7 -name "*.pyc" -type f -delete
	find src/wwcw7 -name "*.pyo" -type f -delete

lint_modified:
	svn status | grep ^M | cut -d' ' -f8 | xargs py_static_check -i

translate-ja:
	./bin/manage makemessages --locale=ja --ignore=eggs/* --ignore=develop-eggs/* --ignore=.env/* --ignore=bin/* --ignore=scripts/* --ignore=wsgi/* --ignore=externals-src/*

translate: translate-ja
	./bin/manage compilemessages
