.PHONY: env
env : 
	conda env create -f environment.yml
	conda activate ligo
	python -m ipykernel install --user --name ligo --display-name "ligo"



.PHONY: clean
clean :
	rm -f figures/*.png
	rm -f audio/*.wav
	rm -f _build/*

