
'''

headlines = ["Papperbok Review: Totally Triffic", "Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away"
             ]

news_ticker = ""
#ticker_space = " "
for headline in headlines:
    
    if len(news_ticker) + len(headline) >= 140:
        news_ticker = news_ticker + headline[:140-len(news_ticker)]
        break
    else:
        news_ticker+= headline+" "


print news_ticker

print len(news_ticker)



my_answers = [1,2,3,4,5]
answers = [1,2,3,4,5]

def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    """
    results= [None, None, None, None, None]
    index = 0
    while index<len(answers):  #this loop compares my answer to the correct answer
        if my_answers[index] == answers[index]:
            results[index] = True
            index+=1
            
        else:
            results[index] = False
            index+=1
    print(results)        
    return results  #this output is used as input by the function below

def count_calculator(results):   #this function uses results as input and outputs test score.
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

'''
        
#dictio = {'breakfast': 'oatmeal', 'lunch': 'chipotle', 'dinner': 'sandwich'}

def most_prolific(some_dict):
    new_dict = {}
    some_list = []
    for album in some_dict:
        some_list.append(some_dict[album])
    for year in some_list:
        new_dict.append(some_list.count(year))
    for year, key in new_dict.iteritems():
        if max(new_dict.values()) == some_list.count(year):
            return year



'''
 https://discussions.udacity.com/t/data-analysis-final-project/305093/16

 https://discussions.udacity.com/t/those-that-survived/308367/2

 https://discussions.udacity.com/t/searching-for-missing-passengers-titanic-data/304928/2

 https://discussions.udacity.com/t/problems-with-adding-values-that-have-already-been-grouped-considering-different-column/290014/2

 https://discussions.udacity.com/t/project-graph-question/238096/11

 https://discussions.udacity.com/t/titanic-data-wrangling-help/224927/6

 https://discussions.udacity.com/t/cleaning-titanic-data/212418/5

 https://discussions.udacity.com/t/titanic-dataset-missing-observations/174708/2



'''
