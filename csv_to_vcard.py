import sys
import vobject
import csv

def convert(csv_filename):
    all_vcs = ""

    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            firstname = row[0]
            surname = row[1]
            mobile = row[2]

            vc_begin = "BEGIN:VCARD\n"
            vc_version = "VERSION:3.0\n"
            vc_name = f"N:{surname};{firstname};;;\n"
            vc_fn= f"FN:{firstname} {surname}\n"
            vc_phone = f"TEL;TYPE=CELL,TYPE=pref;TYPE=VOICE:{mobile}\n"
            vc_end = "END:VCARD\n"

            vc_out = vc_begin + vc_version + vc_name + vc_fn + vc_phone + vc_end
            all_vcs += vc_out

    print(all_vcs)

def usage():
    print("====== USAGE ======")
    print("./csv_to_vcard.py csvfile.csv")
    print("Expected columns in CSV file: Firstname,Surname,MobileNumber")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        exit(1)

    csv_filename = sys.argv[1]
    convert(csv_filename) 
