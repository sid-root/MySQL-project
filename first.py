from tkinter import *
import csv
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

_root = Tk()
_root.title =("Quarantine facility Database")
_root.geometry("400x500")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "iamherono1",
    database = "testdb"
)

mycursor = mydb.cursor()

# DATABASE CREATION :-

# mycursor.execute("CREATE TABLE IF NOT EXISTS patients (\
#         name VARCHAR(255),\
#         age INTEGER(10),\
#         contact VARCHAR(255),\
#         address VARCHAR(255),\
#         email VARCHAR(255),\
#         p_id INT(25 ) ,\
#         dob INT(8),\
#         nationality VARCHAR(255),\
#         qcenterNo INT(10), PRIMARY KEY (p_id))")
#
# mycursor.execute("SHOW TABLES")
#
# for tb in mycursor:
#     print(tb)
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS qcentre (\
#         centre_no INTEGER(10),\
#         centre_name VARCHAR(255),\
#         no_of_rooms INTEGER(10),\
#         centre_address VARCHAR(255),\
#         centre_owner_id INTEGER(10),\
#         centre_incharge_id INTEGER(10),\
#         sanitation_facility_no INTEGER(10), PRIMARY KEY (centre_no))")
#
# mycursor.execute("ALTER TABLE patients\
#                 ADD FOREIGN KEY (qcenterNo) REFERENCES qcentre(centre_no)")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS district_collector(office_no INTEGER(10), name VARCHAR(255), email VARCHAR(255))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS medical_staff(staff_no INTEGER(10) NOT NULL, address VARCHAR(255), city VARCHAR(255), dob INTEGER(8), age INTEGER(10), quarantine_centre_no INTEGER(10), PRIMARY KEY (staff_no))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS doctors(doc_id INTEGER(10) NOT NULL, name VARCHAR(255), contact_no INTEGER(10), email_id VARCHAR(255), FOREIGN KEY (doc_id) REFERENCES medical_staff(staff_no))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS cmo(cmo_no INTEGER(10) NOT NULL, name VARCHAR(255), contact_no INTEGER(10), email_id VARCHAR(255), FOREIGN KEY (cmo_no) REFERENCES medical_staff(staff_no))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS patient_travel_history(p_id INTEGER(25) NOT NULL, city_pincode INTEGER(6) NOT NULL, city VARCHAR(255), no_of_days_of_travel INTEGER(4), FOREIGN KEY (p_id) REFERENCES patients(p_id))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS co_travellers(p_id INTEGER(25) NOT NULL, city_pincode INTEGER(6) NOT NULL, contact_no INTEGER(10), FOREIGN KEY (p_id) REFERENCES patients(p_id))")
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS patient_med_rec(p_id INTEGER(25) NOT NULL, covid_comorbidity VARCHAR(500), covid_test_date INTEGER(8), covid_retest_date INTEGER(8), allergies VARCHAR(255), status VARCHAR(50), FOREIGN KEY (p_id) REFERENCES patients(p_id))")
#
# mycursor.execute("ALTER TABLE medical_staff\
#                 ADD FOREIGN KEY (quarantine_centre_no) REFERENCES qcentre(centre_no)")

describe = StringVar()

def describe_submit():
    if(describe.get() == "1"):
        _login = Tk()
        _login.title = ("Login")
        _login.geometry("1920x1080")

        def main_window1():
            curr_pid = pid_box.get()
            curr_pid = (curr_pid,)

            sqlcmd = "SELECT name,age,contact,address,pincode,email,patients.p_id,dob,nationality,qcenterNo,covid_comorbidity,covid_test_date,covid_retest_date,allergies,status FROM patients,patient_med_rec WHERE patients.p_id = %s AND patient_med_rec.p_id=patients.p_id"
            result = mycursor.execute(sqlcmd,curr_pid)
            result = mycursor.fetchall()
            if not result :
                text = "Please Enter Valid Credentials"
                lab = Label(_login, text = text, fg="Red")
                lab.place(x=130, y=100)
            else:
                myinfo = Tk()
                myinfo.geometry("1920x1080")
                myinfo.title("My Information")
                sqlcmd = "SELECT * FROM patient_med_rec WHERE p_id = %s"
                res = mycursor.execute(sqlcmd,curr_pid)
                res = mycursor.fetchall()

                heading_1 = Label(myinfo, text="Name", font=("Cambria"), fg="white", bg="black").grid(row=0, column=0, padx=3)
                heading_2 = Label(myinfo, text="Age", font=("Cambria"), fg="white", bg="black").grid(row=0, column=1, padx=3)
                heading_3 = Label(myinfo, text="Contact no", font=("Cambria"), fg="white", bg="black").grid(row=0, column=2,
                                                                                                            padx=3)
                heading_4 = Label(myinfo, text="Address", font=("Cambria"), fg="white", bg="black").grid(row=0, column=3, padx=3)
                heading_10 = Label(myinfo, text="Pincode", font=("Cambria"), fg="white", bg="black").grid(row=0, column=4, padx=3)
                heading_5 = Label(myinfo, text="Email", font=("Cambria"), fg="white", bg="black").grid(row=0, column=5, padx=3)
                heading_6 = Label(myinfo, text="P_ID", font=("Cambria"), fg="white", bg="black").grid(row=0, column=6, padx=3)
                heading_7 = Label(myinfo, text="D.O.B", font=("Cambria"), fg="white", bg="black").grid(row=0, column=7, padx=3)
                heading_8 = Label(myinfo, text="Nationality", font=("Cambria"), fg="white", bg="black").grid(row=0, column=8,
                                                                                                             padx=3)
                heading_9 = Label(myinfo, text="Qcenter No", font=("Cambria"), fg="white", bg="black").grid(row=0, column=9,
                                                                                                            padx=3)

                # pidlabel = Label(myinfo,text="Patient Id",font=("Cambria"), fg="white", bg="black")
                # pidlabel.grid(row=0,column=10,padx=10)
                comorblabel = Label(myinfo,text="Covid Comorbities",font=("Cambria"), fg="white", bg="black")
                comorblabel.grid(row=0,column=10,padx=10)
                testdatelab = Label(myinfo,text="Covid Test Date",font=("Cambria"), fg="white", bg="black")
                retstdatelab = Label(myinfo,text="Covid Retest Date",font=("Cambria"), fg="white", bg="black")
                alrglab = Label(myinfo,text="Allergies",font=("Cambria"), fg="white", bg="black")
                statuslab = Label(myinfo,text="Status",font=("Cambria"), fg="white", bg="black")

                testdatelab.grid(row=0,column=11,padx=3)
                retstdatelab.grid(row=0,column=12,padx=3)
                alrglab.grid(row=0,column=13,padx=3)
                statuslab.grid(row=0,column=14,padx=3)

                n=0

                for index,x in enumerate(result):
                    n=0
                    for y in x:
                        lab1 = Label(myinfo, text = y)
                        lab1.grid(row = index+1, column = n, padx = 10)
                        n=n+1
                index=index+2

                # p=n
                # for i,x in enumerate(res):
                #     n=0
                #     for y in x:
                #         lab1 = Label(myinfo, text = y)
                #         lab1.grid(row = i+1, column = p+n, padx = 10)
                #         n=n+1

        l=Label(_login,text="Please Fill Your Credentials", font = ("Arial",20)).pack()
        pid_label = Label(_login, text="Your Id: ", font = ("Arial", 16)).place(x=70,y=150)
        name_label = Label(_login, text="Your Name: ", font = ("Arial", 16)).place(x=70, y=250)

        pid_box = Entry(_login)
        pid_box.place(x=200, y=155)
        _name_box = Entry(_login).place(x=200,y=255)

        login = Button(_login,text="Login",command = main_window1).place(x=200, y=325)

    if(describe.get() == "2"):
        _login = Tk()
        _login.title = ("Login")
        _login.geometry("1920x1080")



        def main_window2():

            def forward1():
                root = Tk()
                root.geometry("1920x1080")
                title_label = Label(root, text="QARANTINE FACILITY", font=("Helvetica 16 bold italic"), fg="white", bg="black")
                title_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10)
                # fprm_label=Label(root,text="Patient form", font=("Cambria,12)")).grid(row=0,column=3)

                # def add_patients():
                #     sql_command1 = "INSERT INTO patients (name, age, contact, address, pincode, email, p_id, dob, nationality, qcenterNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                #     values1 = (name_box.get(), age_box.get(), contact_box.get(), address_box.get(),pincode_box.get(), email_box.get(), p_id_box.get(), dob_box.get(),nationality_box.get(), qcenterNo_box.get())
                #     mycursor.execute(sql_command1, values1)
                #     # commiting to the database
                #     mydb.commit()
                #
                #     sql_command2 = "INSERT INTO patient_med_rec (p_id, allergies, status, covid_test_date, covid_retest_date, covid_comorbidity) VALUES (%s, %s, %s, %s, %s, %s)"
                #     values2 = (p_id_box.get(), allergies_box.get(), status_box.get(),testdate_box.get(), retestdate_box.get(), covid_comor_box.get())
                #     mycursor.execute(sql_command2, values2)
                #     # commiting to the database
                #     mydb.commit()
                #
                #     if(lastpin_box.get() == ""):
                #         lastpin = None
                #     else:
                #         lastpin = int(lastpin_box.get())
                #
                #     sql_command3 = "INSERT INTO patient_travel_history (p_id, city, city_pincode, cotrav_contact, no_of_days_of_travel) VALUES (%s, %s, %s, %s, %s)"
                #     values3 = (p_id_box.get(), lastcity_box.get(), lastpin, cotravellers_contact_box.get(), days_visited_box.get())
                #     mycursor.execute(sql_command3, values3)
                #     # commiting to the database
                #     mydb.commit()

                def list_patients():
                    list_patients_query = Tk()
                    list_patients_query.title("List all patients")
                    list_patients_query.geometry("1920x1080")
                    list_patients_query.configure(bg='black')

                    # QUERY THE DATABASE
                    mycursor.execute("SELECT name,age,contact,address,pincode,email,patients.p_id,dob,nationality,qcenterNo,covid_comorbidity,covid_test_date,covid_retest_date,allergies,status FROM patients,patient_med_rec WHERE patients.p_id= patient_med_rec.p_id AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)",(cmono_box.get(),))
                    result = mycursor.fetchall()

                    heading_1 = Label(list_patients_query, text="Name", font=("Cambria"), fg="white", bg="black").grid(row=0, column=0, padx=3)
                    heading_2 = Label(list_patients_query, text="Age", font=("Cambria"), fg="white", bg="black").grid(row=0, column=1, padx=3)
                    heading_3 = Label(list_patients_query, text="Contact no", font=("Cambria"), fg="white", bg="black").grid(row=0, column=2,
                                                                                                                padx=3)
                    heading_4 = Label(list_patients_query, text="Address", font=("Cambria"), fg="white", bg="black").grid(row=0, column=3, padx=3)
                    heading_10 = Label(list_patients_query, text="Pincode", font=("Cambria"), fg="white", bg="black").grid(row=0, column=4, padx=3)
                    heading_5 = Label(list_patients_query, text="Email", font=("Cambria"), fg="white", bg="black").grid(row=0, column=5, padx=3)
                    heading_6 = Label(list_patients_query, text="P_ID", font=("Cambria"), fg="white", bg="black").grid(row=0, column=6, padx=3)
                    heading_7 = Label(list_patients_query, text="D.O.B", font=("Cambria"), fg="white", bg="black").grid(row=0, column=7, padx=3)
                    heading_8 = Label(list_patients_query, text="Nationality", font=("Cambria"), fg="white", bg="black").grid(row=0, column=8,
                                                                                                                 padx=3)
                    heading_9 = Label(list_patients_query, text="Qcenter No", font=("Cambria"), fg="white", bg="black").grid(row=0, column=9,
                                                                                                                padx=3)
                    heading_10 = Label(list_patients_query, text="Covid Comorbidity", font=("Cambria"), fg="white", bg="black").grid(row=0, column=10, padx=3)
                    heading_11 = Label(list_patients_query, text="Covid Test Date", font=("Cambria"), fg="white", bg="black").grid(row=0, column=11, padx=3)
                    heading_12 = Label(list_patients_query, text="Covid Retest Date", font=("Cambria"), fg="white", bg="black").grid(row=0, column=12, padx=3)
                    heading_13 = Label(list_patients_query, text="Allergies", font=("Cambria"), fg="white", bg="black").grid(row=0, column=13, padx=3)
                    heading_14 = Label(list_patients_query, text="Status", font=("Cambria"), fg="white", bg="black").grid(row=0, column=14, padx=3)


                    index=0
                    for index, x in enumerate(result):
                        num = 0
                        for y in x:
                            lookup_label = Label(list_patients_query, text=y, fg="white", bg="black")
                            lookup_label.grid(row=index + 1, column=num, padx=10)
                            num += 1
                    csv_button = Button(list_patients_query, text="Save to excel", command=lambda: write_to_csv(result), bg="#00FF66")
                    csv_button.grid(row= index + 2, column=0)

                    h = Scrollbar(list_patients_query, orient = 'horizontal')
                    h.grid(row=index+4,sticky="ns")

                    return

                def search_patients():

                    search_patients_query = Tk()
                    search_patients_query.title("List all patients")
                    search_patients_query.geometry("1920x1080")
                    global frame
                    frame = Frame(search_patients_query)
                    frame.grid(row=5,column=6)
                    global test_label
                    global searched_label
                    searched_label = Label(search_patients_query)
                    test_label = Label(search_patients_query)

                    def setframe():
                        global frame
                        frame = Frame(search_patients_query)
                        frame.grid(row=5,column=6)

                    def clear_scr():
                        frame.destroy()
                        searched_label.destroy()
                        test_label.destroy()
                        search_button['state'] = NORMAL
                        setframe()

                    def search_now():
                        selected = drop.get()

                        sql =""

                        allorcom = 0

                        if selected == "Search by...":

                            test_label = Label(search_patients_query,text="Please select a criteria")
                            test_label.grid(row=7,column=0)

                        if selected == "Name":

                            sql = "SELECT * FROM patients WHERE name = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Email":

                            sql = "SELECT * FROM patients WHERE email = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Age":

                            sql = "SELECT * FROM patients WHERE age = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Contact no":

                            sql = "SELECT * FROM patients WHERE contact = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Pincode":

                            sql = "SELECT * FROM patients WHERE pincode = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Patient ID":
                            sql = "SELECT * FROM patients WHERE p_id = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Nationality":
                            sql = "SELECT * FROM patients WHERE nationality = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Q-Center No":
                            sql = "SELECT * FROM patients WHERE qcenterNo = %s AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"

                        if selected == "Allergies":
                            sql = "SELECT * FROM patients,patient_med_rec WHERE patient_med_rec.p_id=patients.p_id AND patient_med_rec.allergies LIKE %s  AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"
                            allorcom = 1

                        if selected == "Covid Comorbidities":
                            sql = "SELECT * FROM patients,patient_med_rec WHERE patient_med_rec.p_id=patients.p_id AND patient_med_rec.covid_comorbidity LIKE %s  AND qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id = %s)"
                            allorcom = 1

                        if(allorcom==0) :
                            searched = search_box.get()
                            centre_inchargeid = cmono_box.get()
                            #sql ="SELECT * FROM patients WHERE name = %s"

                        else:
                            searched = search_box.get()
                            centre_inchargeid = cmono_box.get()
                            searched = '%' + searched + '%'

                        search = searched
                        name = (searched,centre_inchargeid,)
                        result = mycursor.execute(sql, name)
                        result = mycursor.fetchall()

                        global searched_label
                        searched_label = Label(search_patients_query)
                        if not selected == "Search by...":
                            if (not result) or (search == "%%"):

                                result = 'Record not found...'
                                searched_label = Label(frame, text=result, fg="Red")
                                searched_label.grid(row=5, column=2, padx=10)
                            else:

                                val = ""
                                for index, x in enumerate(result):
                                    num = 1
                                    for y in x:
                                        val += str(y)
                                        searched_label = Label(frame, text=y, fg="Black")
                                        searched_label.grid(row=index + 4, column=num, padx=10)
                                        num += 1
                                    val = val + "\n"

                                #print(val)

                        #searched_label = Label(search_patients_query, text=val, fg="Black")
                        #searched_label.grid(row= 4, column=1, padx=10,columnspan=2)
                        search_box.delete(0, END)
                        search_button['state'] = DISABLED
                    #Entry box to search
                    search_box = Entry(search_patients_query)
                    search_box.grid(row=0,column=1,padx=10,pady=10)

                    #Search box Label
                    search_label = Label(search_patients_query,text="Search")
                    search_label.grid(row=0,column=0,padx=10,pady=10)

                    #Search button
                    search_button = Button(search_patients_query,text="Search patients", command=search_now)
                    search_button.grid(row=1 ,column=0,padx=10,ipadx=30)

                    #Drop down box
                    drop = ttk.Combobox(search_patients_query, value=["Search by...", "Name", "Email", "Age", "Contact no", "Pincode", "Patient ID", "Nationality", "Q-Center No","Allergies","Covid Comorbidities"])
                    drop.current(0)
                    drop.grid(row=0,column=2)

                    #Clear screen button
                    clr_scr = Button(search_patients_query,text="Clear Screen",command= clear_scr)
                    clr_scr.grid(row=4, column=0, padx=10, ipadx=38)

                    return

                def clear_fields():
                    name_box.delete(0, END)
                    age_box.delete(0, END)
                    contact_box.delete(0, END)
                    address_box.delete(0, END)
                    pincode_box.delete(0, END)
                    email_box.delete(0, END)
                    p_id_box.delete(0, END)
                    dob_box.delete(0, END)
                    nationality_box.delete(0, END)
                    qcenterNo_box.delete(0, END)

                    allergies_box.delete(0, END)
                    status_box.delete(0, END)
                    testdate_box.delete(0, END)
                    retestdate_box.delete(0, END)
                    covid_comor_box.delete(0, END)
                    lastcity_box.delete(0, END)
                    lastpin_box.delete(0, END)
                    cotravellers_contact_box.delete(0, END)
                    days_visited_box.delete(0, END)

                def delete_patients():
                    delpat = Tk()
                    delpat.title("Delete Patients")
                    delpat.geometry("1920x1080")
                    global frame3
                    frame3=Frame(delpat)
                    frame3.grid(row=7,column=8)

                    def setframe():
                        global frame3
                        frame3 = Frame(delpat)
                        frame3.grid(row=7,column=8)

                    def clrscr():
                        delbut['state']=NORMAL
                        frame3.destroy()
                        setframe()

                    def delete():
                        delbut['state']=DISABLED
                        pid=pidentry.get()
                        sqlcmd="SELECT p_id FROM patients WHERE p_id = %s AND p_id IN (SELECT p_id WHERE qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id=%s))"
                        res0 = mycursor.execute(sqlcmd,(pid,cmono_box.get()))
                        res0=mycursor.fetchall()

                        if not res0:
                            result = 'Record not found...'
                            lab = Label(frame3, text=result, fg="Red")
                            lab.grid(row=10, column=8, padx=10)

                        else:
                            sqlcmd0 = "DELETE FROM patients WHERE p_id=%s"
                            sqlcmd1 = "DELETE FROM patient_med_rec WHERE p_id=%s"
                            sqlcmd2 = "DELETE FROM patient_travel_history WHERE p_id=%s"

                            mycursor.execute(sqlcmd1,(pid,))
                            mydb.commit()
                            mycursor.execute(sqlcmd2,(pid,))
                            mydb.commit()
                            mycursor.execute(sqlcmd0,(pid,))
                            mydb.commit()

                    dpidlab = Label(delpat,text="Id of Patient to be Deleted:")
                    dpidlab.grid(row=4,column=6,padx=10,pady=10)

                    pidentry = Entry(delpat)
                    pidentry.grid(row=4,column=7,padx=10,pady=10)

                    delbut = Button(delpat,text="Delete",command=delete)
                    delbut.grid(row=6,column=6,pady=10)

                    clrscr = Button(delpat,text = "Clear Screen", command=clrscr)
                    clrscr.grid(row=7,column=6,pady=10)

                def update_patients():
                    up = Tk()
                    up.title("Update Patients")
                    up.geometry("1920x1080")
                    global fr
                    fr = Frame(up)
                    fr.grid(row=9,column=9)

                    def setframe():
                        global fr
                        fr = Frame(up)
                        fr.grid(row=9,column=9)

                    def clear():
                        updatebut['state'] = NORMAL
                        fr.destroy()
                        setframe()

                    def update():
                        updatebut['state'] = DISABLED
                        pid=pidentry.get()
                        # pid=(pid,)
                        state=""
                        sqlcmd="SELECT p_id FROM patients WHERE p_id = %s AND p_id IN (SELECT p_id WHERE qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id=%s))"
                        res0=mycursor.execute(sqlcmd,(pid,cmono_box.get()))
                        res0=mycursor.fetchall()

                        if not res0 or updrop.get()=="Update..." or value.get()=="":
                            text = "Please Enter Valid Credentials"
                            lab = Label(fr, text = text, fg="Red")
                            lab.grid()

                        else:
                            text = "Update Query Executed"
                            lab = Label(fr, text = text, fg="Red")
                            lab.grid()

                            select = updrop.get()
                            if select == "Name":
                                col="name"
                                col=(col,)
                                sqlcmd1 = "UPDATE patients SET name = %s WHERE p_id=%s"

                            if select == "Email":
                                col = "email"
                                col=(col,)
                                sqlcmd1 = "UPDATE patients SET email = %s WHERE p_id=%s"

                            if select == "Age":
                                col = "age"
                                col=(col,)
                                sqlcmd1 = "UPDATE patients SET age = %s WHERE p_id=%s"

                            if select == "Contact No":
                                col = "contact"
                                col = (col,)
                                sqlcmd1 = "UPDATE patients SET %s = %s WHERE p_id=%s"

                            if select == "Pincode":
                                col="pincode"
                                col=(col,)
                                sqlcmd1 = "UPDATE patients SET pincode = %s WHERE p_id=%s"

                            if select == "Status":
                                col = "status"
                                col = (col,)
                                sqlcmd1 = "UPDATE patient_med_rec SET status = %s WHERE p_id=%s"

                            if select == "Covid Test Date":
                                col = "covid_test_date"
                                col = (col,)
                                sqlcmd1 = "UPDATE patient_med_rec SET covid_test_date = %s WHERE p_id=%s"

                            if select == "Covid Retest Date":
                                col = "covid_retest_date"
                                col=(col,)
                                sqlcmd1 = "UPDATE patient_med_rec SET covid_retest_date = %s WHERE p_id=%s"

                            if select == "Covid Comorbidities":
                                col = "covid_comorbidity"
                                col=(col,)
                                sqlcmd1 = "UPDATE patient_med_rec SET covid_comorbidity = %s WHERE p_id=%s"

                            if select == "Allergies":
                                col = "allergies"
                                col=(col,)
                                sqlcmd1 = "UPDATE patient_med_rec SET allergies = %s WHERE p_id=%s"

                            res1=mycursor.execute(sqlcmd1,(value.get(),pid))
                            mydb.commit()
                            res1=mycursor.fetchall()
                            cmd="SELECT * FROM patients"
                            mycursor.execute(cmd)
                            res2=mycursor.fetchall()
                            print(res2[1][0])

                    pidlab = Label(up,text="Patient Id")
                    pidlab.grid(row=3,column=6,pady=10,padx=10)
                    pidentry = Entry(up)
                    pidentry.grid(row=3,column=7,pady=10,padx=10)

                    valuelab = Label(up,text="Update Value:")
                    valuelab.grid(row=4,column=6,padx=10)

                    value = Entry(up)
                    value.grid(row=4,column=7,padx=10)

                    updrop = ttk.Combobox(up, value=["Update...", "Name", "Email", "Age", "Contact No", "Pincode","Status", "Covid Test Date", "Covid Retest Date", "Covid Comorbidities", "Allergies"])
                    updrop.current(0)
                    updrop.grid(row=4,column=8,padx=10)

                    updatebut = Button(up,text="Update",command=update)
                    updatebut.grid(row=6,column=6,pady=6)

                    clrbut = Button(up,text="Clear Screen",command = clear)
                    clrbut.grid(row=7,column=6,pady=10)

                # Creating data to fill form
                # name_label = Label(root, text="Name*", fg="white", bg="black").grid(row=1, column=0, sticky=W, padx=10)
                # age_label = Label(root, text="Age*", fg="white", bg="black").grid(row=2, column=0, sticky=W, padx=10)
                # contact_label = Label(root, text="Contact no*", fg="white", bg="black").grid(row=3, column=0, sticky=W, padx=10)
                # address_label = Label(root, text="Address*", fg="white", bg="black").grid(row=4, column=0, sticky=W, padx=10)
                # pincode_label = Label(root, text="pincode*", fg="white", bg="black").grid(row=5, column=0, sticky=W, padx=10)
                # email_label = Label(root, text="Email id", fg="white", bg="black").grid(row=6, column=0, sticky=W, padx=10)
                # p_id_label = Label(root, text="patient_ID*", fg="white", bg="black").grid(row=7, column=0, sticky=W, padx=10)
                # dob_label = Label(root, text="D.O.B (DDMMYYYY)*", fg="white", bg="black").grid(row=8, column=0, sticky=W, padx=10)
                # nationality_label = Label(root, text="NATIONALITY*", fg="white", bg="black").grid(row=9, column=0, sticky=W, padx=10)
                # qcenterNo_label = Label(root, text="Q-Center No*", fg="white", bg="black").grid(row=10, column=0, sticky=W, padx=10)
                #
                #
                # allergies_label =Label(root, text="Allergies", fg="white", bg="black").grid(row=1, column=2, sticky=W, padx=10)
                # covid_comor_label =Label(root, text="Covid comorbidities", fg="white", bg="black").grid(row=2, column=2, sticky=W, padx=10)
                # testdate = Label(root, text="Test date*", fg="white", bg="black").grid(row=3, column=2, sticky=W, padx=10)
                # retestdate = Label(root, text="Retest date*", fg="white", bg="black").grid(row=4, column=2, sticky=W, padx=10)
                # Status = Label(root, text="Status", fg="white", bg="black").grid(row=5, column=2, sticky=W, padx=10)
                #
                # city_visited_name_label = Label(root, text="Last City Visited", fg="white", bg="black").grid(row=6, column=2, sticky=W, padx=10)
                # city_visited_pin_label = Label(root, text="Pincode of place visited", fg="white", bg="black").grid(row=7, column=2, sticky=W, padx=10)
                # cotravellers_contact_label = Label(root, text="Cotravellers' contact", fg="white", bg="black").grid(row=8, column=2, sticky=W, padx=10)
                # no_of_days_label = Label(root, text="No of days visited", fg="white", bg="black").grid(row=9, column=2, sticky=W, padx=10)
                # # Creating entry boxes
                #
                # name_box = Entry(root, bg="#B0C4DE")
                # name_box.grid(row=1, column=1, pady=5, ipadx=30)
                #
                # age_box = Entry(root, bg="#B0C4DE")
                # age_box.grid(row=2, column=1, pady=5, ipadx=30)
                #
                # contact_box = Entry(root, bg="#B0C4DE")
                # contact_box.grid(row=3, column=1, pady=5, ipadx=30)
                #
                # address_box = Entry(root, bg="#B0C4DE")
                # address_box.grid(row=4, column=1, pady=5, ipadx=30)
                #
                # pincode_box = Entry(root, bg="#B0C4DE")
                # pincode_box.grid(row=5, column=1, pady=5, ipadx=30)
                #
                # email_box = Entry(root, bg="#B0C4DE")
                # email_box.grid(row=6, column=1, pady=5, ipadx=30)
                #
                # p_id_box = Entry(root, bg="#B0C4DE")
                # p_id_box.grid(row=7, column=1, pady=5, ipadx=30)
                #
                # dob_box = Entry(root, bg="#B0C4DE")
                # dob_box.grid(row=8, column=1, pady=5, ipadx=30)
                #
                # nationality_box = Entry(root, bg="#B0C4DE")
                # nationality_box.grid(row=9, column=1, pady=5, ipadx=30)
                #
                # qcenterNo_box = Entry(root, bg="#B0C4DE")
                # qcenterNo_box.grid(row=10, column=1, pady=5, ipadx=30)
                #
                # allergies_box = Entry(root, bg="#B0C4DE")
                # allergies_box.grid(row=1, column=3, pady=5, ipadx=30)
                # covid_comor_box = Entry(root, bg="#B0C4DE")
                # covid_comor_box.grid(row=2, column=3, pady=5, ipadx=30)
                #
                # testdate_box = Entry(root, bg="#B0C4DE")
                # testdate_box.grid(row=3, column=3, pady=5, ipadx=30)
                # retestdate_box = Entry(root, bg="#B0C4DE")
                # retestdate_box.grid(row=4, column=3, pady=5, ipadx=30)
                # status_box = Entry(root, bg="#B0C4DE")
                # status_box.grid(row=5, column=3, pady=5, ipadx=30)
                # lastcity_box = Entry(root, bg="#B0C4DE")
                # lastcity_box.grid(row=6, column=3, pady=5, ipadx=30)
                # lastpin_box = Entry(root, bg="#B0C4DE")
                # lastpin_box.grid(row=7, column=3, pady=5, ipadx=30)
                # cotravellers_contact_box = Entry(root, bg="#B0C4DE")
                # cotravellers_contact_box.grid(row=8, column=3, pady=5, ipadx=30)
                # days_visited_box = Entry(root, bg="#B0C4DE")
                # days_visited_box.grid(row=9, column=3, pady=5, ipadx=30)
                #
                # # Create Buttons
                # add_patient_button = Button(root, text="Add patient to database!", command=add_patients, bg="#0198E1", fg="White")
                # add_patient_button.grid(row=11, column=0, padx=10, pady=10)
                #
                # clear_fields_button = Button(root, text="Clear Fields", command=clear_fields, bg="#CD0000", fg="White")
                # clear_fields_button.grid(row=11, column=1, padx=10)

                list_patients_button = Button(root, text="List patients", command=list_patients, bg="#00FF66")
                list_patients_button.grid(row=12, column=0, sticky=W, padx=10,pady=10)

                totalpatlab = Label(root,text = "Total Patients In Your Centre: ", font=("Arial",15))
                totalpatlab.grid(row=15,column=7,padx=10,pady=10)

                sql = "SELECT COUNT(p_id) FROM patients WHERE p_id IN (SELECT p_id WHERE qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id=%s))"
                mycursor.execute(sql,(cmono_box.get(),))
                total = mycursor.fetchall()
                total = str(total[0][0])
                totallab = Label(root,text = total, font=("Arial",15))
                totallab.grid(row=15,column=8,padx=10,pady=10)

                updatepat_but = Button(root,text="Update Patients", command=update_patients)
                updatepat_but.grid(row=13,column=0,pady=10)

                delete_but = Button(root,text="Delete Patients", command=delete_patients)
                delete_but.grid(row=13,column=1,padx=10,pady=10)

                # search patients
                search_patients_button = Button(root, text="Search patients", command=search_patients)
                search_patients_button.grid(row=12, column=1, sticky=W, padx=10)

            def forward2():
                cdocs = Tk()
                cdocs.title("Check Doctors")
                cdocs.geometry("1920x1080")

                cmd = "SELECT doc_id,name,contact_no,email_id,address,city,dob,age,quarantine_centre_no FROM doctors,medical_staff WHERE doctors.doc_id=medical_staff.staff_no AND medical_staff.quarantine_centre_no IN (SELECT centre_no FROM qcentre WHERE centre_incharge_id=%s)"
                mycursor.execute(cmd,(cmono_box.get(),))
                res=mycursor.fetchall()
                lab1=Label(cdocs,text="Doctor Id").grid(row=1,column=1,padx=10,pady=10)
                lab1=Label(cdocs,text="Doctor Name").grid(row=1,column=2,padx=10,pady=10)
                lab1=Label(cdocs,text="Contact No").grid(row=1,column=3,padx=10,pady=10)
                lab1=Label(cdocs,text="Email Id").grid(row=1,column=4,padx=10,pady=10)
                lab1=Label(cdocs,text="Address").grid(row=1,column=5,padx=10,pady=10)
                lab1=Label(cdocs,text="City").grid(row=1,column=6,padx=10,pady=10)
                lab1=Label(cdocs,text="DOB").grid(row=1,column=7,padx=10,pady=10)
                lab1=Label(cdocs,text="Age").grid(row=1,column=8,padx=10,pady=10)
                lab1=Label(cdocs,text="Quarantine Centre No").grid(row=1,column=9,padx=10,pady=10)

                print(res)
                if not res:
                    pass
                else:
                    i=0
                    for x in res:
                        i+=1
                        n=1
                        print(x)
                        for y in x:
                            lab=Label(cdocs,text=y).grid(row=i+2,column=n,padx=10,pady=10)
                            n=n+1


            curr_cmono = cmono_box.get()
            curr_cmono = (curr_cmono,)

            sqlcmd = "SELECT * FROM cmo WHERE cmo_no = %s"
            result = mycursor.execute(sqlcmd,curr_cmono)
            result = mycursor.fetchall()

            if not result:
                text = "Please Enter Valid Credentials"
                lab = Label(_login, text = text, fg="Red")
                lab.place(x=130, y=100)

            else:
                cmotk = Tk()
                cmotk.title("Chief Medical Officer")
                cmotk.geometry("400x500")

                addpatbut = Button(cmotk, text = "Patients", command = forward1).place(x=170,y=150)
                checkdoc = Button(cmotk, text = "Doctors", command = forward2).place(x=170,y=230)


        l=Label(_login,text="Please Fill Your Credentials", font = ("Arial",20)).pack()
        pid_label = Label(_login, text="CMO_no: ", font = ("Arial", 16)).place(x=70,y=150)
        name_label = Label(_login, text="Password: ", font = ("Arial", 16)).place(x=70, y=250)

        cmono_box = Entry(_login)
        cmono_box.place(x=200, y=155)
        pswd_box = Entry(_login)
        pswd_box.place(x=200,y=255)

        login = Button(_login,text="Login",command = main_window2).place(x=200, y=325)

    if(describe.get() == "3"):
        _login = Tk()
        _login.title = ("Login")
        _login.geometry("1920x1080")
        global frame2
        frame2 = Frame(_login)
        frame2.grid(row = 9, column=6)

        def setframe():
            global frame2
            frame2 = Frame(_login)
            frame2.grid(row=7,column=6)

        def clr():
            frame2.destroy()
            login['state'] = NORMAL
            setframe()

        def main_window3():


            login['state'] = DISABLED
            curr_dcno = dcno_box.get()
            curr_dcno = (curr_dcno,)

            sqlcmd0 = "SELECT * FROM district_collector WHERE office_no = %s"
            sqlcmd1 = "SELECT * FROM qcentre WHERE centre_owner_id = %s"
            sqlcmd2 = "SELECT * FROM cmo WHERE cmo_no IN (SELECT centre_incharge_id FROM qcentre WHERE centre_owner_id = %s)"
            res0 = mycursor.execute(sqlcmd0,curr_dcno)
            res0 = mycursor.fetchall()
            res1 = mycursor.execute(sqlcmd1,curr_dcno)
            res1 = mycursor.fetchall()
            res2 = mycursor.execute(sqlcmd2,curr_dcno)
            res2 = mycursor.fetchall()

            if not res0:
                text = "Please Enter Valid Credentials"
                lab = Label(frame2, text = text, fg="Red")
                lab.grid(row=7,column=6)

            else:
                allinfo = Tk()
                allinfo.title("District Collector")
                allinfo.geometry("1920x1080")

                i=0
                lab=Label(allinfo,text="Quarantine Centres:",font=("Arial",18)).grid(row=0,column=0)
                lab1=Label(allinfo,text="Centre No.").grid(row=1,column=1,padx=10,pady=10)
                lab2=Label(allinfo,text="Centre Name").grid(row=1,column=2,padx=10,pady=10)
                lab3=Label(allinfo,text="No of Rooms").grid(row=1,column=3,padx=10,pady=10)
                lab4=Label(allinfo,text="Centre Address").grid(row=1,column=4,padx=10,pady=10)
                lab5=Label(allinfo,text="Centre Owner Id (Distr Collector Id)").grid(row=1,column=5,padx=10,pady=10)
                lab6=Label(allinfo,text="Centre Incharge Id (Chief Med Off Id)").grid(row=1,column=6,padx=10,pady=10)
                # lab7=Label(allinfo,text="Sanitation Facility Id").grid(row=1,column=7,padx=10,pady=10)
                lab8=Label(allinfo,text="Total Patients").grid(row=1,column=7,padx=10,pady=10)

                for i,x in enumerate(res1):
                    n=1
                    newcentreno = res1[i][0]
                    print(newcentreno)
                    sql = "SELECT COUNT(p_id) FROM patients,qcentre WHERE patients.qcenterNo = qcentre.centre_no AND qcentre.centre_no=%s AND qcentre.centre_owner_id=%s"
                    res = mycursor.execute(sql,(newcentreno,dcno_box.get()))
                    res=mycursor.fetchall()
                    print(res)
                    for y in x:
                        lab = Label(allinfo,text=y)
                        lab.grid(row=i+2,column=n,padx=10,pady=10)
                        n+=1
                    lab=Label(allinfo,text=res[0][0]).grid(row=i+2,column=n)

                lab=Label(allinfo,text="Chief Medical Officers:",font=("Arial",18)).grid(row=i+3,column=0)
                lab1=Label(allinfo,text="Chief Medical Officer Id").grid(row=i+4,column=1,padx=10,pady=10)
                lab2=Label(allinfo,text="Name").grid(row=i+4,column=2,padx=10,pady=10)
                lab3=Label(allinfo,text="Contact No").grid(row=i+4,column=3,padx=10,pady=10)
                lab4=Label(allinfo,text="Email Id").grid(row=i+4,column=4,padx=10,pady=10)
                lab5=Label(allinfo,text="Quarantine Centre No.").grid(row=i+4,column=5,padx=10,pady=10)

                for j,x in enumerate(res2):
                    n=1
                    newcmono = res2[i][0]
                    qcencmd = "SELECT centre_no FROM cmo,qcentre WHERE qcentre.centre_incharge_id = cmo.cmo_no AND qcentre.centre_incharge_id=%s AND qcentre.centre_owner_id=%s"
                    qcen = mycursor.execute(qcencmd,(newcmono,dcno_box.get()))
                    qcen = mycursor.fetchall()
                    for y in x:
                        lab=Label(allinfo,text=y).grid(row=i+j+5,column=n)
                        n+=1
                    lab=Label(allinfo,text=qcen[0][0]).grid(row=i+j+5,column=n)

                def plot():
                    sqlcmd3 = "SELECT pincode FROM patients WHERE qcenterNo IN (SELECT centre_no FROM qcentre WHERE centre_owner_id = %s)"
                    mycursor.execute(sqlcmd3,curr_dcno)
                    res3=mycursor.fetchall()

                    array1 = []  #count => y axis
                    array2 = []  #pincode => x axis
                    for x in res3:
                        for y in x:
                            if(y not in array2):
                                array2.append(y)
                                print(y)
                                y=str(y)
                                print(y)
                                sql = "SELECT COUNT(p_id) FROM patients WHERE pincode=%s"
                                mycursor.execute(sql,(y,))
                                count = mycursor.fetchall()
                                count = count[0][0]
                                array1.append(count)

                    l=len(array2)
                    ar=[i for i in range(l)]
                    print(array1,array2)
                    plt.figure(figsize = (20,10))
                    plt.stem(array1)
                    plt.xticks(ar,array2)
                    plt.title("Graph Showing no of Patients in Each Area")
                    plt.xlabel('Pincodes')
                    plt.ylabel('No of Patients')
                    plt.show()

                graphbut = Button(allinfo,text="Show Graph", command=plot)
                graphbut.grid(row=13,column=4)


        l=Label(_login,text="Please Fill Your Credentials", font = ("Arial",20)).grid(row=1,column=3,padx=10,pady=10)
        dcnolab = Label(_login, text="Office No: ", font = ("Arial", 16)).grid(row=4,column=4,padx=10,pady=10)
        passlab = Label(_login, text="Password: ", font = ("Arial", 16)).grid(row=5,column=4,padx=10,pady=10)

        dcno_box = Entry(_login)
        dcno_box.grid(row=4,column=5,pady=10,padx=10)
        pswd_box = Entry(_login)
        pswd_box.grid(row=5,column=5,padx=10,pady=10)

        login = Button(_login,text="Login",command = main_window3)
        login.grid(row=6,column=4,pady=10,padx=10)

        clear = Button(_login,text="Clear Screen",command=clr).grid(row=7,column=4,pady=10,padx=10)

    if(describe.get() == "4"):
        cpatrec = Tk()
        cpatrec.title("Patient Record")
        cpatrec.geometry("1920x1080")
        global frame1
        frame1 = Frame(cpatrec)
        frame1.grid(row=7,column=6)
        lab=Label(cpatrec)

        def setframe():
            global frame1
            frame1 = Frame(cpatrec)
            frame1.grid(row=7,column=6)

        def clr():
            frame1.grid_forget()
            frame1.destroy()
            submitbut['state'] = NORMAL
            setframe()

        def main_window4():
            global frame1
            curr_pid = pid_box.get()
            submitbut['state'] = DISABLED
            curr_pid = (curr_pid,)
            sqlcmd = "SELECT * FROM patient_med_rec WHERE p_id = %s"

            result = mycursor.execute(sqlcmd,curr_pid)
            result = mycursor.fetchall()
            global lab

            if not result:
                text = "Please Enter Valid Credentials"
                lab = Label(frame1, text = text, fg="Red")
                lab.grid(row = 1,column=1)
            else:
                print(result)
                pnamelabel = Label(frame1, text="Patient Name")
                pnamelabel.grid(row=3, column=4, padx=10)
                cvlabel = Label(frame1, text="City Visited")
                cvlabel.grid(row=3, column=5, padx=10)

                pidlabel = Label(frame1,text="Patient Id")
                pidlabel.grid(row=3,column=6,padx=10)
                comorblabel = Label(frame1,text="Covid Comorbities")
                comorblabel.grid(row=3,column=7,padx=10)
                testdatelab = Label(frame1,text="Covid Test Date")
                retstdatelab = Label(frame1,text="Covid Retest Date")
                alrglab = Label(frame1,text="Allergies")
                statuslab = Label(frame1,text="Status")

                testdatelab.grid(row=3,column=8,padx=10)
                retstdatelab.grid(row=3,column=9,padx=10)
                alrglab.grid(row=3,column=10,padx=10)
                statuslab.grid(row=3,column=11,padx=10)
                result11 = mycursor.execute("SELECT name,city FROM patients INNER JOIN patient_travel_history ON patients.p_id = patient_travel_history.p_id")
                result11= mycursor.fetchall()

                for i,x in enumerate(result):
                    n=1
                    for y in x:
                        lab = Label(frame1,text=y)
                        lab.grid(row=i+4,column=n+5,padx=10)
                        n+=1


                for j,x in enumerate(result11):
                    m=1
                    for y in x:
                        lab = Label(frame1,text=y)
                        lab.grid(row=j+4,column=m+3,padx=10)
                        m+=1

        l=Label(cpatrec,text="Please Fill Patient's Credentials", font = ("Arial",20)).grid(row=0,column=7)
        pid_label = Label(cpatrec, text="Patient Id ", font = ("Arial", 16)).grid(row = 5, column = 3)
        pid_box = Entry(cpatrec)
        pid_box.grid(row = 5, column = 4)

        clrscrbut = Button(cpatrec,text = "Clear Screen", command = clr).grid(row=7,column=3,pady=10)
        submitbut = Button(cpatrec,text="Submit",command = main_window4)
        submitbut.grid(row = 6, column = 3,pady=10)

    if(describe.get() == "5"):
        clerkwindow = Tk()
        clerkwindow.title("Add Patients")
        clerkwindow.geometry("1920x1080")

        def clear_fields():
            name_box.delete(0, END)
            age_box.delete(0, END)
            contact_box.delete(0, END)
            address_box.delete(0, END)
            pincode_box.delete(0, END)
            email_box.delete(0, END)
            p_id_box.delete(0, END)
            dob_box.delete(0, END)
            nationality_box.delete(0, END)
            qcenterNo_box.delete(0, END)

            allergies_box.delete(0, END)
            status_box.delete(0, END)
            testdate_box.delete(0, END)
            retestdate_box.delete(0, END)
            covid_comor_box.delete(0, END)
            lastcity_box.delete(0, END)
            lastpin_box.delete(0, END)
            cotravellers_contact_box.delete(0, END)
            days_visited_box.delete(0, END)

        def add_patients():
            sql_command1 = "INSERT INTO patients (name, age, contact, address, pincode, email, p_id, dob, nationality, qcenterNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values1 = (name_box.get(), age_box.get(), contact_box.get(), address_box.get(),pincode_box.get(), email_box.get(), p_id_box.get(), dob_box.get(),nationality_box.get(), qcenterNo_box.get())
            mycursor.execute(sql_command1, values1)
            # commiting to the database
            mydb.commit()

            sql_command2 = "INSERT INTO patient_med_rec (p_id, allergies, status, covid_test_date, covid_retest_date, covid_comorbidity) VALUES (%s, %s, %s, %s, %s, %s)"
            values2 = (p_id_box.get(), allergies_box.get(), status_box.get(),testdate_box.get(), retestdate_box.get(), covid_comor_box.get())
            mycursor.execute(sql_command2, values2)
            # commiting to the database
            mydb.commit()

            if(lastpin_box.get() == ""):
                lastpin = None
            else:
                lastpin = int(lastpin_box.get())

            sql_command3 = "INSERT INTO patient_travel_history (p_id, city, city_pincode, cotrav_contact, no_of_days_of_travel) VALUES (%s, %s, %s, %s, %s)"
            values3 = (p_id_box.get(), lastcity_box.get(), lastpin, cotravellers_contact_box.get(), days_visited_box.get())
            mycursor.execute(sql_command3, values3)
            # commiting to the database
            mydb.commit()

        name_label = Label(clerkwindow, text="Name*", fg="white", bg="black").grid(row=1, column=0, sticky=W, padx=10)
        age_label = Label(clerkwindow, text="Age*", fg="white", bg="black").grid(row=2, column=0, sticky=W, padx=10)
        contact_label = Label(clerkwindow, text="Contact no*", fg="white", bg="black").grid(row=3, column=0, sticky=W, padx=10)
        address_label = Label(clerkwindow, text="Address*", fg="white", bg="black").grid(row=4, column=0, sticky=W, padx=10)
        pincode_label = Label(clerkwindow, text="pincode*", fg="white", bg="black").grid(row=5, column=0, sticky=W, padx=10)
        email_label = Label(clerkwindow, text="Email id", fg="white", bg="black").grid(row=6, column=0, sticky=W, padx=10)
        p_id_label = Label(clerkwindow, text="patient_ID*", fg="white", bg="black").grid(row=7, column=0, sticky=W, padx=10)
        dob_label = Label(clerkwindow, text="D.O.B (DDMMYYYY)*", fg="white", bg="black").grid(row=8, column=0, sticky=W, padx=10)
        nationality_label = Label(clerkwindow, text="NATIONALITY*", fg="white", bg="black").grid(row=9, column=0, sticky=W, padx=10)
        qcenterNo_label = Label(clerkwindow, text="Q-Center No*", fg="white", bg="black").grid(row=10, column=0, sticky=W, padx=10)


        allergies_label =Label(clerkwindow, text="Allergies", fg="white", bg="black").grid(row=1, column=2, sticky=W, padx=10)
        covid_comor_label =Label(clerkwindow, text="Covid comorbidities", fg="white", bg="black").grid(row=2, column=2, sticky=W, padx=10)
        testdate = Label(clerkwindow, text="Test date*", fg="white", bg="black").grid(row=3, column=2, sticky=W, padx=10)
        retestdate = Label(clerkwindow, text="Retest date*", fg="white", bg="black").grid(row=4, column=2, sticky=W, padx=10)
        Status = Label(clerkwindow, text="Status", fg="white", bg="black").grid(row=5, column=2, sticky=W, padx=10)

        city_visited_name_label = Label(clerkwindow, text="Last City Visited", fg="white", bg="black").grid(row=6, column=2, sticky=W, padx=10)
        city_visited_pin_label = Label(clerkwindow, text="Pincode of place visited", fg="white", bg="black").grid(row=7, column=2, sticky=W, padx=10)
        cotravellers_contact_label = Label(clerkwindow, text="Cotravellers' contact", fg="white", bg="black").grid(row=8, column=2, sticky=W, padx=10)
        no_of_days_label = Label(clerkwindow, text="No of days visited", fg="white", bg="black").grid(row=9, column=2, sticky=W, padx=10)
        # Creating entry boxes

        name_box = Entry(clerkwindow, bg="#B0C4DE")
        name_box.grid(row=1, column=1, pady=5, ipadx=30)

        age_box = Entry(clerkwindow, bg="#B0C4DE")
        age_box.grid(row=2, column=1, pady=5, ipadx=30)

        contact_box = Entry(clerkwindow, bg="#B0C4DE")
        contact_box.grid(row=3, column=1, pady=5, ipadx=30)

        address_box = Entry(clerkwindow, bg="#B0C4DE")
        address_box.grid(row=4, column=1, pady=5, ipadx=30)

        pincode_box = Entry(clerkwindow, bg="#B0C4DE")
        pincode_box.grid(row=5, column=1, pady=5, ipadx=30)

        email_box = Entry(clerkwindow, bg="#B0C4DE")
        email_box.grid(row=6, column=1, pady=5, ipadx=30)

        p_id_box = Entry(clerkwindow, bg="#B0C4DE")
        p_id_box.grid(row=7, column=1, pady=5, ipadx=30)

        dob_box = Entry(clerkwindow, bg="#B0C4DE")
        dob_box.grid(row=8, column=1, pady=5, ipadx=30)

        nationality_box = Entry(clerkwindow, bg="#B0C4DE")
        nationality_box.grid(row=9, column=1, pady=5, ipadx=30)

        qcenterNo_box = Entry(clerkwindow, bg="#B0C4DE")
        qcenterNo_box.grid(row=10, column=1, pady=5, ipadx=30)

        allergies_box = Entry(clerkwindow, bg="#B0C4DE")
        allergies_box.grid(row=1, column=3, pady=5, ipadx=30)
        covid_comor_box = Entry(clerkwindow, bg="#B0C4DE")
        covid_comor_box.grid(row=2, column=3, pady=5, ipadx=30)

        testdate_box = Entry(clerkwindow, bg="#B0C4DE")
        testdate_box.grid(row=3, column=3, pady=5, ipadx=30)
        retestdate_box = Entry(clerkwindow, bg="#B0C4DE")
        retestdate_box.grid(row=4, column=3, pady=5, ipadx=30)
        status_box = Entry(clerkwindow, bg="#B0C4DE")
        status_box.grid(row=5, column=3, pady=5, ipadx=30)
        lastcity_box = Entry(clerkwindow, bg="#B0C4DE")
        lastcity_box.grid(row=6, column=3, pady=5, ipadx=30)
        lastpin_box = Entry(clerkwindow, bg="#B0C4DE")
        lastpin_box.grid(row=7, column=3, pady=5, ipadx=30)
        cotravellers_contact_box = Entry(clerkwindow, bg="#B0C4DE")
        cotravellers_contact_box.grid(row=8, column=3, pady=5, ipadx=30)
        days_visited_box = Entry(clerkwindow, bg="#B0C4DE")
        days_visited_box.grid(row=9, column=3, pady=5, ipadx=30)

        # Create Buttons
        add_patient_button = Button(clerkwindow, text="Add patient to database!", command=add_patients, bg="#0198E1", fg="White")
        add_patient_button.grid(row=11, column=0, padx=10, pady=10)

        clear_fields_button = Button(clerkwindow, text="Clear Fields", command=clear_fields, bg="#CD0000", fg="White")
        clear_fields_button.grid(row=11, column=1, padx=10)


l = Label(_root, text = "You describe yourself as a :- ", font = ("Arial", 20)).pack()

values = {"Patient" : "1",
        "Chief Medical Officer" : "2",
        "District Collector" : "3",
        "Doctor" : "4",
        "Clerk": "5"}

for (text,value) in values.items():
    Radiobutton(_root, text = text, variable=describe, value=value).pack(side = TOP, ipady = 5)

submit = Button(_root, text = "Submit", command = describe_submit).pack()

mainloop()
mydb.commit()
