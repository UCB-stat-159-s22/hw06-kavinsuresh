.PHONY: env
env :
	conda env create -f environment.yml
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "ligo"
    
.PHONY: html
html :
#	jupyter-book build hw06-kavinsuresh/
	jupyter-book build . #run all files as failsafe in case of directory name change

.PHONY: html-hub
html-hub :
	jupyter-book config sphinx .
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	cd _build/html
	python -m http.server

#	@echo "Visit the following URL to view the Jupyter Book: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"
#	python -m http.server
#	(info Visit the following URL to view the Jupyter Book: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html)
#	@echo "Visit the following URL to view the Jupyter Book: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"


.PHONY: clean
clean :
	rm -f figures/*.png
	rm -f audio/*.wav
	rm -r _build/html/*.html
	rm -r _build/html/*.inv

