CREATE TABLE  new_table(
	player integer REFERENCES more_player_stats,
	prl numeric,
	position text
);

INSERT INTO new_table (player, prl)
(SELECT id, ROUND(per - 67*va/(gp*minutes),1) FROM more_player_stats);

UPDATE new_table
SET position = 
	CASE 
		WHEN prl >= 11.3 THEN 'PF'
		WHEN prl<11.3 ANd prl>=10.8 THEN 'PG'
		WHEN prl<10.8 ANd prl>=10.6 THEN 'C'
		WHEN prl<10.6 ANd prl>=0 THEN 'SG/SF'
	END;
	
	
SELECT * FROM new_table LIMIT 10;


