import urllib2
import json
import math
import re
import sys
import imp
import sendgrid
import mysql.connector
reload(sys)
sys.setdefaultencoding('utf-8')
filenameAFINN = '/Users/mayurjain/Documents/AFINN/AFINN-111.txt'
afinn = dict(map(lambda (w, s): (w, int(s)), [ws.strip().split('\t') for ws in open(filenameAFINN)]))
pattern_split = re.compile(r"\W+")
Connection = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='Zomato')
global cursor
cursor = Connection.cursor()
cursor.execute("USE Zomato")
global InsertIntoSQL
def InsertIntoSQL(pyline):
    sql = "INSERT INTO ZomatoFeedback(PythonLine) VALUES('"+str(pyline)+"')"
    numbers_of_rows = cursor.execute(sql)

class ZomatoReview(object):
    InsertIntoSQL('Declaring Global Function')
    global zomato_review
    global review_list
    global zomato_ratings
    global zomato_ratings_text
    global sendMail
    global sentiment
    InsertIntoSQL('global zomato_review()')
    InsertIntoSQL('global review_list()')
    InsertIntoSQL('global zomato_ratings()')
    InsertIntoSQL('global zomato_ratings_text()')
    InsertIntoSQL('global sendMail()')
    InsertIntoSQL('global sentiment()')
    #status_rating_review = [] * 5
    #status_rating_text_review = [] * 5
    def zomato_review(res_id):
        #api_key = '9da6a6b0c48bf3929eca72380659bfb5'
        InsertIntoSQL('Assign Zomato Developer URL in Function zomato_review()')
        Zomato_url = 'https://developers.zomato.com/api/v2.1/reviews?res_id='+str(res_id)
        InsertIntoSQL('Assign Zomato URL Header with API KEY in Function zomato_review()')
        headers = {'user-key':'9da6a6b0c48bf3929eca72380659bfb5','Accept':'application/json'}
        InsertIntoSQL('Assign Zomato URL with Header to Form Request Url in zomato_review()')
        request = urllib2.Request(Zomato_url,None,headers)
        InsertIntoSQL('Assign request urls response')
        response = urllib2.urlopen(request)
        InsertIntoSQL('Convert response into Json Format')
        review_data = json.load(response)
        InsertIntoSQL('Declaring List of Json Parameters')
        rating = [] * 5
        review_text = [] * 5
        rating_color = [] * 5
        rating_text = [] * 5
        name = [] * 5
        profile_url = [] * 5
        InsertIntoSQL('rating, review_text, rating_text, rating_color')
        InsertIntoSQL('Iterating through for loop to fetch each Json Object value and Store it in the list declared previously')
        for userreview in review_data['user_reviews']:
            for review in userreview:
                #print userreview[review]['rating']
                #print userreview[review]['rating_color']
                #print userreview[review]['review_text']
                #print userreview[review]['rating_text']
                rating.append(userreview[review]['rating'])
                review_text.append(userreview[review]['review_text'])
                rating_color.append(userreview[review]['rating_color'])
                rating_text.append(userreview[review]['rating_text'])
                name.append(userreview[review]['user']['name'])
                profile_url.append(userreview[review]['user']['profile_url'])
        #print rating
        #print review_text
        #print rating_color
        #print rating_text
        #res_id = 16774318,18387851
        global name
        global profile_url
        return rating, review_text, rating_text, rating_color
    InsertIntoSQL('Assigning the Restaurant ID and Calling the function zomato_review()')
    review_list = zomato_review(16774318)
    InsertIntoSQL('Defining the function zomato_ratings()')
    def zomato_ratings(r):
        #r = int(r)
        InsertIntoSQL('Based on the Json Value for the element - rating, review is assigned')
        if (r <= 2.5):
            bR = 'Bad Review'
            return bR
        elif (r > 2.5 and r < 3.5):
            nR = 'Neutral Review'
            return nR
        elif (r >= 3.5 and r <= 5):
            gR = 'Good Review'
            return gR
        else:
            nRA = 'No Review Available'
            return nRA
    InsertIntoSQL('Defining the function zomato_ratings()')
    def zomato_ratings_text(text_rating):
        text_rating = float(text_rating)
        InsertIntoSQL('Based on the Json Value for the element - rating_text, review is assigned')
        if text_rating < 0.00:
            bR = 'Bad Review'
            return bR
        elif text_rating == 0.00:
            nR = 'Neutral Review'
            return nR
        elif text_rating > 0.00:
            gR = 'Good Review'
            return gR
        else:
            nRA = 'No Review Available'
            return nRA
    def sentiment(text):
        words = pattern_split.split(text.lower())
        sentiments = map(lambda word: afinn.get(word, 0), words)
        if sentiments:
            sentiment = float(sum(sentiments))/math.sqrt(len(sentiments))
        else:
            sentiment = 0
        return sentiment
        InsertIntoSQL('Defining the function reviewed rating, we assign a text based on rating and making it global for comparsion with the text fetched from text_rating')
    def reviewed_rating(self):
        #review_list = zomato_review(16774318)
        #for rating, review_text, rating_text, rating_color in review_list.iteritems():
        #for rating, review_text, rating_text, rating_color in zip(review_list):
        #rating, review_text, rating_text, rating_color = review_list
        rating, review_text, rating_text, rating_color = review_list
        status_rating_review = [] * 5
        ratingValue = [] * 5
        #for r, ra_t in zip(rating, rating_text):
        for r in rating:
            #if __name__ == '__main__':
            #print(zomato_ratings(r),r)#,"%6.2f %s" % (sentiment(ra_t), ra_t)
            ratingValue.append(r)
            status_rating_review.append(zomato_ratings(r))
            #print("%6.2f %s" % (sentiment(ra_t), ra_t))
        global status_rating_review
        global ratingValue
        InsertIntoSQL('Defining the function reviewed rating text, we assign a text based on rating value of sentiment text and making it global for comparsion with the text fetched from rating')
    def reviewed_rating_text(self):
        #review_list = zomato_review(16774318)
        status_rating_text_review = [] * 5
        sentimentValue = [] * 5
        rating, review_text, rating_text, rating_color = review_list
        for ra_t in rating_text:
            #print("%6.2f %s" % (sentiment(ra_t), ra_t))
            text_rating = "%6.2f" % sentiment(ra_t)
            #print(text_rating)
            #print(zomato_ratings_text("%6.2f %s" % (sentiment(ra_t))))
            #print(zomato_ratings_text(text_rating))
            sentimentValue.append(text_rating)
            status_rating_text_review.append(zomato_ratings_text(text_rating))
        global status_rating_text_review
        global sentimentValue
        InsertIntoSQL('Defining the Sentiment function')
        InsertIntoSQL('Passing a sentiment text through the function sentiment')
        InsertIntoSQL('Split the text with words and assigning the value for each word from -5 to +5')
        InsertIntoSQL('assiging value to word is done by affin.txt where the word is compared assigns itself a value.')
    def sendMail():
        InsertIntoSQL('Defining the Function sendMail, Assiging the API Key to Variable')
        InsertIntoSQL('Using the Inbuilt attributes, to store Mail ID of To and From of user.')
        sg = sendgrid.SendGridAPIClient(apikey='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')
        userName = 'User Name '
        profileurl = 'Profile Url of the User '
        data = {
        "personalizations": [
            {
            "to": [
                {
                    "email": "mayurachennaiite@gmail.com"
                }
            ],
            "subject": "NEGATIVE FEEDBACK DETECTED!"
            }
        ],
        "from": {
            "email": "mayur87545@gmail.com"
        },
        "content": [
            {
            "type": "text/plain",
            "value": "Hello, Please find the negative review received from the user !"
            }
            #{
             #"type": "text/plain",
             #"value": "Please find the negative review received from the user !"
            #}
        ]
        }
        response = sg.client.mail.send.post(request_body=data)
        print(str(response.status_code)+' Mail Sent Successfully')
    def final_review(self):
        InsertIntoSQL('Defining the Function Final_review,')
        InsertIntoSQL('Here, we compare the text assigned to Sentiment Value and Rating Value')
        InsertIntoSQL('When the compared text matches for the -Bad Review mail is sent- or else we just print the statement as NO Negative Reviews')
        count = 0
        for zR,zRT in zip(status_rating_review,status_rating_text_review):
            if(zR == 'Bad Review' and zRT == 'Bad Review'):
                Print(zR)
                sendMail()
                print('User Name '+str(name[count])+' with profile Url '+profile_url[count])
                print('The Rating Text is '+str(rating_text[count]))
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count])+' of the '+zR)
                count += 1
            elif(zR == 'Bad Review' and zRT == 'Neutral Review'):
                print(zR)
                sendMail()
                print('User Name '+str(name[count])+' with profile Url '+profile_url[count])
                #print('The Rating Text is '+str(rating_text[count]))
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count])+' of the '+zR)
                count +=1
            elif(zR == 'Bad Review' and zRT == 'Good Review'):
                Print(zR)
                sendMail()
                print('User Name '+str(name[count])+' with profile Url '+profile_url[count])
                #print('The Rating Text is '+str(rating_text[count]))
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count])+' of the '+zR)
                count +=1
            elif(zR == 'Neutral Review' and zRT == 'Bad Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            elif(zR == 'Neutral Review' and zRT == 'Neutral Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            elif(zR == 'Neutral Review' and zRT == 'Good Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            elif(zR == 'Good Review' and zRT == 'Bad Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            elif(zR == 'Good Review' and zRT == 'Neutral Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            elif(zR == 'Good Review' and zRT == 'Good Review'):
                print('The Rating System Review is '+str(ratingValue[count])+' & Sentiment Value is '+str(sentimentValue[count]))
                #print('The Rating Text is '+str(rating_text[count]))
                count +=1
            else:
                count +=1
                print('No Negative Feedback')

zoma = ZomatoReview()
zoma.reviewed_rating_text()
zoma.reviewed_rating()
zoma.final_review()
Connection.commit()
Connection.close()
