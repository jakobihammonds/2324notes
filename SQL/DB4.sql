CREATE TABLE Accounts(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    address varchar(60),
    city varchar(50),
    state varchar(2),
    zip varchar(5),
    phone varchar(15),
    LastUpdate timestamp DEFAULT CURRENT_TIMESTAMP,
    CreateDate timestamp DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
CREATE TABLE Users(
    id int NOT NULL AUTO_INCREMENT,
    accountId int NOT NULL,
    Email varchar(255) NOT NULL,
    LastName varchar(255),
    FirstName varchar(255),
    Password varchar(8),
    LastLogin timestamp NULL,
    LastUpdate timestamp NULL,
    CreateDate timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY (Email)
);
CREATE TABLE IoT(
   id int NOT NULL AUTO_INCREMENT,
   accountId int NOT NULL,
   TypeId int NOT NULL,
   IMEI char(16) NOT NULL,
   Serial varchar(20) NOT NULL,
   Name varchar(255) NOT NULL,
   Lat int,
   Lng int,
   Alt int,
   Speed int,
   Direction int,
   Bearing int,
   LastUpdate timestamp NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
   PRIMARY KEY (Id)
);
CREATE TABLE Groups(
   id int NOT NULL,
   accountId int NOT NULL,
   Name varchar(255),
   LastUpdate timestamp NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
   PRIMARY KEY (Id)
);
CREATE TABLE IoTGroups(
   id int NOT NULL,
   IoTId int NOT NULL,
   GroupId int NOT NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
   PRIMARY KEY (Id)
);
CREATE TABLE States(
   id int NOT NULL,
   State varchar(2) NULL,
   UNIQUE KEY (State),
   PRIMARY KEY (id)
);