create table Location(
    location_id integer NOT NULL PRIMARY KEY,
    latitude integer NOT NULL UNIQUE,
    longitude integer NOT NULL UNIQUE
 
);

create table Params(
    params_id integer NOT NULL PRIMARY KEY,
    brightness float NOT NULL,
    frp float NOT NULL
);

create table Confidence(
  confidence integer NOT NULL PRIMARY key
);

create table Fire_info(
    fire_id integer not NULL PRIMARY KEY,
    location_id integer not NULL UNIQUE,
    params_id integer not NULL UNIQUE,
    confidence integer not NULL
);

ALTER TABLE Fire_info ADD CONSTRAINT fk_location_id FOREIGN key(location_id) REFERENCES Location(location_id);

ALTER TABLE Fire_info ADD CONSTRAINT fk_params_id FOREIGN key(params_id) REFERENCES Params(params_id);

ALTER TABLE Fire_info ADD CONSTRAINT fk_confidence FOREIGN key(confidence) REFERENCES Confidence(confidence);



