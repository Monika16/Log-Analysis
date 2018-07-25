# Log-Analysis

## Description of Project
  Python script uses psycopg2 to query a mock PostgreSQL database for a news website. 
  `news` Database is structured as:
  	It has 3 tables
  	1. articles: Columns:
  		1. author - it is author id and a foreign key.
  		2. title - title of article
  		3. slug - short name of an article
  		4. lead - opening paragraph of an article
  		5. body - full description of article
  		6. time - timestamp of article
  		7. id - primary key, unique id for an article.
  	2. authors: Columns:
  		1. name - name of author
  		2. bio - biodata of author
  		3. id - author id of the author, primary key
  	3. log: Columns:
  		1. path - path to the article
  		2. ip - ip address of the computer
  		3. method - method used to retrieve data
  		4. status - html status code
  		5. time - timestamp when the article was viewed
  		6. id - primary key represents id for each log
  Python script answers 3 queries.
  	1. What are the most popular three articles of all time? 
  	2. Who are the most popular article authors of all time?
  	3. On which days did more than 1% of requests lead to errors?

## Files in the Project
1. newsdatadb.py - contains SQL Queries in python code.
2. create_views.sql - contains SQL Query to create View.
3. output.txt - contains output of the program.

## Requirement for Execution
1. Python 2
2. Virtual machine to run PSQL. 
	Install Virtual Machine - https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0
	This will give PostgreSQL support.
	To get virtual machine online - `vagrant up`
	Log in to it with - `vagrant ssh`
3. Download newsdata.zip - https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
   Unzip the folder to find newsdata.sql file.
4. To load data execute `psql -d news -f newsdata.sql`

## Execution
1. Download the project.
2. in Terminal, change directory to the folder where newsdatadb.py is present.
3. Execute `psql -d news -f create_views.sql` command to create view arview.
4. Execute by command `python newsdatadb.py` in the command prompt.
5. Review the output.

## Queries written
1. What are the most popular three articles of all time?

   Created `view arview` which gives article title and its no. of views from joining tables articles and log. Join is based on the slug in article and path in log.
   
2. Who are the most popular article authors of all time?

   Wrote Subquery to find author id and number of views by joining arview and articles based on title. Sum up all the views based on the author's id from authors table and subquery.
   
3. On which days did more than 1% of requests lead to errors?

   Wrote 2 Subqueries. 1. to find the no. errors  2. to find the total no. of requests on a particular day from the log table. And then found the percentage of failure. Printed the result whose error rate is more than 1%.
