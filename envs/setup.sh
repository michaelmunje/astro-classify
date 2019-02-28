conda create -y -n astro-classify tensorflow-gpu pandas numpy
conda create -y -n astro-classify-test tensorflow pandas numpy
conda create -y -n astro-classify-mine pandas numpy selenium
source activate astro-classify-mine
pip install astroquery
