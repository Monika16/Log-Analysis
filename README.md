# Log-Analysis

## Files in the Project
1. newsdatadb.py - contains SQl Queries in python code.
2. output.doc - contains output of the program.

## Queries written
1. What are the most popular three articles of all time?
   Created `view arview` which gives article title and its no. of views from joining tables articles and log. Join is based on the slug in article and path in log.
2. Who are the most popular article authors of all time?
   Wrote Subquery to find author id and number of views by joining arview and articles based on title. # Log-Analysis