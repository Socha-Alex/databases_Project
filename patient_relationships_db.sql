-- ____________________CREATING AND USING DATABASE________________________________________________________________________________________________________________
-- create database if not exists patient_relationships_db;
-- show databases;
use patient_relationships_db;

--  ___________________CREATING "PROVIDER" TABLE_______________________________________________________________________________________________________
create table provider(
providerID serial not null,
providerFname varchar(20) not null,
providerLname varchar(20) not null,
primary key (providerID)
);

-- ___________________INSERTING VALUES INTO "PROVIDER" TABLE (5 ENTRIES, SEE NOTE BELOW) ______________________________________________________________ 
-- NOTE: WE ONLY DID 5 ENTRIES SINCE OUR DATABASE IS FOR A SMALL MEDICAL OFFICE. WE THOUGHT MORE THAN 5 WOULD BE INAPPROPRIATE.
insert into provider (providerID, providerFname, providerLname) values ("1", "Timothy", "Greer");
insert into provider (providerFname, providerLname) values ("Ron", "Swanson");
insert into provider (providerFname, providerLname) values ("Miranda", "Clark");
insert into provider (providerFname, providerLname) values ("Juan", "Garcia");
insert into provider (providerFname, providerLname) values ("Lyla", "Ng");

-- ___________________CREATING "PATIENT" TABLE_________________________________________________________________________________________________________
create table patient( 
patientID  serial not null,
patientFname varchar(20) not null,
patientLname varchar(20) not null,
patientGender char(1) not null,
phoneNum varchar(10) not null,
DOB varchar(10) not null,
pharmacy_is  bigint unsigned, 
contact_is bigint unsigned,
guardian_is bigint unsigned,
provider_is bigint unsigned not null,
primary key (patientID),
foreign key (provider_is) references provider (providerID)
); 

-- ___________________INSERTING VALUES INTO "PATIENT" TABLE (20 ENTRIES)_______________________________________________________________________________
insert into patient (patientID, patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("1", "Barbara", "Gordon", "F", "2032345678", "04/16/1986", "1");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Scott", "Lang", "M", "2033456789", "12/01/1996", "1");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Hank", "McCoy", "M", "2034567890", "07/04/2000", "1");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Carrie", "Kelly", "F", "2035678901", "09/12/1975", "1");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Selina", "Kyle", "F", "2036789012", "10/31/1969", "2");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Matthew", "Murdock", "M", "2037890123", "02/23/1999", "2");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Viktor", "Fries", "M", "2038901234", "03/02/1992", "2");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Jay", "Garrick", "M", "2030123456", "09/12/1975", "2");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Rita", "Farr", "F", "2039012345", "08/12/1999", "3");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Benjamin", "Tibbetts", "M", "2031023945", "06/20/1979", "3");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Bea", "Huang", "F", "2037775552", "03/27/1939", "3");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Jessica", "Nyguen", "F", "2034256987", "04/14/1939", "3");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Marie", "Kondo", "F", "2032212233", "11/12/2004", "4");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Juanita", "Bueno", "F", "2034251111", "10/17/2005", "4");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Budakar", "Mesa", "M", "2031129874", "03/22/2008", "4");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Nathan", "Hong", "M", "2037789898", "02/11/2008", "4");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Sid", "Bandyopadhya", "M", "2034228686", "11/22/1922", "5");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Layla", "Simone", "F", "2035552211", "09/04/2009", "5");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Bruce", "Lee", "M", "2035554214", "08/03/1931", "5");
insert into patient (patientFname, patientLname, patientGender, phoneNum, DOB, provider_is) values ("Maya", "Hiason", "F", "2039654432", "05/17/2011", "5");

-- ___________________CREATING "PHARMACY" TABLE________________________________________________________________________________________________________
create table pharmacy(
pharmacyID serial not null,
pharmacyName  varchar(20) not null,
pharmacyCity varchar(20) not null,
pharmacyPhoneNum varchar(10) not null,
primary key (pharmacyID)
);

-- ___________________INSERTING VALUES INTO "PHARMACY" TABLE (20 ENTRIES)______________________________________________________________________________
insert into pharmacy (pharmacyID, pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("1", "CVS", "New Haven", "2030987654");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("RiteAid", "East Haven", "2039876543");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Walgreens", "Guilford", "2038765432");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Safeway", "Clinton", "2037654321");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Drug Emporium", "Milford", "2036543210");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Family Pharmacy", "Orange", "2035432109");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Health Mart", "Hartford", "2034321098");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Lewis Drug", "West Haven", "2033210987");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Boone Drug", "North Haven", "2032109876");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Kinney Drugs", "Niantic", "8601098765");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("CVS", "Branford", "2034568971"); 
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("CVS", "East Haven", "2034445656");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("CVS", "West Haven", "2033335858");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("CVS", "Milford", "2036568787");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Walgreens", "East Haven", "2035551111");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Walgreens", "West Haven", "2033256442");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Rite Aid", "Newtown", "2035235423");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Rite Aid", "Guilford", "2036265656");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("Walmart Pharmacy", "Branford", "2035245897");
insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ("CVS", "Orange", "2036455521");

-- ___________________CREATING "EMERGENCY_CONTACT" TABLE_______________________________________________________________________________________________
create table emergency_contact(
contactID serial not null,
contactFname varchar(20) not null,
contactLname varchar(20) not null,
contactPhoneNum varchar(10) not null,
contact_of bigint unsigned not null,
primary key (contactID),
foreign key (contact_of) references patient (patientID)
);

-- ___________________INSERTING VALUES INTO "EMERGENCY_CONTACT" TABLE (20 ENTRIES)_____________________________________________________________________
insert into emergency_contact (contactID, contactFname, contactLname, contactPhoneNum, contact_of) values ("1", "Jonathan", "Osterman", "2031233210", "1");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Walter", "Kovacs", "2032344321", "2");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Luke", "Keller", "2031232109", "3");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Neil", "Morrison", "2030121098", "4");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Cecilia", "Preston", "2039010987", "5");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Angela", "Franklin", "2038909876", "6");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Abigail", "Norman", "2037898765", "7");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Dexter", "Parham", "2036787654", "8");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Tracy", "Jacobs", "2035676543", "9");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Calvin", "Harper", "2034565432", "10");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Joy", "Tosakoon", "2036542315", "11");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Maya", "Angelo", "2035647891", "12");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Maria", "Lopez", "8609929487", "13");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Carlos", "Santana", "2039994899", "14");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Vivian", "Rose", "2039893311", "15");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Mateo", "Esmar", "2037654444", "16");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Ann", "Hong", "2036968451", "17");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Lori", "Do", "2039991112", "18");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Geralda", "Bodi", "2035419999", "19");
insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ("Kensi", "Wang", "2036654621", "20");

-- ___________________CREATING "LEGAL_GUARDIAN" TABLE__________________________________________________________________________________________________
create table legal_guardian(
guardianID serial not null,
guardianFname varchar(20) not null,
guardianLname varchar(20) not null,
guardianPhoneNum varchar(10) not null,
guardian_of bigint unsigned not null,
primary key (guardianID),
foreign key (guardian_of) references patient (patientID)
);

-- ___________________INSERTING VALUES INTO "LEGAL_GUARDIAN" TABLE (10 ENTRIES, SEE NOTE BELOW)________________________________________________________
-- NOTE: WE ONLY DID 10 ENTRIES BECAUSE NOT EVERY ONE OF OUR PATIENTS WILL HAVE A LEGAL GUARDIAN
insert into legal_guardian (guardianID, guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("1", "Thomas", "Meyer", "2032038475", "11");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Emily", "Simon", "2033948576", "12");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Doug", "Freeman", "2034857610", "13");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Grant", "Coleman", "2035867102", "14");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Nathaniel", "Rhodes", "2036720394", "15");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Lizzie", "Fuller", "2031056928", "16");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Arnold", "Neel", "2039112044", "17");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Duncan", "Middleton", "203661529", "18");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Kenny", "Law", "2038013048", "19");
insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ("Jessica", "Parks", "2036103927", "20");

-- ___________________addING MORE foreign keyS TO "PATIENT" TABLE______________________________________________________________________________________
alter table patient
add foreign key (pharmacy_is) references pharmacy (pharmacyID),
add foreign key (contact_is) references emergency_contact (contactID),
add foreign key (guardian_is) references legal_guardian (guardianID);

-- ___________________UPDATING "PATIENT" TABLE TO REFLECT addED foreign keyS (SEE NOTE)__________________________________________________________________
-- NOTE: THESE foreign keyS ARE DEFAULT NULL, SO NOT EVERY PATIENT WILL HAVE ALL OF THEM. ALL OF OUR CURRENT PATIENTS HAPPEN TO HAVE A PHARMACY AND EMERGENCY CONTACT, BUT IT IS NOT REQUIRED. 
update patient set pharmacy_is = "1", contact_is = "1" where (patientID = "1");
update patient set pharmacy_is = "2", contact_is = "2" where (patientID = "2");
update patient set pharmacy_is = "3", contact_is = "3" where (patientID = "3");
update patient set pharmacy_is = "4", contact_is = "4" where (patientID = "4");
update patient set pharmacy_is = "5", contact_is = "5" where (patientID = "5");
update patient set pharmacy_is = "6", contact_is = "6" where (patientID = "6");
update patient set pharmacy_is = "7", contact_is = "7" where (patientID = "7");
update patient set pharmacy_is = "8", contact_is = "8" where (patientID = "8");
update patient set pharmacy_is = "9", contact_is = "9" where (patientID = "9");
update patient set pharmacy_is = "10", contact_is = "10" where (patientID = "10");
update patient set pharmacy_is = "11", contact_is = "11", guardian_is = "1" where (patientID = "11");
update patient set pharmacy_is = "12", contact_is = "12", guardian_is = "2" where (patientID = "12");
update patient set pharmacy_is = "13", contact_is = "13", guardian_is = "3" where (patientID = "13");
update patient set pharmacy_is = "14", contact_is = "14", guardian_is = "4" where (patientID = "14");
update patient set pharmacy_is = "15", contact_is = "15", guardian_is = "5" where (patientID = "15");
update patient set pharmacy_is = "16", contact_is = "16", guardian_is = "6" where (patientID = "16");
update patient set pharmacy_is = "17", contact_is = "17", guardian_is = "7" where (patientID = "17");
update patient set pharmacy_is = "18", contact_is = "18", guardian_is = "8" where (patientID = "18");
update patient set pharmacy_is = "19", contact_is = "19", guardian_is = "9" where (patientID = "19");
update patient set pharmacy_is = "20", contact_is = "20", guardian_is = "10" where (patientID = "20");

/*
DROP FUNCTION IF EXISTS checkPatient;

CREATE FUNCTION checkPatient (message CHAR(150))
RETURNS CHAR(150) DETERMINISTIC
RETURN CONCAT('Note: ',message,'!');

delimiter //
CREATE TRIGGER patientInsert_check AFTER INSERT ON patient
 FOR EACH ROW       
 BEGIN           
	 SELECT checkPatient('If the patient has a legal guardian or emergency contact, remember to insert those into the database as well');      
END;//

delimiter //
CREATE TRIGGER patientCount_check AFTER INSERT ON patient
 FOR EACH ROW       
 BEGIN           
     SELECT count(*) from patient;      
END;//

CREATE TRIGGER showPatients AFTER INSERT ON patient
 FOR EACH ROW       
 BEGIN           
     DESCRIBE patient;     
END;//

drop function checkPatient;

*/

/*
-- ___________________JOINING TABLES___________________________________________________________________________________________________________
-- Joining patient table with all other tables (provider, pharmacy, legal_guardian, emergency_contact)

select patientID, patientFname, patientLname, patientGender, phoneNum, DOB, providerFname, providerLname, pharmacyName, pharmacyCity, pharmacyPhoneNum, guardianFname, guardianLname, guardianPhoneNum, contactFname, contactLname, contactPhoneNum
from patient
join provider on patient.provider_is = provider.providerID
join pharmacy on patient.pharmacy_is = pharmacy.pharmacyID
join legal_guardian on patient.guardian_is = legal_guardian.guardianID
join emergency_contact on patient.contact_is = emergency_contact.contactID
order by patientID;
*/