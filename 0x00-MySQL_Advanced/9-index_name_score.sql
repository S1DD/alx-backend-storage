--  Script that creates an index idx_name_first_score on the table names and the first letter of name and the score.
CRETE INDEX idx_name_first_score on names(name(1), score);
