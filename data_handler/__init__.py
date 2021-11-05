import json
import datetime
from random import randint
from pathlib import Path


class DataCreator:

    def __init__(self):

        self.now = str(datetime.date.today().strftime("%d-%m-%Y"))

    @staticmethod
    def ref_num_maker():
        file_name = "client_database.json"
        file_path = Path(file_name)
        if file_path.is_file():
            pass
        if file_path.is_file():
            with open(file_name, "r") as open_data:
                ref_maker_dict = json.load(open_data)
                ref_maker_number = randint(100000, 999999)

            if str(ref_maker_number) in ref_maker_dict:
                checking = True
                while checking:
                    print("found a naughty")
                    ref_maker_number = randint(100000, 999999)
                    if str(ref_maker_number) in ref_maker_dict:
                        print("found another naughty")
                    else:
                        return ref_maker_number

            else:
                return ref_maker_number

        else:
            ref_maker_number = randint(100000, 999999)
            return ref_maker_number

    def add_client(self, name, address_1=None, address_2=None, address_3=None, postcode=None, email=None,
                   home_number=None, mobile_number=None, quote_sent=False, invoice_sent=False, job_desc=None,
                   quote_accepted=False, paid=False, service_address_1=None, service_address_2=None,
                   service_address_3=None, service_postcode=None, job_completed=False, quote_declined=False,
                   price=0, amount_paid=0, date_quote_sent="Not Sent", date_invoice_sent="Not Sent", client_ref=None,
                   invoice_number=None, date_paid="Not Paid", favourite=False):
        # Invoice number creation
        inv_file_name = "invoice_number.json"
        inv_file_path = Path(inv_file_name)

        if inv_file_path.is_file():
            with open(inv_file_name, "r") as open_inv_data:
                invoice_number = json.load(open_inv_data)
                invoice_number += 1

            with open(inv_file_name, "w") as open_inv_data:
                json.dump(invoice_number, open_inv_data, indent=2)
        else:
            with open(inv_file_name, "w") as open_inv_data:
                invoice_number = 239
                json.dump(invoice_number, open_inv_data, indent=2)

        ref_number = self.ref_num_maker()
        client = {"name": name,
                  "address": {"add_1": address_1,
                              "add_2": address_2,
                              "add_3": address_3,
                              "postcode": postcode},
                  "email": email,
                  "home_number": home_number,
                  "mobile_number": mobile_number,
                  "quote_sent": quote_sent,
                  "invoice_sent": invoice_sent,
                  "job_desc": job_desc,
                  "quote_accepted": quote_accepted,
                  "paid": paid,
                  "service_address": {"service_add_1": service_address_1,
                                      "service_add_2": service_address_2,
                                      "service_add_3": service_address_3,
                                      "service_postcode": service_postcode},
                  "job_completed": job_completed,
                  "quote_declined": quote_declined,
                  "price": price,
                  "amount_paid": amount_paid,
                  "date_quote_sent": date_quote_sent,
                  "date_invoice_sent": date_invoice_sent,
                  "ref_number": ref_number,
                  "date_created": self.now,
                  "client_ref": client_ref,
                  "invoice_number": invoice_number,
                  "materials_and_labour": {},
                  "date_paid": date_paid,
                  "notes": [],
                  "favourite": favourite
                  }

        file_name = "client_database.json"
        file_path = Path(file_name)

        if file_path.is_file():
            with open(file_name, "r") as open_data:
                to_save = json.load(open_data)
                to_save[ref_number] = client

            with open(file_name, "w") as open_file:
                json.dump(to_save, open_file, indent=2)

        else:
            dict_create = {ref_number: client}
            with open(file_name, "w") as new_data:
                json.dump(dict_create, new_data, indent=2)


class ClientListPopulate:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def clv_populate_all(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)
                for item in clv_dict:
                    string_to_disp = ""
                    if clv_dict[item]["client_ref"] is None:
                        string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                          f"{clv_dict[item]['address']['add_1']}"
                        list_to_return.append(string_to_disp)
                        self.key_dict.append(clv_dict[item]["ref_number"])
                    else:
                        string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -  " \
                                          f"{clv_dict[item]['job_desc']}  -  " \
                                        f"{clv_dict[item]['address']['add_1']}"
                        list_to_return.append(string_to_disp)
                        self.key_dict.append(clv_dict[item]["ref_number"])
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_populate_quotes_pending(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in clv_dict:
                    if clv_dict[item]["quote_sent"]:
                        if clv_dict[item]["quote_accepted"]:
                            pass
                        else:
                            string_to_disp = ""
                            if clv_dict[item]["client_ref"] is None:
                                string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])
                            else:
                                string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -" \
                                                  f"  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

            if len(list_to_return) == 0:
                list_to_return.append(" No Pending Quotes")
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_populate_quotes_accepted(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in clv_dict:

                    if clv_dict[item]["quote_accepted"]:
                        if not clv_dict[item]["invoice_sent"]:
                            string_to_disp = ""
                            if clv_dict[item]["client_ref"] is None:
                                string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])
                            else:
                                string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -" \
                                                  f"  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

            if len(list_to_return) == 0:
                list_to_return.append(" No Accepted Quotes")
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_populate_awaiting_payment(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in clv_dict:

                    if clv_dict[item]["invoice_sent"]:
                        if not clv_dict[item]["paid"]:
                            string_to_disp = ""
                            if clv_dict[item]["client_ref"] is None:
                                string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])
                            else:
                                string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -" \
                                                  f"  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

            if len(list_to_return) == 0:
                list_to_return.append(" No Jobs Awaiting Payment")
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_populate_jobs_completed(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in clv_dict:

                    if clv_dict[item]["job_completed"]:
                        string_to_disp = ""
                        if clv_dict[item]["client_ref"] is None:
                            string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                              f"{clv_dict[item]['address']['add_1']}"
                            list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])
                        else:
                            string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -" \
                                              f"  {clv_dict[item]['job_desc']}  -  " \
                                               f"{clv_dict[item]['address']['add_1']}"
                            list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])

            if len(list_to_return) == 0:
                list_to_return.append(" No Completed Jobs")
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_populate_favourites(self):
        list_to_return = []
        self.key_dict = []
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in clv_dict:
                    if not clv_dict[item]["favourite"]:
                        pass
                    else:
                        string_to_disp = ""
                        if clv_dict[item]["client_ref"] is None:
                            string_to_disp += f" {clv_dict[item]['name']}  -  " \
                                                 f"{clv_dict[item]['service_address']['service_add_1']}"
                            list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])
                        else:
                            string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -  " \
                                              f"{clv_dict[item]['service_address']['service_add_1']}"
                            list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])

            if len(list_to_return) == 0:
                list_to_return.append(" No Favourites Added")
            self.perm_dict = self.key_dict
            return list_to_return

        else:
            list_to_return.append(" Client List Is Empty")
            self.perm_dict = self.key_dict
            return list_to_return

    def clv_dict_key_maker(self):
        return self.key_dict

    def search_populate(self, search_term):
        self.key_dict = []
        self.list_to_return = []
        search_dict = []
        for item in self.perm_dict:
            search_dict.append(str(item))

        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                clv_dict = json.load(open_data)

                for item in search_dict:
                    string_to_disp = ""
                    if search_term.lower() in str(clv_dict[item].values()).lower():

                        if clv_dict[item]["client_ref"] is None:
                            string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                              f"{clv_dict[item]['address']['add_1']}"
                            self.list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])

                        else:
                            string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -  " \
                                              f"{clv_dict[item]['job_desc']}  -  " \
                                              f"{clv_dict[item]['address']['add_1']}"
                            self.list_to_return.append(string_to_disp)
                            self.key_dict.append(clv_dict[item]["ref_number"])

                    if search_term.lower() in str(clv_dict[item]["address"].values()).lower():

                        if clv_dict[item]["client_ref"] is None:
                            if string_to_disp == "":
                                string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                self.list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])
                        else:
                            if string_to_disp == "":
                                string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -  " \
                                                  f"{clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                self.list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

                    if search_term.lower() in str(clv_dict[item]["service_address"].values()).lower():

                        if clv_dict[item]["client_ref"] is None:
                            if string_to_disp == "":
                                string_to_disp += f" {clv_dict[item]['name']}  -  {clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                self.list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

                        else:
                            if string_to_disp == "":
                                string_to_disp += f" {clv_dict[item]['name']} ({clv_dict[item]['client_ref']})  -  " \
                                                  f"{clv_dict[item]['job_desc']}  -  " \
                                                  f"{clv_dict[item]['address']['add_1']}"
                                self.list_to_return.append(string_to_disp)
                                self.key_dict.append(clv_dict[item]["ref_number"])

                if len(self.list_to_return) == 0:
                    self.list_to_return.append(" No Match Found")
                    print(self.list_to_return)
                    return self.list_to_return
                return self.list_to_return

        else:
            self.list_to_return.append(" No Information to Display")
            return self.list_to_return


class ClientInfoDictCreate:
    def __init__(self):
        self.filename = "client_database.json"

    def create_client_info_dict(self, key):
        self.client_key = key
        with open(self.filename, "r") as open_data:
            client_dict = json.load(open_data)
            return client_dict[self.client_key]


class FavouriteInfoDictCreate:
    def __init__(self):
        self.filename = "client_database.json"

    def create_favourite_info_dict(self, key):
        self.client_key = key
        with open(self.filename, "r") as open_data:
            client_dict = json.load(open_data)
            return client_dict[self.client_key]


class ClientMarkFunctions:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def create_newest_cmf_dict(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                self.cmf_dict = json.load(open_data)

    def dict_quote_sent(self, client_key):
        self.cmf_dict[client_key]["quote_sent"] = True
        self.cmf_dict[client_key]["date_quote_sent"] = str(datetime.date.today().strftime("%d-%m-%Y"))
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)

    def dict_quote_accepted(self, client_key):
        self.cmf_dict[client_key]["quote_accepted"] = True
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)

    def dict_quote_declined(self, client_key):
        self.cmf_dict[client_key]["quote_declined"] = True
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)

    def dict_invoice_sent(self, client_key):
        self.cmf_dict[client_key]["invoice_sent"] = True
        self.cmf_dict[client_key]["date_invoice_sent"] = str(datetime.date.today().strftime("%d-%m-%Y"))
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)

    def dict_paid(self, client_key):
        self.cmf_dict[client_key]["amount_paid"] = self.cmf_dict[client_key]["price"]
        self.cmf_dict[client_key]["paid"] = True
        self.cmf_dict[client_key]["job_completed"] = True
        self.cmf_dict[client_key]["date_paid"] = str(datetime.date.today().strftime("%d-%m-%Y"))
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)


class AddNewClientRef:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def add_ref_to_dict(self, client_key, new_data):
        with open(self.filename, "r") as open_data:
            self.cmf_dict = json.load(open_data)

        self.cmf_dict[client_key]["client_ref"] = new_data
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)


class AddNote:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def add_note_to_dict(self, client_key, new_data):
        with open(self.filename, "r") as open_data:
            self.cmf_dict = json.load(open_data)

        self.cmf_dict[client_key]["notes"].append(new_data)
        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)


class AddDataToMatAndLabour:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def add_to_dict(self, key, dic):
        with open(self.filename, "r") as open_data:
            self.cmf_dict = json.load(open_data)

        for item in dic:
            try:
                self.cmf_dict[key]["materials_and_labour"][item] = format(float(dic[item]), '.2f')
            except ValueError:
                pass

        quote_total = 0
        for cost in self.cmf_dict[key]["materials_and_labour"]:
            price_var = float(self.cmf_dict[key]["materials_and_labour"][cost])
            quote_total += price_var
        self.cmf_dict[key]["price"] = format(float(quote_total), ".2f")

        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)


class MatAndLabListBoxPopulate:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def populate_mat_lab_listbox(self, key, display_full):
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                self.cmf_dict = json.load(open_data)
        list_to_return = []
        if len(self.cmf_dict[key]["materials_and_labour"]) == 0:
            list_to_return.append(" Nothing Added To This Account")
            return list_to_return
        else:
            if not display_full:
                for item in self.cmf_dict[key]["materials_and_labour"]:
                    data_string = ""
                    if len(item) <= 20:
                        data_string += f" {item}  -  £{self.cmf_dict[key]['materials_and_labour'][item]}"
                        list_to_return.append(data_string)
                    else:
                        data_string += f" {item[:20]}....  -  £{self.cmf_dict[key]['materials_and_labour'][item]}"
                        list_to_return.append(data_string)
            else:
                for item in self.cmf_dict[key]["materials_and_labour"]:
                    data_string = ""
                    data_string += f" {item}  -  £{self.cmf_dict[key]['materials_and_labour'][item]}"
                    list_to_return.append(data_string)

            return list_to_return


class AddPayment:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def add_payment(self, key, value):
        with open(self.filename, "r") as open_data:
            self.cmf_dict = json.load(open_data)

        payment_total = float(self.cmf_dict[key]["amount_paid"])
        to_add = float(value)
        payment_total += to_add

        self.cmf_dict[key]["amount_paid"] = format(float(payment_total), ".2f")

        if float(self.cmf_dict[key]["amount_paid"]) > float(self.cmf_dict[key]["price"]):
            self.cmf_dict[key]["amount_paid"] = format(float(self.cmf_dict[key]["price"]), ".2f")

        with open(self.filename, "w") as open_data:
            json.dump(self.cmf_dict, open_data, indent=2)


class ViewNotes:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def view_notes(self, key):
        """Creates and returns a list of client notes"""
        with open(self.filename, "r") as open_data:
            self.cmf_dict = json.load(open_data)
        list_to_return = []
        for item in self.cmf_dict[key]["notes"]:
            list_to_return.append(f" {item}")

        if len(list_to_return) == 0:
            list_to_return.append(" No Notes Added To Account")

        return list_to_return


class BackUpDatabase:
    def __init__(self):
        self.main_filename = "client_database.json"
        self.main_filepath = Path(self.main_filename)
        self.backup_filename = "client_backup_database.json"
        self.main_inv_number_filename = "invoice_number.json"
        self.main_inv_filepath = Path(self.main_inv_number_filename)
        self.backup_inv_filename = "invoice_number_backup.json"

    def back_up(self):
        if self.main_filepath.is_file():
            with open(self.main_filename, "r") as open_data:
                data_to_backup = json.load(open_data)
            with open(self.backup_filename, "w") as backup_data:
                json.dump(data_to_backup, backup_data, indent=2)

            with open(self.main_inv_number_filename, "r") as inv_open_data:
                inv_data_to_backup = json.load(inv_open_data)
            with open(self.backup_inv_filename, "w") as inv_backup_data:
                json.dump(inv_data_to_backup, inv_backup_data, indent=2)


class RecoverDatabase:
    def __init__(self):
        self.main_filename = "client_database.json"
        self.main_filepath = Path(self.main_filename)
        self.backup_filename = "client_backup_database.json"
        self.main_inv_number_filename = "invoice_number.json"
        self.main_inv_filepath = Path(self.main_inv_number_filename)
        self.backup_inv_filename = "invoice_number_backup.json"

    def recover_database(self):
        with open(self.backup_filename, "r") as backup_data:
            data_to_recover = json.load(backup_data)
        with open(self.main_filename, "w") as empty_database:
            json.dump(data_to_recover, empty_database, indent=2)

        with open(self.backup_inv_filename, "r") as backup_inv_data:
            inv_data_to_recover = json.load(backup_inv_data)
        with open(self.main_inv_number_filename, "w") as empty_inv_database:
            json.dump(inv_data_to_recover, empty_inv_database)


class ChangeClientInfoDataHandler:
    def __init__(self):
        self.filename = "client_database.json"
        self.filepath = Path(self.filename)

    def change_client_info(self, key, client_name, client_serv_add_1, client_serv_add_2, client_serv_add_3,
                           client_serv_postcode, client_email, client_home_phone, client_mobile, client_job_desc,
                           client__ref_name, client_job_add_1, client_job_add_2, client_job_add_3, client_job_postcode,
                           date_quote_sent, date_invoice_sent, date_paid):
        """Takes passed in variables and modifies client information in database"""
        if self.filepath.is_file():
            with open(self.filename, "r") as open_data:
                cmf_dict = json.load(open_data)

            cmf_dict[key]["name"] = client_name
            cmf_dict[key]["address"]["add_1"] = client_job_add_1
            cmf_dict[key]["address"]["add_2"] = client_job_add_2
            cmf_dict[key]["address"]["add_3"] = client_job_add_3
            cmf_dict[key]["address"]["postcode"] = client_job_postcode
            cmf_dict[key]["email"] = client_email
            cmf_dict[key]["home_number"] = client_home_phone
            cmf_dict[key]["mobile_number"] = client_mobile
            cmf_dict[key]["job_desc"] = client_job_desc
            cmf_dict[key]["client_ref"] = client__ref_name
            cmf_dict[key]["service_address"]["service_add_1"] = client_serv_add_1
            cmf_dict[key]["service_address"]["service_add_2"] = client_serv_add_2
            cmf_dict[key]["service_address"]["service_add_3"] = client_serv_add_3
            cmf_dict[key]["service_address"]["service_postcode"] = client_serv_postcode
            cmf_dict[key]["date_quote_sent"] = date_quote_sent
            cmf_dict[key]["date_invoice_sent"] = date_invoice_sent
            cmf_dict[key]["date_paid"] = date_paid

            with open(self.filename, "w") as new_data:
                json.dump(cmf_dict, new_data, indent=2)
