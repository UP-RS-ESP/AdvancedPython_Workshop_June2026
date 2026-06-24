# INITIATE: Advanced Python Workshop (June2026)

Python workshop at the University of Potsdam: Regression, Parallelization, GPU Programming, Random Forest / XGBoost Classification, Convolution Neural Networks

Please create a new conda environment 'geodata' and install the following packages (or use pip or uv) :
```bash
conda create -n geodata -c conda-forge python=3.12
conda activate geodata
conda install -c conda-forge python=3.12 ipython jupyterlab multiprocess numba xarray dask tqdm numpy statsmodels scipy gdal scikit-image scikit-learn xgboost seaborn matplotlib cartopy pandas geopandas graphviz ipycytoscape netcdf4 rioxarray

```


Adding Google to the XYZ tiles in QGIS: https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}

Copernicus DEM Data for GPU Exercise:
https://www.dropbox.com/scl/fi/3exc11zfuche3c7ty3g6f/COP_10m_PunaECordillera_int16_epsg32719.tif?rlkey=2n2ykmfwikqnx306wz1ig5i0b&st=7s61qbbi&dl=0

Hillshade Version:
https://www.dropbox.com/scl/fi/0bhd3gt4ais0654qgu7ku/COP_10m_PunaECordillera_int16_epsg32719_hs.tif?rlkey=09yjh599b0ibclyzkjla8off2&st=s7s1osz9&dl=0

