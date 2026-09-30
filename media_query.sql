SELECT users.username, users.followers, posts.likes
FROM users JOIN posts 
  WHERE posts.user_id = users.user_id;
