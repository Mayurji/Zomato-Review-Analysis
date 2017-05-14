# Zomato-Review-Analysis
Assuming as a working employee of Restaurant registered in Zomato, Employee should be able to receive the alert in form of a Mail when a Negative Feedback is written in Zomato!

## Tools:
  
  > **Python Shell**
  
  > **Mysql Database**
  
  > **Sendgrid**
  
  > **Affin.txt**
  
  > **Zomato Valid API Key And Access to zomato**
  
## Tools Explanation:
  
  #### **Python Shell:** 
       To write and execute python programs.
  #### **Mysql Database:**
       To store the logs to passed from the python program.
  #### **Sendgrid:** 
       To send mail to receipt whenever a negative feedback is generated.
  #### **Affin.txt:** 
       To compare the text review from zomato and assign a sentiment value to the review text.
  #### **Zomato API:** 
       To fetch the ratings and review text for analysis.
       ref: https://developers.zomato.com/

## Set Up:

  ### **MAC**
  #### Python shell:
       Open Terminal -> type 'python' -> Python Shell opens
  #### Mysql Database:
       Open New Terminal -> Start Mysql Server -> Switch to root or new user 
       -> Create Database Zomato
       -> use Zomato
       -> Create Table ZomatoFeedback(PythonLine VARCHAR(500))
  #### Sendgrid:
       Register Sendgrid -> Generate Sendgrid API Key
       Install Pip(Python Package Index) -> Using pip install sendgrid
  #### Zomato API:
       Register in Zomato Developers -> Generate API KEY

## Commands:
  
  ### To Start Mysql Server:
       cmd: /usr/local/mysql/support-files/mysql.server start
       switch to user: mysql -u root
  ### To install pip and sendgrid:
       cmd: sudo easy_install pip
       cmd: pip install sendgrid
       
       
              
       
