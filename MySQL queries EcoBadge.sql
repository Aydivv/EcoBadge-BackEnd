CREATE TABLE business(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    address VARCHAR(255),
    postcode VARCHAR(50),
    pNumber VARCHAR(20),
    email VARCHAR(100),
    description VARCHAR(255),
    website VARCHAR(255),
    cuisine VARCHAR(255),
    scored BOOLEAN
)

CREATE TABLE score(
    business_id INT,
    score INT,
    vegan BOOLEAN,
    singleUsePlastic BOOLEAN,
    foodwasteCollection BOOLEAN,
    localProduce BOOLEAN,
    latest BOOLEAN,
    dateOfScore DATETIME,
    PRIMARY KEY (business_id,dateOfScore),
    FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE TABLE user(
    id VARCHAR(20) PRIMARY KEY NOT NULL,
    email VARCHAR(255),
    name VARCHAR(255),
    priority INT(20),
);

CREATE TABLE review(
    id INT PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(255),
    user_id VARCHAR(50),
    business_id INT,
    date_created DATETIME,
    reply_of INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (business_id) REFERENCES business(id)
);

CREATE VIEW businessScores
AS 
SELECT b.id,b.name,b.address,b.postcode,b.description,b.cuisine,b.scored,s.score
FROM business as b, score as s 
WHERE b.id = s.business_id and s.latest=true;
