# ETL and Feature Engineering

This package will provide base ETL functionality for 
handling data structured like standard market timeseries data

To build package using the requirements run the code below
```shell script
inv build
``` 

If you install any new python libraries then you need 
to rebuild the environment to add 
the new libraries to the requirements.txt
```shell script
inv rebuild
```

## Pipelines that exist in this package
* Load CSV into db file
* create new db file
* upload to existing db file
* load data from existing db file

### 1 - Load CSV data into db file



