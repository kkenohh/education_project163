import dash
from dash import html, dcc

dash.register_page(__name__, name='Final Thoughts')

layout = html.Div(children=[
    dcc.Markdown('''
    # Conclusion

    ## Q1 Disparities Between Degrees:
    For this question, we dicided to make a chart that showed thedifferent
    number of people who attained each degree. We found that the most
    commonly attained degree was "less than high school" which was surprising
    since we did not expect the majority of populations to not even graduate
    from high school.

    ## Q2 Education Attainment Over Time:
    For this question, we looked for correlations between median income
    of a region, and the number of people who attained less than a high school
    degree. Using an interactive plot, we were able to statistically
    and empirically conclude that from 2013 to 2017, the population of people
    who attained a minimum high school education was not significantly impacted
    by the median income of a given region.

    ## Q6 Highest Ratio of People in Labor Force:
    Looking at the graph we created, we found that the number of people with
    "less than high school" had the lowest amount of people in the labor force
    from 2013 to 2017. We predicted that this was due to those groups of people
    wanting to continue to pursue school or just being too young to be in the
    workforce.

    ## Final Words:

    While performing our analysism we were considering the possible impacts of
    our results. We wanted to provide meaning analysis that would be beneficial
    in educational and social reform. For example, a political party that may
    want to change budgets alloted for education may come across our analysis
    and use it to help justify or refute his/her decision. After performing our
    analysis, we found that while we originally intended to reinforce equity,
    we may have unintentionally reinforced the inherent biases present within
    the datasets we found. Our analysis could have possibly further reinforced
    the stereotypes and targeted specific racial and social groups which would
    be incredibly discouraging for young children aspiring to grow into the
    generation of working adults. While we may have had the focus and intent of
    advocating educational equity, in the end it is still important to be
    careful with data as well as solutions towards problems that our analysis
    of PUMA regions, education levels, and income levels may have shown.

    ''', className='markdown home'),
    dcc.Markdown('''
    # Machine Learning Results

    For our third and fourth research questions regarding predicting a person's
    median income and education we attempted to use sklearn's machine learning
    DecisionTreeRegressor and DecisionTreeClassifier models to answer these two
    questions.

    ## Question 3 Predicting Median Income Based on Education Attainment Level:
    * To answer this questionn, we used DecisionTreeRegressor to build a
    regression model that predicted a person's income based on their education
    level. Our independent variables (features) were educational attainment
    regions (PUMA regions in Washington State) and our dependent variable
    (label) was the median income. The model gave us a 0.0 mean squared error
    for our training set, however it gave use a 16316183.46 mean squared error
    for our testing set. As a result, we concluded that our model was
    significantly overfitting to the training set, possibly a result of the
    size of our data set being relatively small. Additionally, we only had
    aggregating/summarizing data which cannot provide detailed enough
    inforation for our model to learn effectively with.

    ## Question 4 Predicting an Education Level Based on Their Median Income:
    * To answer this question, we used DecisionTreeClassifier to construct a
    model that predicted a person's education level based on their median
    income as well as PUMA region. Our independent variables (features) were
    median incom and PUMA regions within Washington State; where our dependent
    variable (label) was the educational attainment level. The model produced
    an accuracy score of 1.0 for our training set and an accuracy score of 0.65
    for our test set. Based on the accuracy scores above, we found concluded
    that our model was quite accurate and could be used to predict a person's
    educational attainment level.
    ''', className='markdown home')
], className='home-div')
