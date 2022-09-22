CREATE TABLE IF NOT EXISTS CARS
(
    "track_id" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "traveled_d" TEXT DEFAULT NULL,
    "avg_speed" TEXT DEFAULT NULL,
    PRIMARY KEY ("track_id")
);