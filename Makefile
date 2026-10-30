.PHONY: build search serve clean

build:
	uv run pelican content -s pelicanconf.py
	$(MAKE) search

search:
	uv run python -m pagefind --site docs

serve: build
	uv run pelican content -s pelicanconf.py --listen --autoreload

clean:
	rm -rf docs
