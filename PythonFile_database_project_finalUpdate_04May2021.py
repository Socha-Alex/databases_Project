def MainWindow():
    #Create a window for the database
    window = tk.Tk()
    window.title("Patient Relationships Database")
    window.geometry = ("500x500")

    #Create a frame to change the background color
    frame_main = Frame(window, bg = "white", width = 500, height = 500)
    frame_main.grid(row = 10, column = 10)

    #Create label to display welcome message
    label_welcome = Label(frame_main, text = "Welcome to the Patient Relationships Database",fg = "black", bg = "white", font = ("Courier", 16))
    label_welcome.grid(row = 0, column = 0, pady = 10)

    #Create label to display instructions
    label_instructions = Label(frame_main, text = "What would you like to insert, update, delete, or search? ",fg = "black", bg = "white")
    label_instructions.grid(row = 1, column = 0, pady = 10)

    #Create buttons for database entities
    button_patient = Button(frame_main, fg = "black", bg = "light blue", text = "Patient", command = PatientWindow)
    button_patient.grid(row = 2, column = 0, pady = 5)

    button_provider = Button(frame_main, fg = "black", bg = "lawn green", text = "Provider", command = ProviderWindow)
    button_provider.grid(row = 3, column = 0, pady = 5)

    button_pharmacy = Button(frame_main, fg = "black", bg = "orange", text = "Pharmacy", command = PharmacyWindow)
    button_pharmacy.grid(row = 4, column = 0, pady = 5)

    button_legalGuardian = Button(frame_main, fg = "black", bg = "mediumpurple1", text = "Legal Guardian", command = GuardianWindow)
    button_legalGuardian.grid(row = 5, column = 0, pady = 5)

    button_emergencyContact = Button(frame_main, fg = "black", bg = "yellow", text = "Emergency Contact", command = ContactWindow)
    button_emergencyContact.grid(row = 6, column = 0, pady = 5)

######################################################
#PATIENT-RELATED FUNCTIONS AND WINDOW
    
def InsertPatient():
    #Link SQL attributes with GUI variables
    patientFname = entry_patientFname.get()
    patientLname = entry_patientLname.get()
    patientGender = entry_patientGender.get()
    phoneNum = entry_patientPhone.get()
    DOB = entry_patientDOB.get()
    pharmacy_is = entry_patientPharmacy.get()
    contact_is = entry_patientContact.get()
    guardian_is = entry_patientGuardian.get()
    provider_is = entry_patientProvider.get()

    #Send SQL statement to database as a string
    insert_patient = """Insert into patient(patientFname, patientLname, patientGender, phoneNum, DOB, pharmacy_is, contact_is, guardian_is, provider_is) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");"""%(patientFname, patientLname, patientGender, phoneNum, DOB, pharmacy_is, contact_is, guardian_is, provider_is)
    mycursor.execute(insert_patient)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_insert = Label(success_window, text = "Insert Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_insert.grid(row = 20, column = 0)



def UpdatePatient():
    #Link SQL attributes with GUI variables
    patientID = entry_patientID.get()
    patientFname = entry_patientFname.get()
    patientLname = entry_patientLname.get()
    patientGender = entry_patientGender.get()
    phoneNum = entry_patientPhone.get()
    DOB = entry_patientDOB.get()
    pharmacy_is = entry_patientPharmacy.get()
    contact_is = entry_patientContact.get()
    guardian_is = entry_patientGuardian.get()
    provider_is = entry_patientProvider.get()

    #Send SQL statement to database as a string
    update_patient = "Update patient set patientFname='%s', patientLname='%s', patientGender='%s', phoneNum='%s', DOB='%s', pharmacy_is='%s', contact_is='%s', guardian_is='%s', provider_is='%s' where patientID= '%s' ;" % (patientFname, patientLname, patientGender, phoneNum, DOB, pharmacy_is, contact_is, guardian_is, provider_is, patientID)
    mycursor.execute(update_patient)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_update = Label(success_window, text = "Update Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_update.grid(row = 20, column = 0)



def DeletePatient():
    #Link SQL attributes with GUI variables
    patientID = entry_patientID.get()

    #Send SQL statement to database as a string
    delete_patient = "Delete from patient where patientID='%s';" % (patientID)
    mycursor.execute(delete_patient)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_delete = Label(success_window, text = "Delete Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_delete.grid(row = 20, column = 0)



def SearchPatient():
    #Link SQL attributes with GUI variables
    patientID = entry_patientID.get()

    #Send SQL statement to database as a string
    search_patient = "Select * from patient where patientID='%s';" % (patientID)
    mycursor.execute(search_patient)
    patient = mycursor.fetchone()
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_search = Label(success_window, text = "Patient ID:   %s \n First Name:    %s \n Last Name:    %s \n Gender:    %s \n Phone:    %s \n DOB:    %s \n Pharmacy ID:    %s \n Emergency Contact ID:    %s \n, Legal Guardian ID:    %s \n, Provider ID:    %s \n " % (patient), fg = "black", bg = "light pink", justify = LEFT)
    label_success_search.grid(row = 20, column = 0)


    
def PatientWindow():
    #Create new window to display patient fields and options
    patient_window = tk.Tk()
    patient_window.title("Patient")
    patient_window.geometry = ("500x500")

    #Label to display instructions
    label_instruction = Label(patient_window, text = "For Insert: Enter all fields except ID. \nFor Update: Enter all fields. \nFor Delete: Enter ID only. \nFor Search: Enter ID only. ",font = ("Courier", 10), justify = LEFT, fg = "black", bg = "light yellow")
    label_instruction.grid(row = 0, column = 0)

    #Create labels and entries for patient, set global variables 
    label_patientID = Label(patient_window, text = "PatientID",fg = "black", bg = "white")
    label_patientID.grid(row = 1, column = 0, padx = 5)
    global entry_patientID
    entry_patientID = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientID.grid(row = 2, column = 0, padx = 5)

    label_patientFname = Label(patient_window, text = "Patient First Name",fg = "black", bg = "white")
    label_patientFname.grid(row = 3, column = 0, padx = 5)
    global entry_patientFname
    entry_patientFname = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientFname.grid(row = 4, column = 0, padx = 5)

    label_patientLname = Label(patient_window, text = "Patient Last Name",fg = "black", bg = "white")
    label_patientLname.grid(row = 5, column = 0, padx = 5)
    global entry_patientLname
    entry_patientLname = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientLname.grid(row = 6, column = 0, padx = 5)

    label_patientDOB = Label(patient_window, text = "Patient DOB",fg = "black", bg = "white")
    label_patientDOB.grid(row = 7, column = 0, padx = 5)
    global entry_patientDOB
    entry_patientDOB = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientDOB.grid(row = 8, column = 0, padx = 5)

    label_patientGender = Label(patient_window, text = "Patient Gender",fg = "black", bg = "white")
    label_patientGender.grid(row = 9, column = 0, padx = 5)
    global entry_patientGender
    entry_patientGender = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientGender.grid(row = 10, column = 0, padx = 5)

    label_patientPhone = Label(patient_window, text = "Patient Phone",fg = "black", bg = "white")
    label_patientPhone.grid(row = 11, column = 0, padx = 5)
    global entry_patientPhone
    entry_patientPhone = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientPhone.grid(row = 12, column = 0, padx = 5)

    label_patientPharmacy = Label(patient_window, text = "Patient Pharmacy (PharmacyID)",fg = "black", bg = "white")
    label_patientPharmacy.grid(row = 13, column = 0, padx = 5)
    global entry_patientPharmacy
    entry_patientPharmacy = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientPharmacy.grid(row = 14, column = 0, padx = 5)

    label_patientContact = Label(patient_window, text = "Patient's Emergency Contact (ContactID)",fg = "black", bg = "white")
    label_patientContact.grid(row = 15, column = 0, padx = 5)
    global entry_patientContact
    entry_patientContact = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientContact.grid(row = 16, column = 0, padx = 5)

    label_patientGuardian = Label(patient_window, text = "Patient's Legal Guardian (GuardianID)",fg = "black", bg = "white")
    label_patientGuardian.grid(row = 17, column = 0, padx = 5)
    global entry_patientGuardian
    entry_patientGuardian = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientGuardian.grid(row = 18, column = 0, padx = 5)

    label_patientProvider = Label(patient_window, text = "Patient's Provider (ProviderID)",fg = "black", bg = "white")
    label_patientProvider.grid(row = 19, column = 0, padx = 5)
    global entry_patientProvider
    entry_patientProvider = Entry(patient_window, fg = 'black', bg = 'white', width = 10)
    entry_patientProvider.grid(row = 20, column = 0, padx = 5)
    
    #Create a button to initiate options to insert into database
    button_insert = Button(patient_window, fg = "black", bg = "light blue", text = "Insert", command = InsertPatient)
    button_insert.grid(row = 17, column = 10, pady = 5)

    #Create a button to initiate options to update database
    button_update = Button(patient_window, fg = "black", bg = "lawn green", text = "Update", command = UpdatePatient)
    button_update.grid(row = 18, column = 10, pady = 5)

    #Create a button to initiate options to delete in database
    button_delete = Button(patient_window, fg = "black", bg = "orange", text = "Delete", command = DeletePatient)
    button_delete.grid(row = 19, column = 10, pady = 5)

    #Create a button to initiate options to search in database
    button_search = Button(patient_window, fg = "black", bg = "mediumpurple1", text = "Search", command = SearchPatient)
    button_search.grid(row = 20, column = 10, pady = 5)

######################################################
#PROVIDER-RELATED FUNCTIONS AND WINDOW

def UpdateProvider():
    #Link SQL attributes with GUI variables
    providerID = entry_providerID.get()
    providerFname = entry_providerfname.get()
    providerLname = entry_providerLname.get()
    
    #Send SQL update statement to database as a string
    update_provider = "Update provider set providerFname='%s', providerLname='%s'  where providerID= '%s' ;" % (providerFname, providerLname, providerID)
    mycursor.execute(update_provider)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_update = Label(success_window, text = "Update Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_update.grid(row = 20, column = 0)



def DeleteProvider():
    #Link SQL attributes with GUI variables
    providerID = entry_providerID.get()
    
    #Send SQL statement to database as a string
    delete_provider = "Delete from provider where providerID= '%s' ;" % (providerID)
    mycursor.execute(delete_provider)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_delete = Label(success_window, text = "Delete Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_delete.grid(row = 20, column = 0)



def InsertProvider():
    #Link SQL attributes with GUI variables
    providerFname = entry_providerfname.get()
    providerLname = entry_providerLname.get()
    
    #Send SQL statement to database as a string
    insert_provider = "Insert into provider (providerFname, providerLname) values ('%s', '%s');" % (providerFname, providerLname)
    mycursor.execute(insert_provider)
    db.commit()

 #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_insert = Label(success_window, text = "Insert Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_insert.grid(row = 20, column = 0)



def SearchProvider():
    #Link SQL attributes with GUI variables
    providerID = entry_providerID.get()

    #Send SQL statement to database as a string
    search_provider = "Select * from provider where providerID='%s';" % (providerID)
    mycursor.execute(search_provider)
    provider = mycursor.fetchone()
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_search = Label(success_window, text = "Provider ID:   %s \n First Name:    %s \n Last Name:    %s \n " % (provider), fg = "black", bg = "light pink", justify = LEFT)
    label_success_search.grid(row = 20, column = 0)
    


def ProviderWindow():
    #Create new window to display provider fields and options
    provider_window = tk.Tk()
    provider_window.title("Provider")
    provider_window.geometry = ("500x500")

    #Label to display instructions
    label_instruction = Label(provider_window, text = "For Insert: Enter all fields except ID. \nFor Update: Enter all fields. \nFor Delete: Enter ID only. \nFor Search: Enter ID only. ",font = ("Courier", 10), justify = LEFT, fg = "black", bg = "light yellow")
    label_instruction.grid(row = 0, column = 0)

    #Create labels and entries for PROVIDER

    label_providerID = Label(provider_window, text = "Provider ID",fg = "black", bg = "white")
    label_providerID.grid(row = 1, column = 0, padx = 5)
    global entry_providerID
    entry_providerID = Entry(provider_window, fg = 'black', bg = 'white', width = 10)
    entry_providerID.grid(row = 2, column = 0, padx = 5)

    label_providerfname = Label(provider_window, text = "Provider First Name",fg = "black", bg = "white")
    label_providerfname.grid(row = 3, column = 0, padx = 5)
    global entry_providerfname
    entry_providerfname = Entry(provider_window, fg = 'black', bg = 'white', width = 10)
    entry_providerfname.grid(row = 4, column = 0, padx = 5)

    label_providerLname = Label(provider_window, text = "Provider Last Name",fg = "black", bg = "white")
    label_providerLname.grid(row = 5, column = 0, padx = 5)
    global entry_providerLname
    entry_providerLname = Entry(provider_window, fg = 'black', bg = 'white', width = 10)
    entry_providerLname.grid(row = 6, column = 0, padx = 5)

    #Create a button to initiate options to insert into database
    button_insert = Button(provider_window, fg = "black", bg = "light blue", text = "Insert", command = InsertProvider)
    button_insert.grid(row = 3, column = 8, pady = 5)

    #Create a button to initiate options to update database
    button_update = Button(provider_window, fg = "black", bg = "lawn green", text = "Update", command = UpdateProvider)
    button_update.grid(row = 4, column = 8, pady = 5)

    #Create a button to initiate options to delete in database
    button_delete = Button(provider_window, fg = "black", bg = "orange", text = "Delete", command = DeleteProvider)
    button_delete.grid(row = 5, column = 8, pady = 5)

    #Create a button to initiate options to search in database
    button_search = Button(provider_window, fg = "black", bg = "mediumpurple1", text = "Search", command = SearchProvider)
    button_search.grid(row = 6, column = 8, pady = 5)

######################################################
#PHARMACY-RELATED FUNCTIONS AND WINDOW

def UpdatePharmacy():
    #Link SQL attributes with GUI variables
    pharmacyID = entry_pharmacyID.get()
    pharmacyName = entry_pharmacyName.get()
    pharmacyCity = entry_pharmacyCity.get()
    pharmacyPhoneNum = entry_pharmacyPhoneNum.get()

    #Send SQL statement to database as a string
    update_pharmacy = "Update pharmacy set pharmacyName='%s', pharmacyCity='%s', pharmacyPhoneNum='%s' where pharmacyID= '%s' " % (pharmacyName, pharmacyCity, pharmacyPhoneNum, pharmacyID)
    
    mycursor.execute(update_pharmacy)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_update = Label(success_window, text = "Update Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_update.grid(row = 20, column = 0)



def DeletePharmacy():
    #Link SQL attributes with GUI variables
    pharmacyID = entry_pharmacyID.get()

    #Send SQL statement to database as a string
    delete_pharmacy = "Delete from pharmacy where pharmacyID = '%s';" % (pharmacyID) 
    mycursor.execute(delete_pharmacy)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_delete = Label(success_window, text = "Delete Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_delete.grid(row = 20, column = 0)



def InsertPharmacy():
    #Link SQL attributes with GUI variables
    pharmacyName = entry_pharmacyName.get()
    pharmacyCity = entry_pharmacyCity.get()
    pharmacyPhoneNum = entry_pharmacyPhoneNum.get()

    #Send SQL statement to database as a string
    insert_pharmacy = "Insert into pharmacy (pharmacyName, pharmacyCity, pharmacyPhoneNum) values ('%s', '%s', '%s');" % (pharmacyName, pharmacyCity, pharmacyPhoneNum)
    mycursor.execute(insert_pharmacy)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_insert = Label(success_window, text = "Insert Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_insert.grid(row = 20, column = 0)



def SearchPharmacy():
    #Link SQL attributes with GUI variables
    pharmacyID = entry_pharmacyID.get()

    #Send SQL statement to database as a string
    search_pharmacy = "Select * from pharmacy where pharmacyID='%s';" % (pharmacyID)
    mycursor.execute(search_pharmacy)
    pharmacy = mycursor.fetchone()
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_search = Label(success_window, text = "Pharmacy ID:   %s \n Name:    %s \n City:    %s \n  Phone:    %s \n " % (pharmacy), fg = "black", bg = "light pink", justify = LEFT)
    label_success_search.grid(row = 20, column = 0)



def PharmacyWindow():
    #Create new window to display pharmacy fields and options
    pharmacy_window = tk.Tk()
    pharmacy_window.title("Pharmacy")
    pharmacy_window.geometry = ("500x500")

   #Label to display instructions
    label_instruction = Label(pharmacy_window, text = "For Insert: Enter all fields except ID. \nFor Update: Enter all fields. \nFor Delete: Enter ID only. \nFor Search: Enter ID only. ",font = ("Courier", 10), justify = LEFT, fg = "black", bg = "light yellow")
    label_instruction.grid(row = 0, column = 0)

    #Create labels and entries for PHARMACY
    label_pharmacyID = Label(pharmacy_window, text = "Pharmacy ID",fg = "black", bg = "white")
    label_pharmacyID.grid(row = 1, column = 0, padx = 5)
    global entry_pharmacyID
    entry_pharmacyID = Entry(pharmacy_window, fg = 'black', bg = 'white', width = 10)
    entry_pharmacyID.grid(row = 2, column = 0, padx = 5)

    label_pharmacyName = Label(pharmacy_window, text = "Pharmacy Name",fg = "black", bg = "white")
    label_pharmacyName.grid(row = 3, column = 0, padx = 5)
    global entry_pharmacyName
    entry_pharmacyName = Entry(pharmacy_window, fg = 'black', bg = 'white', width = 10)
    entry_pharmacyName.grid(row = 4, column = 0, padx = 5)

    label_pharmacyCity = Label(pharmacy_window, text = "Pharmacy City",fg = "black", bg = "white")
    label_pharmacyCity.grid(row = 5, column = 0, padx = 5)
    global entry_pharmacyCity
    entry_pharmacyCity = Entry(pharmacy_window, fg = 'black', bg = 'white', width = 10)
    entry_pharmacyCity.grid(row = 6, column = 0, padx = 5)

    label_pharmacyPhoneNum = Label(pharmacy_window, text = "Pharmacy Phone Number",fg = "black", bg = "white")
    label_pharmacyPhoneNum.grid(row = 7, column = 0, padx = 5)
    global entry_pharmacyPhoneNum
    entry_pharmacyPhoneNum = Entry(pharmacy_window, fg = 'black', bg = 'white', width = 10)
    entry_pharmacyPhoneNum.grid(row = 8, column = 0, padx = 5)

    #Create a button to initiate options to insert into database
    button_insert = Button(pharmacy_window, fg = "black", bg = "light blue", text = "Insert", command = InsertPharmacy)
    button_insert.grid(row = 5, column = 8, pady = 5)

    #Create a button to initiate options to update database
    button_update = Button(pharmacy_window, fg = "black", bg = "lawn green", text = "Update", command = UpdatePharmacy)
    button_update.grid(row = 6, column = 8, pady = 5)

    #Create a button to initiate options to delete in database
    button_delete = Button(pharmacy_window, fg = "black", bg = "orange", text = "Delete", command = DeletePharmacy)
    button_delete.grid(row = 7, column = 8, pady = 5)

    #Create a button to initiate options to search in database
    button_search = Button(pharmacy_window, fg = "black", bg = "mediumpurple1", text = "Search", command = SearchPharmacy)
    button_search.grid(row = 8, column = 8, pady = 5)

######################################################
#EMERGENCY CONTACT-RELATED FUNCTIONS AND WINDOW

def UpdateContact():
    #Link SQL attributes with GUI variables
    contactID = entry_contactID.get()
    contactFname = entry_contactfname.get()
    contactLname = entry_contactLname.get()
    contactPhoneNum = entry_contactPhoneNum.get()
    contact_of = entry_contactOf.get()

   #Send SQL statement to database as a string    
    update_contact = "Update emergency_contact set contactFname='%s', contactLname='%s', contactPhoneNum='%s', contact_of = '%s'  where contactID= '%s' " % (contactFname, contactLname, contactPhoneNum, contact_of, contactID)
    mycursor.execute(update_contact)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_update = Label(success_window, text = "Update Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_update.grid(row = 20, column = 0)


def DeleteContact():
    #Link SQL attributes with GUI variables
    contactID = entry_contactID.get()

    #Send SQL statement to database as a string
    delete_contact = "Delete from emergency_contact where contactID = '%s'; " % (contactID)
    mycursor.execute(delete_contact)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_delete = Label(success_window, text = "Delete Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_delete.grid(row = 20, column = 0)



def InsertContact():
    #Link SQL attributes with GUI variables
    contactFname = entry_contactfname.get()
    contactLname = entry_contactLname.get()
    contactPhoneNum = entry_contactPhoneNum.get()
    contact_of = entry_contactOf.get()

    #Send SQL statement to database as a string    
    insert_contact = "Insert into emergency_contact (contactFname, contactLname, contactPhoneNum, contact_of) values ('%s', '%s', '%s', '%s')" % (contactFname, contactLname, contactPhoneNum, contact_of)
    mycursor.execute(insert_contact)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_insert = Label(success_window, text = "Insert Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_insert.grid(row = 20, column = 0)



def SearchContact():
    #Link SQL attributes with GUI variables
    contactID = entry_contactID.get()

    #Send SQL statement to database as a string
    search_contact = "Select * from emergency_contact where contactID='%s';" % (contactID)
    mycursor.execute(search_contact)
    contact = mycursor.fetchone()
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_search = Label(success_window, text = "Contact ID:   %s \nFirst Name:    %s \nLast Name:    %s \nPhone:    %s \nContact Of(PatientID):    %s" % (contact), fg = "black", bg = "light pink", justify = LEFT)
    label_success_search.grid(row = 20, column = 0)



def ContactWindow():
    #Create new window to display emergency contact fields and options
    contact_window = tk.Tk()
    contact_window.title("Emergency Contact")
    contact_window.geometry = ("500x500")

    #Label to display instructions
    label_instruction = Label(contact_window, text = "For Insert: Enter all fields except ID. \nFor Update: Enter all fields. \nFor Delete: Enter ID only. \nFor Search: Enter ID only. ",font = ("Courier", 10), justify = LEFT, fg = "black", bg = "light yellow")
    label_instruction.grid(row = 0, column = 0)

    #Create labels and entries for EMERGENCY CONTACTS
    label_contactID = Label(contact_window, text = "Emergency Contact ID",fg = "black", bg = "white")
    label_contactID.grid(row = 1, column = 0, padx = 5)
    global entry_contactID
    entry_contactID = Entry(contact_window, fg = 'black', bg = 'white', width = 10)
    entry_contactID.grid(row = 2, column = 0, padx = 5)

    label_contactfname = Label(contact_window, text = "Emergency Contact First Name",fg = "black", bg = "white")
    label_contactfname.grid(row = 3, column = 0, padx = 5)
    global entry_contactfname
    entry_contactfname = Entry(contact_window, fg = 'black', bg = 'white', width = 10)
    entry_contactfname.grid(row = 4, column = 0, padx = 5)

    label_contactLname = Label(contact_window, text = "Emergency Contact Last Name",fg = "black", bg = "white")
    label_contactLname.grid(row = 5, column = 0, padx = 5)
    global entry_contactLname
    entry_contactLname = Entry(contact_window, fg = 'black', bg = 'white', width = 10)
    entry_contactLname.grid(row = 6, column = 0, padx = 5)

    label_contactPhoneNum = Label(contact_window, text = "Emergency Contact Phone Number",fg = "black", bg = "white")
    label_contactPhoneNum.grid(row = 7, column = 0, padx = 5)
    global entry_contactPhoneNum
    entry_contactPhoneNum = Entry(contact_window, fg = 'black', bg = 'white', width = 10)
    entry_contactPhoneNum.grid(row = 8, column = 0, padx = 5)

    label_contactOf = Label(contact_window, text = "Emergency Contact Of (PatientID)",fg = "black", bg = "white")
    label_contactOf.grid(row = 9, column = 0, padx = 5)
    global entry_contactOf
    entry_contactOf = Entry(contact_window, fg = 'black', bg = 'white', width = 10)
    entry_contactOf.grid(row = 10, column = 0, padx = 5)

    #Create a button to initiate options to insert into database
    button_insert = Button(contact_window, fg = "black", bg = "light blue", text = "Insert", command = InsertContact)
    button_insert.grid(row = 7, column = 8, pady = 5)

    #Create a button to initiate options to update database
    button_update = Button(contact_window, fg = "black", bg = "lawn green", text = "Update", command = UpdateContact)
    button_update.grid(row = 8, column = 8, pady = 5)

    #Create a button to initiate options to delete in database
    button_delete = Button(contact_window, fg = "black", bg = "orange", text = "Delete", command = DeleteContact)
    button_delete.grid(row = 9, column = 8, pady = 5)

    #Create a button to initiate options to search in database
    button_search = Button(contact_window, fg = "black", bg = "mediumpurple1", text = "Search", command = SearchContact)
    button_search.grid(row = 10, column = 8, pady = 5)

######################################################
#LEGAL GUARDIAN-RELATED FUNCTIONS AND WINDOW


def UpdateGuardian():
    #Link SQL attributes with GUI variables
    guardianID = entry_guardianID.get()
    guardianFname = entry_guardianfname.get()
    guardianLname = entry_guardianLname.get()
    guardianPhoneNum = entry_guardianPhoneNum.get()
    guardian_of = entry_guardianOf.get()
 
    #Send SQL statement to database as a string
    update_guardian = "Update legal_guardian set guardianFname='%s', guardianLname='%s', guardianPhoneNum='%s', guardian_of = '%s' where guardianID= '%s' " % (guardianFname, guardianLname, guardianPhoneNum, guardian_of, guardianID)
    mycursor.execute(update_guardian)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_update = Label(success_window, text = "Update Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_update.grid(row = 20, column = 0)


def DeleteGuardian():
    #Link SQL attributes with GUI variables
    guardianID = entry_guardianID.get()

    #Send SQL statement to database as a string
    delete_guardian = "Delete from legal_guardian where guardianID= '%s';" % (guardianID)
    mycursor.execute(delete_guardian)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_delete = Label(success_window, text = "Delete Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_delete.grid(row = 20, column = 0)


def InsertGuardian():
    #Link SQL attributes with GUI variables
    guardianFname = entry_guardianfname.get()
    guardianLname = entry_guardianLname.get()
    guardianPhoneNum = entry_guardianPhoneNum.get()
    guardian_of = entry_guardianOf.get()

    #Send SQL statement to database as a string
    insert_guardian = "Insert into legal_guardian (guardianFname, guardianLname, guardianPhoneNum, guardian_of) values ('%s', '%s', '%s', '%s');" % (guardianFname, guardianLname, guardianPhoneNum, guardian_of)
    mycursor.execute(insert_guardian)
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_insert = Label(success_window, text = "Insert Successful! You may close this window.",fg = "black", bg = "light pink")
    label_success_insert.grid(row = 20, column = 0)



def SearchGuardian():
    #Link SQL attributes with GUI variables
    guardianID = entry_guardianID.get()

    #Send SQL statement to database as a string
    search_guardian = "Select * from legal_guardian where guardianID='%s';" % (guardianID)
    mycursor.execute(search_guardian)
    guardian = mycursor.fetchone()
    db.commit()

    #Create window and message to display success to the user
    success_window = tk.Tk()
    success_window.title("Success")
    success_window.geometry = ("300x300")

    label_success_search = Label(success_window, text = "Legal Guardian ID:   %s \n First Name:    %s \n Last Name:    %s \n  Phone:    %s \nGuardian Of (PatientID):     %s\n" % (guardian), fg = "black", bg = "light pink", justify = LEFT)
    label_success_search.grid(row = 20, column = 0)



def GuardianWindow():
    #Create new window to display legal guardian fields and options
    guardian_window = tk.Tk()
    guardian_window.title("Legal Guardian")
    guardian_window.geometry = ("500x500")

    #Label to display instructions
    label_instruction = Label(guardian_window, text = "For Insert: Enter all fields except ID. \nFor Update: Enter all fields. \nFor Delete: Enter ID only. \nFor Search: Enter ID only. ",font = ("Courier", 10), justify = LEFT, fg = "black", bg = "light yellow")
    label_instruction.grid(row = 0, column = 0)

    #Create labels and entries for LEGAL GUARDIAN

    label_guardianID = Label(guardian_window, text = "Legal Guardian ID",fg = "black", bg = "white")
    label_guardianID.grid(row = 1, column = 0, padx = 5)
    global entry_guardianID
    entry_guardianID = Entry(guardian_window, fg = 'black', bg = 'white', width = 10)
    entry_guardianID.grid(row = 2, column = 0, padx = 5)

    label_guardianfname = Label(guardian_window, text = "Legal Guardian First Name",fg = "black", bg = "white")
    label_guardianfname.grid(row = 3, column = 0, padx = 5)
    global entry_guardianfname
    entry_guardianfname = Entry(guardian_window, fg = 'black', bg = 'white', width = 10)
    entry_guardianfname.grid(row = 4, column = 0, padx = 5)

    label_guardianLname = Label(guardian_window, text = "Legal Guardian Last Name",fg = "black", bg = "white")
    label_guardianLname.grid(row = 5, column = 0, padx = 5)
    global entry_guardianLname
    entry_guardianLname = Entry(guardian_window, fg = 'black', bg = 'white', width = 10)
    entry_guardianLname.grid(row = 6, column = 0, padx = 5)

    label_guardianPhoneNum = Label(guardian_window, text = "Legal Guardian Phone Number",fg = "black", bg = "white")
    label_guardianPhoneNum.grid(row = 7, column = 0, padx = 5)
    global entry_guardianPhoneNum
    entry_guardianPhoneNum = Entry(guardian_window, fg = 'black', bg = 'white', width = 10)
    entry_guardianPhoneNum.grid(row = 8, column = 0, padx = 5)

    label_guardianOf = Label(guardian_window, text = "Legal Guardian Of (PatientID)",fg = "black", bg = "white")
    label_guardianOf.grid(row = 9, column = 0, padx = 5)
    global entry_guardianOf
    entry_guardianOf = Entry(guardian_window, fg = 'black', bg = 'white', width = 10)
    entry_guardianOf.grid(row = 10, column = 0, padx = 5)

    #Create a button to initiate options to insert into database
    button_insert = Button(guardian_window, fg = "black", bg = "light blue", text = "Insert", command = InsertGuardian)
    button_insert.grid(row = 7, column = 8, pady = 5)

    #Create a button to initiate options to update database
    button_update = Button(guardian_window, fg = "black", bg = "lawn green", text = "Update", command = UpdateGuardian)
    button_update.grid(row = 8, column = 8, pady = 5)

    #Create a button to initiate options to delete in database
    button_delete = Button(guardian_window, fg = "black", bg = "orange", text = "Delete", command = DeleteGuardian)
    button_delete.grid(row = 9, column = 8, pady = 5)

    #Create a button to initiate options to search in database
    button_search = Button(guardian_window, fg = "black", bg = "mediumpurple1", text = "Search", command = SearchGuardian)
    button_search.grid(row = 10, column = 8, pady = 5)

   
#################################
#Main Function
    
if __name__ == '__main__':

    import mysql.connector
    
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "77OILCsc!614",
        database = "patient_relationships_db"
        )

    mycursor = db.cursor()

    from tkinter import *
    import tkinter as tk
    
    MainWindow()

