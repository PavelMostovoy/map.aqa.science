# map_aqa_science
Service provider
##For make working gisdjango 

    on Windows you can use GDAL from  http://www.gisinternals.com/archive.php
    https://sandbox.idre.ucla.edu/sandbox/tutorials/installing-gdal-for-windows
    https://trac.osgeo.org/osgeo4w/
    
    or:
    Install Python 3.6 
    Create a virtual environment and activate it
    pip install django
    pip install psycopg2 (assuming you've setup PostgreSQL)
    pip install GDAL-2.2.4-cp36-cp36m-win_amd64.whl
    You can get that .whl here {https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal}. Take note of the warning there "Do not use together with       OSGeo4W or gdalwin32".
    add 2 system environment variables "GDAL_DATA" and "GDAL_LIB".

GDAL_DATA = C:\<path_to_your>\venv\Lib\site-packages\osgeo\data\gdal
GDAL_LIB = C:\<path_to_your>\venv\Lib\site-packages\osgeo
Then, add each variable to your system PATH like so: %GDAL_DATA% %GDAL_LIB%

Restart Pycharm and Fire up the django server
    
    on Mac : brew install gdal
    
    on raspbery : sudo apt-get install gdal-bin qgis
    
    on debian : sudo apt-get install libgdal-dev piror to pip install GDAL
    

## For connect Postgress DB on HEROCU 
 Pycharm:  string "?ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory?" 
 should be added at the end of URL
