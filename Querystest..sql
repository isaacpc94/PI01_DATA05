use video;
#Primera Query
 select d.title,d.release_year,d.Plataforma,d.type,d.duration,convert(SUBSTRING_INDEX(d.duration,' ', 1), UNSIGNED INTEGER) AS durnum from 
 (select a.IdPlataforma,a.Plataforma,b.duration,c.release_year,c.type,c.title from
 idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)
 join video c on (binary b.IdVideo=binary c.IdVideo)
 ) d where d.type='Movie' and d.Plataforma='hulu' and d.release_year=2018 
order by 6 desc
limit 1;

#Segunda Query
select a.Plataforma,c.type,count(*) from
 idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)
 join video c on (binary b.IdVideo=binary c.IdVideo)
 where a.Plataforma='netflix'
 group by 2 order by 2;
 
 #Tercera Query
 select a.Plataforma,c.listed_in,count(*) from
 idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)
 join (select * from listed 
 where listed_in like 'comed%') c on (b.IdPlataforma= c.IdPlataforma and (binary b.IdVideo= binary c.IdVideo) )
 group by 1
 order by 3 desc
 limit 1;
 
 #Cuarta Query
 select a.Plataforma,d.cast,b.IdVideo,c.release_year,count(*) as cantidad from
 idplataforma a join plataforma b on (a.IdPlataforma=b.IdPlataforma)
 join video c on (binary b.IdVideo=binary c.IdVideo)
 join cast d on (binary c.IdVideo=binary d.IdVideo)
 where a.Plataforma='netflix' and c.release_year=2018
 group by d.cast
 having cast !=''
 order by 5 desc
 limit 1;