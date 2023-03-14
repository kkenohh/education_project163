# Analysis of Education Attainment and Income of PUMA Regions in Washington
Report by Alison, Ken, Willis

CSE 163: Intermediate Data Programming

Professor: Hunter Schafer

insert info about presentation

## Required Libraries:
* `Pandas`
* `Dash`
* `Numpy`
* `Sklearn`
* `Plotly`
> **Installation Line:** pip install pandas dash numpy sklearn plotly

## Required Data:
You will need the following data:

- *educational_attainment.csv* => data/educational_attainment.csv
    - Contains original data from data.wa.gov regarding edcucational attainment levels of PUMA regions in WA
- *employment_status_2013.csv* => data/employment_status_2013.csv
    - Contains original data from the United States census regarding employment status in 2013
- *employment_status_2014.csv* => data/employment_status_2014.csv
    - Contains original data from the United States census regarding employment status in 2014
- *employment_status_2015.csv* => data/employment_status_2015.csv
    - Contains original data from the United States census regarding employment status in 2015 
- *employment_status_2016.csv* => data/employment_status_2016.csv
    - Contains original data from the United States census regarding employment status in 2016 
- *employment_status_2017.csv* => data/employment_status_2017.csv
    - Contains original data from the United States census regarding employment status in 2017 
- *income_2013.csv* => data/income_og/income_2013.csv
    - Contains original data from the United States census regarding employment status in 2013 
- *income_2014.csv* => data/income_og/income_2014.csv
    - Contains original data from the United States census regarding employment status in 2014 
- *income_2015.csv* => data/income_og/income_2015.csv
    - Contains original data from the United States census regarding employment status in 2015 
- *income_2016.csv* => data/income_og/income_2016.csv
    - Contains original data from the United States census regarding employment status in 2016 
- *income_2017.csv* => data/income_og/income_2017.csv
    - Contains original data from the United States census regarding employment status in 2017 
> **Source:** All original data attained from the [WA data catalog](https://catalog.data.gov/dataset/educational-attainment-of-washington-population-by-age-race-ethnicity-and-puma-region) and the [United States Census Bureau](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2013.S2001)

## Instructions
While we include all the original data, the cleaned and merged data for employment status and median income are included in `data/employment` and `data/income` respectfully. The methods for which we reached these data are additionally included below.

1. Make sure all required files are cloned to your device locally within the same directory (folder)
2. The file `data_analysis.py` contains all of the functions to clean and proces the original data sets and is imported into the other programs as `dp`, running the program will create new files for median incomes and employment by year.
3. Contained within `pages/` are the individual files for the pages of this project's webpage, you do not need to alter these after running `data_analysis.py`. Running `app.py` will start the webpage, to access the webpage ensure that you not stop running `app.py` and follow the link to [our site](http://127.0.0.1:8050/) or paste <http://127.0.0.1:8050/> into your browser.
4. Within the webpage you can navigate to each data visualization by clicking through the pages where you will find blank graphs with manipulatable drop downs where you can select specific filters to view.
5. To run the machine learning model you will need to run `data_analysis.py`, doing so will create and assess models that predict the income and education attainment level based on the input data set `data/income/median_income.csv` respectively.





## Miscellaneous


