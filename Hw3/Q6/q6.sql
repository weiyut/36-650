ALTER TABLE player_bios
	ADD COLUMN Height_in_inches numeric;
	
UPDATE player_bios 
SET Height_in_inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer

ALTER TABLE player_bios
	DROP COLUMN height;
ALTER TABLE player_bios
	RENAME COLUMN Height_in_inches to height;
	
SELECT firstname, lastname, height FROM player_bios ORDER BY id LIMIT 5;

