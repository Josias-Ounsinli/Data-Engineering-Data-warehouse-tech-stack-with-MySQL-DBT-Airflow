CREATE TABLE IF NOT EXISTS vehicles
(
    "id" INT NOT NULL AUTO_INCREMENT,
    "track_id" TEXT NOT NULL,
    "lat" TEXT NOT NULL,
    "lon" TEXT DEFAULT NULL,
    "speed" TEXT DEFAULT NULL,
    "lon_acc" TEXT DEFAULT NULL,
    "lat_acc" TEXT DEFAULT NULL,
    "time" TEXT DEFAULT NULL,
    PRIMARY KEY ("id"),
    FOREIGN KEY ('track_id') REFERENCES CARS('track_id')
);