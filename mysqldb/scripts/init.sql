CREATE DATABASE IF NOT EXISTS strongdm;

CREATE USER 'jimmy'@'localhost' IDENTIFIED BY 'jimmy9478';

GRANT ALL ON strongdm.* TO 'jimmy'@'localhost';

CREATE DATABASE IF NOT EXISTS cloud_config;

USE cloud_config;

create table
    PROPERTIES(
        application varchar(256),
        profile varchar(256),
        label varchar(256),
        `key` varchar(256),
        value varchar(256)
    );

insert into PROPERTIES
values (
        'api',
        'dev',
        'latest',
        'sample key',
        'a value'
    );

CREATE DATABASE IF NOT EXISTS auth;

USE auth ;