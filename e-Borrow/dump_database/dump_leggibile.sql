CREATE DATABASE IF NOT EXISTS eborrow;
USE eborrow;

DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS offers;
DROP TABLE IF EXISTS requests;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS notifications;

CREATE TABLE users (
    id VARCHAR(64) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE requests (
    id VARCHAR(64) PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    message TEXT,
    urgency INT,
    importance INT,
    time INT,
    borrower VARCHAR(100),
    status VARCHAR(30) DEFAULT 'in attesa',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE offers (
    id VARCHAR(64) PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    message TEXT,
    lender VARCHAR(100),
    status VARCHAR(30) DEFAULT 'disponibile',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE loans (
    id VARCHAR(64) PRIMARY KEY,
    item_name VARCHAR(100),
    message TEXT,
    borrower VARCHAR(100),
    lender VARCHAR(100),
    status VARCHAR(30) DEFAULT 'preso in carico',
    start_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    end_date TIMESTAMP NULL
);

CREATE TABLE notifications (
    id VARCHAR(64) PRIMARY KEY,
    user VARCHAR(100),
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);