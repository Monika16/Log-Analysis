# Log-Analysis

## Files in the Project
1. newsdatadb.py - contains SQl Queries in python code.
2. output.doc - contains output of the program.

## Requirement for Execution
1. Python 
2. Virtual machine to run PSQL.
3. Download newsdata.sql.
4. To load data execute `psql -d news -f newsdata.sql`

## Execution
1. Download the project.
2. Place newsdatadb.py in the same folder as newsdata.sql
3. Change directory to the folder where newsdatadb.py is present.
4. Execute by command `python newsdatadb.py` in the command prompt.
5. Review the output.

## Queries written
1. What are the most popular three articles of all time?
   Created `view arview` which gives article title and its no. of views from joining tables articles and log. Join is based on the slug in article and path in log.
2. Who are the most popular article authors of all time?
   Wrote Subquery to find author id and number of views by joining arview and articles based on title. Sum up all the views based on the author's id from authors table and subquery.
3. On which days did more than 1% of requests lead to errors?
   Wrote 2 Subqueries. 1. to find the no. errors  2. to find the total no. of requests on a particular day from the log table. And then found the percentage of failure. Printed the result whose error rate is more than 1%.
