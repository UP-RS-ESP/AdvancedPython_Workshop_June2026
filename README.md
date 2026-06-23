# INITIATE: Advanced Python Workshop (June2026)

Python workshop at the University of Potsdam: Regression, Parallelization, GPU Programming, Random Forest / XGBoost Classification, Convolution Neural Networks

Please create a new conda environment 'geodata' and install the following packages (or use pip or uv) :
```bash
conda create -n geodata -c conda-forge python=3.12
conda activate geodata
conda install -c conda-forge python=3.12 ipython jupyterlab multiprocess numba xarray dask tqdm numpy statsmodels scipy gdal scikit-image scikit-learn xgboost seaborn matplotlib cartopy pandas geopandas graphviz ipycytoscape netcdf4 rioxarray

```


Adding Google to the XYZ tiles in QGIS: https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}
