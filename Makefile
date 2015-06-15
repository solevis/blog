build:
	bin/pelican -s solevis.cfg.py content

clean:
	rm -rfv output/
