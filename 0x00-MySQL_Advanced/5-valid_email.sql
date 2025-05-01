-- Creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMTER ;
CREATE TRIGGER validate_email BEFORE UPDATE ON user
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
	NEW.valid_email = 0
	ELSE
	SET NEW.valid_email = NEW.valid_email;
	END IF
END $$
DELIMITER ;
	
