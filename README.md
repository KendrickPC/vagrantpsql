##### September 20th, 2017:

# Logs Analysis Project 
  This project uses python3 to interact with a PostgreSQL database containing information from a newspaper site. The Python3 module document entitled: newsdb7.py. newsdb7.py python code used as a reporting tool to answer the following questions: 
  
  1. What are the top three (3) news articles in the database? 
  2. Who are the most popular authors in the news database?
  3. On what days were there more than 1% error in the news database? 

### Before You Run the Program:
  Before we run the program , we must install a few programs. 
  1. Download install Python version 3 from the following website: 
       https://www.python.org/downloads/
        * Make sure you install Python version 3+ * 
  2. Download and install Virtual Box from the following website: 
       https://www.virtualbox.org/
        * You do not need to open this program after downloading and installing * 
  3. Download and install Vagrant from the following website: 
       https://www.vagrantup.com/downloads.html
  4. Download the data files for the news database from the following location: 
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
        * Unzip the newsdata.zip file. * 
  5. Place the newsdata.sql file into the vagrantpsql folder (the folder downloaded from the following github repository link: https://www.google.com)
        * Your vagrantpsql folder should now contain the following files: 
            - vagrantfile
            - newsdb7.py
            - createviews.sql
            - newsdata.sql
            - README.md
            
### Initial setup of the virtual machine
  6. Now we will attempt to run the virtual machine by opening up your terminal program. CD into the downloaded vagrantpsql folder (with the newsdata.sql file that you manually moved over)
  7. After your terminal window is CD into the vagrantpsql folder, run the terminal command 'vagrant up'. 
      * The 'vagrant up' command may take more than five minutes to install so be patient * 
  8. Next, run the terminal command 'vagrant ssh'
  9. cd into your vagrant file by literally typing in 'CD vagrant'
  10. Next, in your terminal program, type 'ls' to get a list view of files in your vagrantpsql folder. The previous listed five (5) files should show up. 
  11. For an initial install, run the command 'psql -d news -f createviews.sql'
  12. Finally, run my custom python code with the following terminal command 'python3 newsdb7.py'
  
### Run the logs analysis reporting tool
    1. CD into the vagrantpsql folder. 
    2. run vagrant up
    3. run vagrant ssh
    4. cd /vagrant 
    5. python3 newsdb7.py
    
The terminal window should print the following results: 


The top three news articles in the database are as follows:

"Candidate Is Jerk, Alleges Rival" = 338,647 views
"Bears Love Berries, Alleges Bear" = 253,801 views
"Bad Things Gone, Say Good People" = 170,098 views

-----------------------------------


The top authors in the news database are as follows:

Ursula La Multa: 507,594views
Rudolf von Treppenwitz: 423,457views
Anonymous Contributor: 170,098views
Markoff Chaney: 84,557views

-----------------------------------


Days in which 404 errors accounted for >1% of requests:

2016-07-17: 2.26%



-----------------------------------