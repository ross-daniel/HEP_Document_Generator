from Electrical_Docs import Cable_Traveler
from Mechanical_Docs import MechQCForm
import gui
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# ------------------FIREBASE SETUP--------------------------------------------------------
#retrieve admin credentials
cred = credentials.Certificate('hep---dune-firebase-adminsdk-gtwlw-40673207a6.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hep---dune-default-rtdb.firebaseio.com'
})

# As an admin, the app has access to read and write all data
ref = db.reference('')
# -----------------------------------------------------------------------------------------

# TODO: write _Docs classes with methods to fill and return spreadsheet/pdf objects


def pull_from_mech_DB(obj):
    print("called")
    return None


def pull_from_cable_DB(obj):
    # batch_table[cable_num] gives a dictionary with (qc step: name-date) format
    return ref.child(obj.cable_type).child('Batch').child(obj.batch_num).order_by_key().get()


if __name__ == "__main__":
    # -------------LOAD MAIN GUI----------------
    document_select = gui.MainGUI()

    if document_select.document_req == "Mechanical QC":
        # requesting MechQC Document
        mech_obj = gui.MechGUI()
        mech_table = pull_from_mech_DB(mech_obj)
        qc_doc = MechQCForm(mech_obj, mech_table)

    elif document_select.document_req == "Cable Traveler":
        # requesting Cable Traveler
        cable_obj = gui.CableGUI()    # holds cable information
        dest = cable_obj.destination  # file destination for traveler
        filename = dest + cable_obj.cable_type + "_batch" + cable_obj.batch_num +".xlsx"
        cable_table = pull_from_cable_DB(cable_obj)  # cable QC info from database
        traveler = Cable_Traveler(cable_obj, cable_table)
        traveler.fill_table()
        traveler.update_batch()
        traveler.workbook.save(filename=filename)
