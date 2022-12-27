LOAD DATA LOCAL INFILE 
'/Users/krc/Desktop/FIFA_Project_Personal/modeling/data/query_table/player_season_stats_ICON.csv'
INTO TABLE ICON_stats
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
