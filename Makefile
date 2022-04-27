.PHONY: env
env : 
	conda env create -f environment.yml
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "ligo"
    
.PHONY: html : 
#	jupyter-book build hw06-kavinsuresh/
	jupyter-book build . #run all files as failsafe in case of directory name change



.PHONY: clean
clean :
	rm -f figures/*.png
	rm -f audio/*.wav
	rm -f _build/*

