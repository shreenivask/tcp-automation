-- Database
CREATE DATABASE tc_python_framework;

--  User table definition
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT (CURRENT_DATE),
  `updated_at` datetime DEFAULT (CURRENT_DATE),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- User table data
INSERT INTO tc_python_framework.`user` (first_name,last_name,email,phone,password,`role`,updated_at,created_at) VALUES
   ('User','One','userone@targetclose.com','9988776655','3ffb4015404b4444251a5d94f08df277414924c03742b432066c0fe5ef2a6fd2','user',NOW(),NOW()),
   ('User','Two','usertwo@targetclose.com','9988776644','3ffb4015404b4444251a5d94f08df277414924c03742b432066c0fe5ef2a6fd2','user',NOW(),NOW()),
   ('Admin','User','admin@targetclose.com','9988776633','3ffb4015404b4444251a5d94f08df277414924c03742b432066c0fe5ef2a6fd2','admin',NOW(),NOW());


-- Test table definition
CREATE TABLE `test` (
  `id` int NOT NULL AUTO_INCREMENT,
  `test_ticket` varchar(255) DEFAULT NULL,
  `test_description` varchar(255) DEFAULT NULL,
  `test_executed_by` varchar(255) DEFAULT NULL,
  `test_report_file` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--  Client table definition

CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `client_name` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT (CURRENT_DATE),
  `updated_at` datetime DEFAULT (CURRENT_DATE),
  `IsActive` TINYINT(1) NOT NULL DEFAULT 1,
  UNIQUE KEY `client_name` (`client_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Client table data
INSERT INTO client (id, client_name) VALUES (1, 'AARP'), (2, 'INOGEN'),  (3, 'RIF'), (4, 'JAYA'), (5, 'GREETINGGENIE') ;

--  test_case table definition

CREATE TABLE `test_case` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `test_case_name` varchar(100) NOT NULL,
  `client_id` INT NOT NULL,
  `created_at` datetime DEFAULT (CURRENT_DATE),
  `updated_at` datetime DEFAULT (CURRENT_DATE),
  UNIQUE KEY `test_case_name` (`test_case_name`),
  FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- test_case table data

INSERT INTO `test_case` (`test_case_name`, `client_id`, `created_at`, `updated_at`) 
VALUES 
('Verify Join Page with parameters', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Renew Page with parameters', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Meta Tags', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Https Links', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Page Meta Tags Index Follow', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify v60 and v197 in Smetric Network', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Class Names', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify CTA query string', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Console Error', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Correct Premium Name', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify CTA Click Functionality', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Page in Different Browser Widths', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Page by Scrolling', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Header phone number', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify Category query string', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
('Verify PYP Functionality', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

--  test_case table altered to accomodate function

ALTER TABLE `test_case`
ADD COLUMN `test_function` VARCHAR(255) NOT NULL;

--  test_case table add alterede function data

UPDATE `test_case`
SET `test_function` = 'aarp_join_page_with_parameter'
WHERE `test_case_name` = 'Verify Join Page with parameters';

UPDATE `test_case`
SET `test_function` = 'aarp_renew_page_with_parameter'
WHERE `test_case_name` = 'Verify Renew Page with parameters';

UPDATE `test_case`
SET `test_function` = 'aarp_meta_tags'
WHERE `test_case_name` = 'Verify Meta Tags';

UPDATE `test_case`
SET `test_function` = 'aarp_https_link_verification'
WHERE `test_case_name` = 'Verify Https Links';

UPDATE `test_case`
SET `test_function` = 'aarp_meta_tags_index_follow'
WHERE `test_case_name` = 'Verify Page Meta Tags Index Follow';

UPDATE `test_case`
SET `test_function` = 'aarp_smetric_in_network'
WHERE `test_case_name` = 'Verify v60 and v197 in Smetric Network';

UPDATE `test_case`
SET `test_function` = 'aarp_verify_class_name'
WHERE `test_case_name` = 'Verify Class Names';

UPDATE `test_case`
SET `test_function` = 'aarp_cta_qs_button'
WHERE `test_case_name` = 'Verify CTA query string';

UPDATE `test_case`
SET `test_function` = 'aarp_verify_console_error'
WHERE `test_case_name` = 'Verify Console Error';

UPDATE `test_case`
SET `test_function` = 'aarp_verify_correct_premium_name'
WHERE `test_case_name` = 'Verify Correct Premium Name';

UPDATE `test_case`
SET `test_function` = 'aarp_cta_click'
WHERE `test_case_name` = 'Verify CTA Click Functionality';

UPDATE `test_case`
SET `test_function` = 'aarp_different_browser_widths'
WHERE `test_case_name` = 'Verify Page in Different Browser Widths';

UPDATE `test_case`
SET `test_function` = 'aarp_different_widths_with_scroll'
WHERE `test_case_name` = 'Verify Page by Scrolling';

UPDATE `test_case`
SET `test_function` = 'aarp_lg_copy_text_verification'
WHERE `test_case_name` = 'Verify Header phone number';

UPDATE `test_case`
SET `test_function` = 'aarp_category_level_accord"'
WHERE `test_case_name` = 'Verify Category query string';

UPDATE `test_case`
SET `test_function` = 'aarp_join_renew_with_parameter_pyp'
WHERE `test_case_name` = 'Verify PYP Functionality';

--  test_suite table definition

CREATE TABLE `test_suite` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `test_suite_name` varchar(100) NOT NULL,
  `client_id` INT NOT NULL,
  `test_case_ids` JSON,
  `created_at` datetime DEFAULT (CURRENT_DATE),
  `updated_at` datetime DEFAULT (CURRENT_DATE),
  UNIQUE KEY `test_suite_name` (`test_suite_name`),
  FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- to make the testcase JSON values unique To enforce uniqueness on the test_case_ids JSON column in MySQL, you cannot directly apply a UNIQUE constraint on the JSON field itself, because MySQL does not support indexing on JSON columns by default. However, you can achieve this uniqueness by using a workaround with a generated column or by storing the individual elements from the test_case_ids JSON column

ALTER TABLE `test_suite`
  ADD COLUMN `test_case_ids_hash` varchar(255) GENERATED ALWAYS AS (MD5(CAST(test_case_ids AS CHAR))) STORED,
  ADD UNIQUE KEY `unique_test_case_ids_hash` (`test_case_ids_hash`);

-- test_suite table data

INSERT INTO test_suite (test_suite_name, client_id, test_case_ids, created_at, updated_at)
VALUES ('Master Checklist', 1, '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]', NOW(), NOW());

--  test_execution table definition

CREATE TABLE `test_execution` (
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `test_ticket` VARCHAR(25) NOT NULL,
  `user_id` INT NOT NULL,
  `client_id` INT NOT NULL,
	`test_case_id` INT NOT NULL,
	`test_suite_id` INT,
	`created_at` datetime DEFAULT (CURRENT_DATE),
	`updated_at` datetime DEFAULT (CURRENT_DATE),
  `test_description` varchar(255) DEFAULT NULL,
	`test_report_file` varchar(255) DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE,
	  FOREIGN KEY (test_case_id) REFERENCES test_case(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- Test suite queries
INSERT INTO test_suite (id, test_suite_name,client_id,test_case_ids) VALUES (1, 'Test Suite 1', 1,'[1, 2, 3]');

SELECT JSON_EXTRACT(test_case_ids, '$[0]') AS first_test_case 
FROM test_suite 
WHERE id = 1;

