    I started by creating a file of dictionaries, one for each language, that stores ten different
values for ten metrics to describe each of the twenty most widely spoken languages in the United
States. Then, we can compare the user's responses to the survey and their previously learned languages
to each of those twenty languages and see which ones are the least different from the user's input.
    Each of the survey questions have values associated with each of the radio buttons (0–10). Higher
numbers represent more of the metric in question. For example, the first metric is Conservative, thus if
the user strongly agrees with a conservative statement, this will translate to a 10. The five responses
for each metric are averaged to give a survey metric, with the naming convention survey_conservative.
These averages are taken for each of the ten metrics. At the end, I take the difference of each of these
survey metrics and each of the language's values for those corresponding metrics. I sum all of these
differences and store them for each of the languages in a dictionary. I then sort the dictionary by the
sum of the differences, selecting the smallest sum of differences to be displayed first as the best
match for the user. I remove all the languages that the user already speaks so that the recommendations
are actually relevant. This is the premise of how I optimize the language selection.
    In this iteration of my project, I decided to not use a database for storing the survey results
since I intend for this to be a tool just for me and my friends. Thus, it doesn't matter that you can't
store your results for a long time and that you will see others' results. If you navigate to Results
prematurely, it will just seem like a preview and not someone else's results or your prior results. If
no one else fills out the survey, it will show your previous results, but if someone else does, you will
see their results before completing the survey yourself. Since this does not affect the accuracy of the
user's results, I was fine with leaving it like this, because upon completing the survey, it will take
you to your personalized results page, and if you want to save the information, you can screenshot it or
memorize it. However, this project is designed to help you decide the next language you should learn,
so once you are finished, there is, to an extent, an expectation for the user to take note of the top
language and go learn it, not necessarily needing to reference it again. This is my rationale for using
the more strightforward method of using a dictionary within application.py instead of using a table
linked to the user. In this vain, registration is not entirely necessary as results are not saved to the
user's account. I figured it was still beneficial for the user's feeling of security to have the login
system, and as an extension of this project, I could later add the survey results to a database so they
remain permanently on the Results page, but again, since that does not distract from the functionality
right now, I didn't worry about it.