CREATE VIEW arview AS 
SELECT articles.title, count(*) AS num
FROM articles JOIN log 
ON '/article/'|| articles.slug = log.path
GROUP BY articles.title
ORDER BY num DESC;