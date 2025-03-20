CREATE DATABASE smartfaq;
USE smartfaq;

CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    domain VARCHAR(50) NOT NULL
);
