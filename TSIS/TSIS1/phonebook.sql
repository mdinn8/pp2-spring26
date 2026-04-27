DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS groups;
DROP TABLE IF EXISTS phones;

CREATE TABLE contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(100)
);

CREATE TABLE groups (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

ALTER TABLE contacts
    ADD COLUMN email    VARCHAR(100),
    ADD COLUMN birthday DATE,
    ADD COLUMN group_id INTEGER REFERENCES groups(id);

CREATE TABLE phones (
    id         SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone      VARCHAR(20)  NOT NULL,
    type       VARCHAR(10)  CHECK (type IN ('home', 'work', 'mobile'))
);

CREATE OR REPLACE FUNCTION get_contacts_by_patterns(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY SELECT c.name, c.phone FROM contacts c
        WHERE c.name ILIKE '%' || p || '%'
        OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN 
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_new_users(names VARCHAR[], phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE 
    i INT;
    invalid_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR I IN 1..array_length(names, 1) LOOP
        IF phones[i] ~'^\d+$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;

    IF array_length(invalid_data, 1) IS NOT NULL THEN
        RAISE NOTICE 'Invalid data: %', array_to_string(invalid_data, ',');
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM contacts
    ORDER BY id 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE deleting_contacts(p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    ELSE
        RAISE NOTICE 'No name or phone provided!';
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id FROM contacts WHERE name = p_contact_name;
    INSERT INTO phones(contact_id, phone, type) VALUES (contact_id, p_phone, p_type);
END;
$$;

CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE 
    v_group_id INT;
BEGIN
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    IF v_group_id IS NULL THEN 
        INSERT INTO groups(name) VALUES(p_group_name) RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE name = p_contact_name;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.id, c.name, c.phone, c.email
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.name ILIKE '%' || p_query || '%'
    OR c.email ILIKE '%' || p_query || '%'
    OR p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;


CALL upsert_contact('Madina', '87767321438');
CALL upsert_contact('Mad885', '87765321438');
CALL upsert_contact('Ma', '879561438');
CALL upsert_contact('Mdin', '821438');
--pagination
SELECT get_contacts_paginated(1, 2);
--search by patterns
SELECT get_contacts_by_patterns('776732');
--insert with array
CALL insert_new_users(ARRAY['fghj', 'ghjk', 'ghjkjk'], ARRAY['74185','85296','8525']);
SELECT * FROM contacts;
-- deleting
CALL deleting_contacts(p_name := 'Ma');
--add phone to phones
CALL add_phone('Merey', '87767361498', 'work');
--move to group
CALL move_to_group('Merey', 'family');
--search contacts 
SELECT * FROM search_contacts('8776')

SELECT * FROM contacts;