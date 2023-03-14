import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    dcc.Markdown('''
    # Introduction

    For our project, we decided to explore education attainment level in
    Washington state and demographics that may relate to it or cause the
    levels to be how they are. Our team members are Ken Oh, Allison Ho,
    and Willis Liang.
    ''', className='markdown home'),
    dcc.Markdown('''
    # Research Questions

    1. Is there large disparity between any of the levels of education
    attained? Between which degrees? What could be causing this disparity?

    2. How has education attainment level changed over time? Are there any
    factors that are contributing to this pattern? If so, what?

    3. Is there any correlation between educational attainment and the
    unemployment rate in the 5 years interval 2013-2017? Especially does having
    higher educational attainment result in lower unemployment rate?
    ''', className='markdown home'),
    dcc.Markdown('''
    # Motivation

    We are interested in the educational attainment of the PUMA region because
    it is a critical factor for decision making in education policy and
    demonstrates the presence or lack of equity within a given community.
    Studying education data can provide critical insights to the development
    of future strategies and plans to address educational inequity and biases.
    In addition, data regarding levels of educational attainment can provide
    critical information showing flaws and benefits of education programs
    currently in place. Being students im Washington, we are interested in
    analyzing and predicting trends in educational achievment across groups as
    well as considering implmentations to improve education for groups with
    less documented and recorded data.

    ''', className='markdown home'),
    dcc.Markdown('''
    # Datasets

    The main data set that we chose to base our analysis on is data on the
    education level attained by different categories of ages, races, and PUMA
    regions; from 2013 to 2017 in Washington state. Each row within the dataset
    contains a column called "Population Estimate (Count)" which tells us the
    total number of people for that group that attained a specfic level of
    education. The additional datasets that we used were source data from
    government censuses regarding income and employment status trends within
    different counties in Washington from 2013 to 2017.

    ## Education Attainment Levels:
    * [Education Dataset](https://catalog.data.gov/dataset/educational-attainment-of-washington-population-by-age-race-ethnicity-and-puma-region)
    * [Education CSV Download](https://www.google.com/url?q=https://data.wa.gov/api/views/aqa5-4cee/rows.csv?accessType%3DDOWNLOAD&sa=D&source=docs&ust=1678775997628088&usg=AOvVaw3MRyV5L7ZrWBe4oxPP7SIN)

    ## Median Income:
    * [Median Income WA Counties 2013](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2013.S2001)
    * [Median Income WA Counties 2014](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2014.S2001)
    * [Median Income WA Counties 2015](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2015.S2001)
    * [Median Income WA Counties 2016](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2016.S2001)
    * [Median Income WA Counties 2017](https://data.census.gov/table?q=median+income&t=Earnings+(Individuals)&g=0400000US53,53$7950000&tid=ACSST1Y2017.S2001)

    ## Employment Status:
    * [Employment Status WA Counties 2013](https://data.census.gov/table?q=employment+status&g=0400000US53$7950000&tid=ACSST1Y2013.S2301)
    * [Employment Status WA Counties 2014](https://data.census.gov/table?q=employment+status&g=0400000US53$7950000&tid=ACSST1Y2014.S2301)
    * [Employment Status WA Counties 2015](https://data.census.gov/table?q=employment+status&g=0400000US53$7950000&tid=ACSST1Y2015.S2301)
    * [Employment Status WA Counties 2016](https://data.census.gov/table?q=employment+status&g=0400000US53$7950000&tid=ACSST1Y2016.S2301)
    * [Employment Status WA Counties 2017](https://data.census.gov/table?q=employment+status&g=0400000US53$7950000&tid=ACSST1Y2017.S2301)

    ''', className='markdown home')
], className='home-div')
