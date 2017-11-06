#!/usr/bin/env python


# https://wiki.postgresql.org/wiki/Using_psycopg2_with_PostgreSQL
# we import sys for the sys exit(1) code
import psycopg2
import sys

DB_NAME = 'news'


# The following code is written to check if the PostgreSQL database
# is connected properly. If not, there will be a custom error message.
def connect():
    try:
        connection = psycopg2.connect(database=DB_NAME)
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
            print("Error with connection to the PostgreSQL database"
                  "as defined by newsdb7.py function connect in line #33")
            sys.exit(1)


# My runTheSearch function will return the results of the three main
# questions. In this specific instance, it will answer
# questions 1, 2, and 3.
def runTheSearch(questionsFromBoss):
    connection, cursor = connect()
    cursor.execute(questionsFromBoss)
    results = cursor.fetchall()
    connection.close()
    return results


# Question #1: Proposes to answer the question regarding
# "the top three views articles in the news database."
def topThreeArticlesInNewsDatabase():
    results = runTheSearch(
        """select articles.title, count(log.path)
        from articles, log
        where log.path = '/article/' || articles.slug
          and log.status = '200 OK'
        group by articles.title
        order by count(log.path) desc limit 3;"""
    )
    print('\n\n' + "The top three news articles in the database"
          "are as follows:" + '\n')
    for item in results:
        print("\"" + item[0].title() + "\" = " +
              str("{:,}".format(item[1])) + "views")


# Question #2: Proposes to answer the question concerning "the most popular
# authors in the news database" fetched from the total views of each
# news article.
def mostPopularAuthorsInNewsDatabase():
    results = runTheSearch(
        """select author_slug.name, count(log.path)
        from author_slug, log
        where log.path = '/article/'  || author_slug.slug
            and log.status = '200 OK'
        group by author_slug.name
        order by count(log.path) desc;"""
    )
    print('\n\n' + "The top authors in the news"
          "database are as follows:" + '\n')
    for item in results:
        print(item[0] + ": " + str("{:,}".format(item[1])) + "views")


# Question #3: Proposes to answer the question of days with more
# than 1% of 404 error_days
def error_days():
    results = runTheSearch(
        """select total_view.day, (error_view.num/total_view.num)*100 as pct
        from total_view
        join error_view on total_view.day=error_view.day
        where (error_view.num/total_view.num)*100 > 1;"""
        )
    print('\n\n' + "Days in which 404 errors accounted for >1% of "
               "requests:" + '\n')
for errday, errpercent in results:
    print(str(errday) + ": " + str(round(errpercent, 2)) + "%")
    print('\n')

if __name__ == "__main__":
    print('\n' + "")
    topThreeArticlesInNewsDatabase()
    print('\n' + "-----------------------------------")
    mostPopularAuthorsInNewsDatabase()
    print('\n' + "-----------------------------------")
    error_days()
    print('\n' + "-----------------------------------")
