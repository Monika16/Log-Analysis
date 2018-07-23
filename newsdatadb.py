import psycopg2
from datetime import datetime

DBNAME = "news"

# view to find articles with its no. of views
sql = '''
    create view arview as 
    select articles.title, count(*) as num
    from articles join log 
    on articles.slug = substring(log.path from 10)
    group by articles.title
    order by num desc
'''

# query to find most popular article author with 
#    total no. of views for the author's articles.
sql1 = '''
    select authors.name, sum(auid.num) as views from authors join
    (select articles.author, arview.num
    from articles join arview
    on articles.title = arview.title) as auid 
    on authors.id = auid.author
    group by authors.id
    order by views desc
'''

# query to find date 
# where more than 1% requests lead to error
sql2 = '''
    select date, round(fail_percent,1) from
    (select tottab.dat as date, 
     ((failtab.fail*100.0)/tottab.total)as fail_percent from
    (select date(time) as dat, count(*) as fail from log 
     where status!='200 OK' group by date(time))as failtab right join
    (select date(time)as dat, count(*) as total 
     from log group by date(time))as tottab
    on failtab.dat = tottab.dat 
    order by failtab.dat)as percent_failure
    where fail_percent > 1.0;
'''

# method to print the results in a fomatted form


def printresults(result):
    for row in result:
        title = row[0]
        views = row[1]
        print(str(title)+' - '+str(views)+' views')
    return

# establish database connection
db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# to create view
c.execute(sql)
# to find three most popular articles with the no.of views
c.execute("select * from arview limit 3")
results = c.fetchall()
print("\nThree most popular articles:")
printresults(results)

# to find the most popular author
c.execute(sql1)
results = c.fetchall()
print("\nMost popular article authors:")
printresults(results)

# days on which more than 1% requests lead to error
c.execute(sql2)
results = c.fetchall()
print("\nDays when more than 1% requests lead to error: ")
for row in results:
    date = row[0]
    error = row[1]
    print(datetime.strftime(date, '%B %d,%Y')+' - '+str(error)+'% errors')
print('')
db.close()
