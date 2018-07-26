#!usr/bin/env python

import psycopg2
from datetime import datetime

DBNAME = "news"
"""query to find most popular article author with
total no. of views for the author's articles."""
sql1 = '''
    SELECT authors.name, sum(auid.num) AS VIEWS
    FROM authors
    JOIN
        (SELECT articles.author, arview.num
         FROM articles JOIN arview
         ON articles.title = arview.title)
    AS auid
    ON authors.id = auid.author
    GROUP BY authors.id
    ORDER BY views DESC
'''


"""query to find date
where more than 1% requests lead to error"""
sql2 = '''
    SELECT to_char(date, 'FMMonth DD, YYYY'), round(fail_percent,1) FROM
        (SELECT tottab.dat AS date,
            ((failtab.fail*100.0)/tottab.total)AS fail_percent
        FROM (
            SELECT date(time) AS dat, count(*) AS fail
            FROM log
            WHERE status!='200 OK'
            GROUP BY date(time))
            AS failtab
            RIGHT JOIN (
                SELECT date(time)AS dat, count(*) AS total
                FROM log
                GROUP BY date(time))
                AS tottab
                ON failtab.dat = tottab.dat
            ORDER BY failtab.dat)
        AS percent_failure
    WHERE fail_percent > 1.0
'''


def printresults(result):
    """method to print the results in a fomatted form"""
    for row in result:
        title = row[0]
        views = row[1]
        print('{} - {} views'.format(title, views))
    return


def db_connect():
    """Establish database connection with database news
        and cursor for database.
       Returns:
            Cursor c """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    return db, c


def execute_query(query):
    """To execute given query
       Returns:
            results of the query"""
    db, c = db_connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_top_articles():
    """Prints top 3 articles"""
    query = "SELECT * FROM arview LIMIT 3"
    results = execute_query(query)
    print("\nThree most popular articles:")
    printresults(results)


def print_top_authors():
    """to find the most popular author"""
    query = sql1
    results = execute_query(query)
    print("\nMost popular article authors:")
    printresults(results)


def print_errors_over_one():
    """days on which more than 1% requests lead to error"""
    query = sql2
    results = execute_query(query)
    print("\nDays when more than 1% requests lead to error: ")
    for row in results:
        date = row[0]
        error = row[1]
        print(str(date)+' - '+str(error)+'% errors')


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()
    print('')
