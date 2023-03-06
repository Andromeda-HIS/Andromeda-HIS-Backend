INSERT INTO `Admin` VALUES('Albert','hms','Albert Einstein','123 Rhinestrasse, Berlin');

INSERT INTO `Patient` VALUES(0,'Marconi','C-33 Hall Street, Geneva, Switzerland', True);
INSERT INTO `Patient` VALUES(0,'Isaac','A-56 Beacon Street, Lucknow, India', True);
INSERT INTO `Patient` VALUES(0,'Charles','B-3, Berlington Street, New York, USA', True);
INSERT INTO `Patient` VALUES(0,'Marie','D-12 Hill Street, Kolkata, India', False);

INSERT INTO `Room` VALUES(0, False);
INSERT INTO `Room` VALUES(0, False);
INSERT INTO `Room` VALUES(0, True);
INSERT INTO `Room` VALUES(0, False);
INSERT INTO `Room` VALUES(0, True);
INSERT INTO `Room` VALUES(0, True);
INSERT INTO `Room` VALUES(0, True);

INSERT INTO `Doctor` VALUES('galileo', 'galileogal', 'Galileo Galilei', 'House 34, Gali Street, Capetown', 'Neurology');
INSERT INTO `Doctor` VALUES('stephen', 'stephenhawk', 'Stephen Hawking', 'House 55, Hari Street, Wellington', 'Cardiology');
INSERT INTO `Doctor` VALUES('nikola', 'nikolates', 'Nikola Tesla', 'House 1, Rali Street, Auckland', 'Oncology');
INSERT INTO `Doctor` VALUES('thomas', 'thomased', 'Thomas Edison', 'House 9, Dali Street, Birmingham', 'Pathology');

INSERT INTO `Front_Desk_Operator` VALUES('michael', 'michaelfar', 'Michael Faraday', 'House 2, Mion Street, Melbourne');
INSERT INTO `Front_Desk_Operator` VALUES('james', 'jamesmax', 'James Maxwell', 'House 22, Max Street, Adelaide');

INSERT INTO `Data_Entry_Operator` VALUES('richard', 'richardfey', 'Richard Feynman', 'House 13, Rich Street, Madagascar');

INSERT INTO `Admitted` VALUES(0, 1, 4,True);
INSERT INTO `Admitted` VALUES(0, 2, 2,True);
INSERT INTO `Admitted` VALUES(0, 3, 1,True);

INSERT INTO `Appointment` VALUES(0, 1, 'galileo', '2023-03-02', 'cough, sore throat', False);
INSERT INTO `Appointment` VALUES(0, 2, 'stephen', '2023-03-03', 'weakness, red-eyes, cough', False);
INSERT INTO `Appointment` VALUES(0, 3, 'nikola', '2023-03-04', 'fever, high blood pressure', False);
INSERT INTO `Appointment` VALUES(0, 4, 'thomas', '2023-03-05', 'muscular cramps', False);