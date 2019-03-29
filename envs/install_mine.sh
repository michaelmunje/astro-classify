conda create -y --name galana-mine
source activate galana-mine
conda install -y --quiet --yes \
    'numpy' \
    'pandas' \
    'tensorflow' \
    'pytest' \
    'pytest-cov' \
    'keras'
conda install -y openjdk && \
conda clean -tipsy && \
pip install pytest-cov && \
conda install -c astropy astroquery && \
mkdir .astropy && \
pip uninstall -y keras-preprocessing && \
pip install git+https://github.com/keras-team/keras-preprocessing.git
