CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL UNIQUE,
	followers INT NOT NULL DEFAULT 0,
	following INT NOT NULL DEFAULT 0
);

CREATE TABLE posts (
	post_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT NOT NULL,
	likes INT NOT NULL DEFAULT 0,
	comments INT NOT NULL DEFAULT 0,
	shares INT NOT NULL DEFAULT 0,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);


INSERT INTO users (user_id, username, followers, following) VALUES (1,  'Jimmy',   500, 501);
INSERT INTO users (user_id, username, followers, following) VALUES (2,  'Elliot',   120, 80);
INSERT INTO users (user_id, username, followers, following) VALUES (3,  'John',   95, 87);
INSERT INTO users (user_id, username, followers, following) VALUES (4,  'Mark',   110, 200);
INSERT INTO users (user_id, username, followers, following) VALUES (5,  'Lucas',   178, 203);
INSERT INTO users (user_id, username, followers, following) VALUES (6,  'Diego',   197, 190);
INSERT INTO users (user_id, username, followers, following) VALUES (7,  'Thomas',   1240, 1304);
INSERT INTO users (user_id, username, followers, following) VALUES (8,  'Prabhav',   1100, 1005);
INSERT INTO users (user_id, username, followers, following) VALUES (9,  'Rylan',   890, 3);
INSERT INTO users (user_id, username, followers, following) VALUES (10,  'Avery',   654, 500);

INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (1,  1,  100,  5,  1);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (2,  2,  189,  9,  2);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (3,  3,  78,  20,  1);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (4,  4,  52,  28,  6);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (5,  5,  31,  61,  3);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (6,  6,  30,  52,  19);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (7,  7,  97,  73,  9);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (8,  8,  295,  88,  6);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (9,  9,  9182,  285,  555);
INSERT INTO posts (post_id, user_id, likes, comments, shares) VALUES (10,  1,  7,  3,  0);

