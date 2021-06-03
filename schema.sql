CREATE USER IF NOT EXISTS faces@localhost IDENTIFIED BY 'faces';

DROP DATABASE IF EXISTS faces;
CREATE DATABASE faces;

GRANT ALL PRIVILEGES ON faces.* TO faces@localhost;

USE faces;

CREATE TABLE `cameras` (
    `id` INTEGER AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `x` FLOAT NOT NULL,
    `y` FLOAT NOT NULL,

    `rstp` VARCHAR(255) NOT NULL,

    `F` FLOAT DEFAULT 0,

    `current_frame` MEDIUMTEXT
);

CREATE TABLE `known_persons` (
    `id` INTEGER AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `picture` VARCHAR(255) NOT NULL,

    `e2` FLOAT NOT NULL,
    `e1` FLOAT NOT NULL,
    `e3` FLOAT NOT NULL,
    `e4` FLOAT NOT NULL,
    `e5` FLOAT NOT NULL,
    `e6` FLOAT NOT NULL,
    `e7` FLOAT NOT NULL,
    `e8` FLOAT NOT NULL,
    `e9` FLOAT NOT NULL,
    `e10` FLOAT NOT NULL,
    `e11` FLOAT NOT NULL,
    `e12` FLOAT NOT NULL,
    `e13` FLOAT NOT NULL,
    `e14` FLOAT NOT NULL,
    `e15` FLOAT NOT NULL,
    `e16` FLOAT NOT NULL,
    `e17` FLOAT NOT NULL,
    `e18` FLOAT NOT NULL,
    `e19` FLOAT NOT NULL,
    `e20` FLOAT NOT NULL,
    `e21` FLOAT NOT NULL,
    `e22` FLOAT NOT NULL,
    `e23` FLOAT NOT NULL,
    `e24` FLOAT NOT NULL,
    `e25` FLOAT NOT NULL,
    `e26` FLOAT NOT NULL,
    `e27` FLOAT NOT NULL,
    `e28` FLOAT NOT NULL,
    `e29` FLOAT NOT NULL,
    `e30` FLOAT NOT NULL,
    `e31` FLOAT NOT NULL,
    `e32` FLOAT NOT NULL,
    `e33` FLOAT NOT NULL,
    `e34` FLOAT NOT NULL,
    `e35` FLOAT NOT NULL,
    `e36` FLOAT NOT NULL,
    `e37` FLOAT NOT NULL,
    `e38` FLOAT NOT NULL,
    `e39` FLOAT NOT NULL,
    `e40` FLOAT NOT NULL,
    `e41` FLOAT NOT NULL,
    `e42` FLOAT NOT NULL,
    `e43` FLOAT NOT NULL,
    `e44` FLOAT NOT NULL,
    `e45` FLOAT NOT NULL,
    `e46` FLOAT NOT NULL,
    `e47` FLOAT NOT NULL,
    `e48` FLOAT NOT NULL,
    `e49` FLOAT NOT NULL,
    `e50` FLOAT NOT NULL,
    `e51` FLOAT NOT NULL,
    `e52` FLOAT NOT NULL,
    `e53` FLOAT NOT NULL,
    `e54` FLOAT NOT NULL,
    `e55` FLOAT NOT NULL,
    `e56` FLOAT NOT NULL,
    `e57` FLOAT NOT NULL,
    `e58` FLOAT NOT NULL,
    `e59` FLOAT NOT NULL,
    `e60` FLOAT NOT NULL,
    `e61` FLOAT NOT NULL,
    `e62` FLOAT NOT NULL,
    `e63` FLOAT NOT NULL,
    `e64` FLOAT NOT NULL,
    `e65` FLOAT NOT NULL,
    `e66` FLOAT NOT NULL,
    `e67` FLOAT NOT NULL,
    `e68` FLOAT NOT NULL,
    `e69` FLOAT NOT NULL,
    `e70` FLOAT NOT NULL,
    `e71` FLOAT NOT NULL,
    `e72` FLOAT NOT NULL,
    `e73` FLOAT NOT NULL,
    `e74` FLOAT NOT NULL,
    `e75` FLOAT NOT NULL,
    `e76` FLOAT NOT NULL,
    `e77` FLOAT NOT NULL,
    `e78` FLOAT NOT NULL,
    `e79` FLOAT NOT NULL,
    `e80` FLOAT NOT NULL,
    `e81` FLOAT NOT NULL,
    `e82` FLOAT NOT NULL,
    `e83` FLOAT NOT NULL,
    `e84` FLOAT NOT NULL,
    `e85` FLOAT NOT NULL,
    `e86` FLOAT NOT NULL,
    `e87` FLOAT NOT NULL,
    `e88` FLOAT NOT NULL,
    `e89` FLOAT NOT NULL,
    `e90` FLOAT NOT NULL,
    `e91` FLOAT NOT NULL,
    `e92` FLOAT NOT NULL,
    `e93` FLOAT NOT NULL,
    `e94` FLOAT NOT NULL,
    `e95` FLOAT NOT NULL,
    `e96` FLOAT NOT NULL,
    `e97` FLOAT NOT NULL,
    `e98` FLOAT NOT NULL,
    `e99` FLOAT NOT NULL,
    `e100` FLOAT NOT NULL,
    `e101` FLOAT NOT NULL,
    `e102` FLOAT NOT NULL,
    `e103` FLOAT NOT NULL,
    `e104` FLOAT NOT NULL,
    `e105` FLOAT NOT NULL,
    `e106` FLOAT NOT NULL,
    `e107` FLOAT NOT NULL,
    `e108` FLOAT NOT NULL,
    `e109` FLOAT NOT NULL,
    `e110` FLOAT NOT NULL,
    `e111` FLOAT NOT NULL,
    `e112` FLOAT NOT NULL,
    `e113` FLOAT NOT NULL,
    `e114` FLOAT NOT NULL,
    `e115` FLOAT NOT NULL,
    `e116` FLOAT NOT NULL,
    `e117` FLOAT NOT NULL,
    `e118` FLOAT NOT NULL,
    `e119` FLOAT NOT NULL,
    `e120` FLOAT NOT NULL,
    `e121` FLOAT NOT NULL,
    `e122` FLOAT NOT NULL,
    `e123` FLOAT NOT NULL,
    `e124` FLOAT NOT NULL,
    `e125` FLOAT NOT NULL,
    `e126` FLOAT NOT NULL,
    `e127` FLOAT NOT NULL,
    `e128` FLOAT NOT NULL

);

CREATE TABLE `occurrences` (
    `id` INTEGER AUTO_INCREMENT PRIMARY KEY,
    `human_id` VARCHAR(255),
    `face_id` VARCHAR(255),
    `camera_id` INT NOT NULL,
    `timestamp` TIMESTAMP NOT NULL,
    `distance` FLOAT,

    `e1` FLOAT,
    `e2` FLOAT,
    `e3` FLOAT,
    `e4` FLOAT,
    `e5` FLOAT,
    `e6` FLOAT,
    `e7` FLOAT,
    `e8` FLOAT,
    `e9` FLOAT,
    `e10` FLOAT,
    `e11` FLOAT,
    `e12` FLOAT,
    `e13` FLOAT,
    `e14` FLOAT,
    `e15` FLOAT,
    `e16` FLOAT,
    `e17` FLOAT,
    `e18` FLOAT,
    `e19` FLOAT,
    `e20` FLOAT,
    `e21` FLOAT,
    `e22` FLOAT,
    `e23` FLOAT,
    `e24` FLOAT,
    `e25` FLOAT,
    `e26` FLOAT,
    `e27` FLOAT,
    `e28` FLOAT,
    `e29` FLOAT,
    `e30` FLOAT,
    `e31` FLOAT,
    `e32` FLOAT,
    `e33` FLOAT,
    `e34` FLOAT,
    `e35` FLOAT,
    `e36` FLOAT,
    `e37` FLOAT,
    `e38` FLOAT,
    `e39` FLOAT,
    `e40` FLOAT,
    `e41` FLOAT,
    `e42` FLOAT,
    `e43` FLOAT,
    `e44` FLOAT,
    `e45` FLOAT,
    `e46` FLOAT,
    `e47` FLOAT,
    `e48` FLOAT,
    `e49` FLOAT,
    `e50` FLOAT,
    `e51` FLOAT,
    `e52` FLOAT,
    `e53` FLOAT,
    `e54` FLOAT,
    `e55` FLOAT,
    `e56` FLOAT,
    `e57` FLOAT,
    `e58` FLOAT,
    `e59` FLOAT,
    `e60` FLOAT,
    `e61` FLOAT,
    `e62` FLOAT,
    `e63` FLOAT,
    `e64` FLOAT,
    `e65` FLOAT,
    `e66` FLOAT,
    `e67` FLOAT,
    `e68` FLOAT,
    `e69` FLOAT,
    `e70` FLOAT,
    `e71` FLOAT,
    `e72` FLOAT,
    `e73` FLOAT,
    `e74` FLOAT,
    `e75` FLOAT,
    `e76` FLOAT,
    `e77` FLOAT,
    `e78` FLOAT,
    `e79` FLOAT,
    `e80` FLOAT,
    `e81` FLOAT,
    `e82` FLOAT,
    `e83` FLOAT,
    `e84` FLOAT,
    `e85` FLOAT,
    `e86` FLOAT,
    `e87` FLOAT,
    `e88` FLOAT,
    `e89` FLOAT,
    `e90` FLOAT,
    `e91` FLOAT,
    `e92` FLOAT,
    `e93` FLOAT,
    `e94` FLOAT,
    `e95` FLOAT,
    `e96` FLOAT,
    `e97` FLOAT,
    `e98` FLOAT,
    `e99` FLOAT,
    `e100` FLOAT,
    `e101` FLOAT,
    `e102` FLOAT,
    `e103` FLOAT,
    `e104` FLOAT,
    `e105` FLOAT,
    `e106` FLOAT,
    `e107` FLOAT,
    `e108` FLOAT,
    `e109` FLOAT,
    `e110` FLOAT,
    `e111` FLOAT,
    `e112` FLOAT,
    `e113` FLOAT,
    `e114` FLOAT,
    `e115` FLOAT,
    `e116` FLOAT,
    `e117` FLOAT,
    `e118` FLOAT,
    `e119` FLOAT,
    `e120` FLOAT,
    `e121` FLOAT,
    `e122` FLOAT,
    `e123` FLOAT,
    `e124` FLOAT,
    `e125` FLOAT,
    `e126` FLOAT,
    `e127` FLOAT,
    `e128` FLOAT,

    `human_picture` VARCHAR(255) NOT NULL,
    `face_picture` VARCHAR(255),

    `picture_x` FLOAT NOT NULL,
    `picture_y` FLOAT NOT NULL
);