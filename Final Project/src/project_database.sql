create schema fifa;

create table fifa.players_20 (
	sofifa_id text,
	player_url text,
	short_name text,
	long_name text,
	age int check(age >0),
	dob date,
	height_cm numeric check(height_cm >0),
	weight_kg numeric check(weight_kg >0),
	nationality text,
	club text,
	overall numeric,
	potential numeric,
	value_eur numeric,
	wage_eur numeric,
	player_positions text,
	preferred_foot text,
	international_reputation numeric,
	weak_foot numeric,
	skill_moves numeric,
	work_rate text,
	body_type text,
	real_face text,
	release_clause_eur numeric,
	player_tags text,
	team_position text,
	team_jersey_number text,
	loaned_from text,
	joined date,
	contract_valid_until numeric,
	nation_position text,
	nation_jersey_number text,
	pace numeric,
	shooting numeric,
	passing numeric,
	dribbling numeric,
	defending numeric,
	physic numeric,
	gk_diving numeric,
	gk_handling numeric,
	gk_kicking numeric,
	gk_reflexes numeric,
	gk_speed numeric,
	gk_positioning numeric,
	player_traits text,
	attacking_crossing numeric,
	attacking_finishing numeric,
	attacking_heading_accuracy numeric,
	attacking_short_passing numeric,
	attacking_volleys numeric,
	skill_dribbling numeric,
	skill_curve numeric,
	skill_fk_accuracy numeric,
	skill_long_passing numeric,
	skill_ball_control numeric,
	movement_acceleration numeric,
	movement_sprint_speed numeric,
	movement_agility numeric,
	movement_reactions numeric,
	movement_balance numeric,
	power_shot_power numeric,
	power_jumping numeric,
	power_stamina numeric,
	power_strength numeric,
	power_long_shots numeric,
	mentality_aggression numeric,
	mentality_interceptions numeric,
	mentality_positioning numeric,
	mentality_vision numeric,
	mentality_penalties numeric,
	mentality_composure numeric,
	defending_marking numeric,
	defending_standing_tackle numeric,
	defending_sliding_tackle numeric,
	goalkeeping_diving numeric,
	goalkeeping_handling numeric,
	goalkeeping_kicking numeric,
	goalkeeping_positioning numeric,
	goalkeeping_reflexes numeric,
	ls text,
	st text,
	rs text,
	lw text,
	lf text,
	cf text,
	rf text,
	rw text,
	lam text,
	cam text,
	ram text,
	lm text,
	lcm text,
	cm text,
	rcm text,
	rm text,
	lwb text,
	ldm text,
	cdm text,
	rdm text,
	rwb text,
	lb text,
	lcb text,
	cb text,
	rcb text,
	rb text
);

\copy fifa.players_20 (sofifa_id, player_url, short_name, long_name, age, dob, height_cm, weight_kg, nationality, club, overall, potential, value_eur, wage_eur, player_positions, preferred_foot, international_reputation, weak_foot, skill_moves, work_rate, body_type, real_face, release_clause_eur, player_tags, team_position, team_jersey_number, loaned_from, joined, contract_valid_until, nation_position, nation_jersey_number, pace, shooting, passing, dribbling, defending, physic, gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, player_traits, attacking_crossing, attacking_finishing, attacking_heading_accuracy, attacking_short_passing, attacking_volleys, skill_dribbling, skill_curve, skill_fk_accuracy, skill_long_passing, skill_ball_control, movement_acceleration, movement_sprint_speed, movement_agility, movement_reactions, 	movement_balance, power_shot_power, power_jumping, power_stamina, power_strength, power_long_shots, mentality_aggression, mentality_interceptions, mentality_positioning, mentality_vision, mentality_penalties, mentality_composure, defending_marking, defending_standing_tackle, defending_sliding_tackle, goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking, goalkeeping_positioning, goalkeeping_reflexes, ls, st, rs, lw, lf, cf, rf, rw, lam, cam, ram, lm, lcm, cm, rcm, rm, lwb, ldm, cdm, rdm, rwb, lb, lcb, cb, rcb, rb) from '/Users/Downloads/players_20.csv' DELIMITER ',' CSV HEADER;
