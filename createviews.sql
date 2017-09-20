create view author_slug as
        select authors.name, articles.slug
        from articles, authors
        where articles.author = authors.id;
        
create view error_view as
        select count(*)::numeric as num, time::date as day
        from log
        where status != '200 OK'
        group by day
        order by day desc;
        
create view total_view as
        select count(*)::numeric as num, time::date as day
        from log
        group by day;