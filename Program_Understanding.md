## Understanding Logic 

#### Using Zomato API, Fetching all json objects related to Reviews and store into a List.
      Json Object for Reviews:
        > rating
        > review text
        > review color
        > rating text

#### Based On Rating 
       In our program, we are using rating and rating text for analysis.
       Rating is similar to rating color as
       each color is assigned a value 
            Rating    Rating Color
               1        Dark Red
              1.5       Light Red
              ...         ....

               5        Dark Green
       
       We are categorizing the review based on rating as
          
          > Bad Review
          > Neutral Review
          > Good Review
       
       if rating <= 2.5 then Bad Review
       if rating > 2.5 and rating <= 3.5 then Neutral Review
       if rating > 3.5 and rating <= 5 then Good Review

#### Based on Rating Text        
       Rating Text is a complicated process factor to analyse.We are using AFFIN.txt for analysing the review.
       Min value of word is -5
       Max value of word is +5
   
   AFFIN.txt
   
        abandoned	-2
        abandons	-2
        abhor	-3
        abhorred	-3
        abhorrent	-3
        abilities	2
        ability	2
        aboard	1
        absentee	-1
        absentees	-1

       So each word is assigned a value based on meaning and with review as context of the word
       
       review text : abhor ability 
       then we can calculate the sentiment value as "-3+2/sqrt(2)", 2 inside sqrt because 2 words
       
       We are categorizing the review based on rating text as follows
          
          > Bad Review
          > Neutral Review
          > Good Review
       
       if rating text < 0 then Bad Review
       if rating text == 0 then Neutral Review
       if rating text > 0 then Good Review

       We are scaling down the value of -5 to +5 as -2.5 to +2.5
       At last, We'll compare rating and rating text, then arrive at a Breakpoint to make review Bad or not.
      
 #### Sending Mail
 
      A Alert in the form of a MAIL is triggered incase of bad review.
      
      > Star Based Rating is prefered over Review comments when a decision is taken to make a review
     BAD or NEUTRAL or GOOD
      > We compare the "Text" assigned by us to the RATING and RATING Text in the form 'Bad Review','Neutral Review','Good Review'
      > We'll trigger mail based on the output as follows
      > BR - BAD REVIEW | NR - NEUTRAL REVIEW | GR - GOOD REVIEW
      
            RATING            RATING TEXT
              BR                   BR
              BR                   NR
              BR                   GR
              ..                   ..
              
              ..                   .. 
              GR                   GR 
      
      > For (BR,BR),(BR,NR),(BR,GR),(NR,BR),(NR,NR) review, We'll trigger mail as we are giving priority to "STAR RATING" !
      
      
     
 
 ## Note: Zomato API allows only latest 5 or less than 5 reviews for a restaurant at time.
       
