CREATE TABLE sales
(
    id           INT AUTO_INCREMENT PRIMARY KEY,
    order_date   VARCHAR(100) NOT NULL,
    bucket       INT          NOT NULL
);
-- 2.
INSERT INTO sales