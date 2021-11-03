from tkinter import *
from sound_player import SoundPlayer
from tkinter import messagebox
from data_handler import ChangeClientInfoDataHandler

cci_sounds = SoundPlayer()


class ChangeClientInfo(ChangeClientInfoDataHandler):
    """Change CLient Info Page"""
    def __init__(self):
        ChangeClientInfoDataHandler.__init__(self)
        self.project_background_colour = "#8e94a4"
        self.project_bar_colour = "#3b415b"
        self.label_background_colour = "white"
        self.test_colour = "black"
        self.height = 720
        self.width = 1280
        self.frame_height = 496
        self.cid_font = ("Arial", "16")
        self.cid_font_large = ("Arial", "24", "underline")
        self.cid_font_large_no_line = ("Arial", "24")
        self.cid_font_small = ("Arial", "10")
        self.cid_font_underline = ("Arial", "16", "underline")

    def create_change_client_info(self, key, frame, root, client_dict, fnc):
        """Creates change client info page"""
        self.cci_key = key
        self.cci_frame = frame
        self.cci_root = root
        self.cci_dict = client_dict
        self.fnc = fnc

        self.cci_info_frame = Frame(self.cci_frame)
        self.cci_info_frame.config(bg=self.project_background_colour, height=self.frame_height, width=self.width,
                                   highlightthickness=0, borderwidth=0)
        self.cci_info_frame.grid(row=0, column=0)
        self.cci_info_frame.grid_propagate(False)

        self.name_label = AddCciFields(self.cci_info_frame, 0, 0, "Client Name: ")
        self.service_add_1_label = AddCciFields(self.cci_info_frame, 1, 0, "Service Address Line One: ")
        self.service_add_2_label = AddCciFields(self.cci_info_frame, 2, 0, "Service Address Line Two: ")
        self.service_add_3_label = AddCciFields(self.cci_info_frame, 3, 0, "Service Address Line Three: ")
        self.service_postcode_label = AddCciFields(self.cci_info_frame, 4, 0, "Service Postcode: ")
        self.email_label = AddCciFields(self.cci_info_frame, 5, 0, "Email: ")
        self.home_number_label = AddCciFields(self.cci_info_frame, 6, 0, "Home Number: ")
        self.mobile_number_label = AddCciFields(self.cci_info_frame, 7, 0, "Mobile Number: ")
        self.job_desc_label = AddCciFields(self.cci_info_frame, 8, 0, "Job Description: ")
        AddCciFields.pad = 60
        self.client_ref_label = AddCciFields(self.cci_info_frame, 0, 2, "Client Reference: ")
        self.job_add_1_label = AddCciFields(self.cci_info_frame, 1, 2, "Job Address Line One: ")
        self.job_add_2_label = AddCciFields(self.cci_info_frame, 2, 2, "Job Address Line Two: ")
        self.job_add_3_label = AddCciFields(self.cci_info_frame, 3, 2, "Job Address Line Three: ")
        self.job_postcode_label = AddCciFields(self.cci_info_frame, 4, 2, "Job Postcode: ")
        self.date_quote_sent_label = AddCciFields(self.cci_info_frame, 5, 2, "Date Quote Sent: ")
        self.date_invoice_sent_label = AddCciFields(self.cci_info_frame, 6, 2, "Date Invoice Sent: ")
        self.date_paid_label = AddCciFields(self.cci_info_frame, 7, 2, "Date Paid: ")
        AddCciFields.pad = 40

        self.change_details_button = Label(self.cci_info_frame)
        self.change_details_button.config(bg=self.project_bar_colour, text="Add New Details To Client Database",
                                          font=self.cid_font)
        self.change_details_button.grid(row=8, column=2, columnspan=2, padx=(20, 0), pady=10, sticky="we")
        self.change_details_button.bind("<Enter>", lambda _: self.change_details_button.config(relief="ridge"))
        self.change_details_button.bind("<Leave>", lambda _: self.change_details_button.config(relief="flat"))
        self.change_details_button.bind("<Button-1>", self.add_new_details_button_func)
        self.populate_entry_boxes()

    def populate_entry_boxes(self):
        """Populates entry boxes in change_client_info page"""
        self.name_label.item_entry_name.insert(END, self.cci_dict["name"])
        self.service_add_1_label.item_entry_name.insert(END, self.cci_dict["service_address"]["service_add_1"])
        self.service_add_2_label.item_entry_name.insert(END, self.cci_dict["service_address"]["service_add_2"])
        self.service_add_3_label.item_entry_name.insert(END, self.cci_dict["service_address"]["service_add_3"])
        self.service_postcode_label.item_entry_name.insert(END, self.cci_dict["service_address"]["service_postcode"])
        self.email_label.item_entry_name.insert(END, self.cci_dict["email"])
        self.home_number_label.item_entry_name.insert(END, self.cci_dict["home_number"])
        self.mobile_number_label.item_entry_name.insert(END, self.cci_dict["mobile_number"])
        self.job_desc_label.item_entry_name.insert(END, self.cci_dict["job_desc"])
        try:
            self.client_ref_label.item_entry_name.insert(END, self.cci_dict["client_ref"])
        except TclError:
            self.client_ref_label.item_entry_name.insert(END, " ")
        self.job_add_1_label.item_entry_name.insert(END, self.cci_dict["address"]["add_1"])
        self.job_add_2_label.item_entry_name.insert(END, self.cci_dict["address"]["add_2"])
        self.job_add_3_label.item_entry_name.insert(END, self.cci_dict["address"]["add_3"])
        self.job_postcode_label.item_entry_name.insert(END, self.cci_dict["address"]["postcode"])
        self.date_quote_sent_label.item_entry_name.insert(END, self.cci_dict["date_quote_sent"])
        self.date_invoice_sent_label.item_entry_name.insert(END, self.cci_dict["date_invoice_sent"])
        self.date_paid_label.item_entry_name.insert(END, self.cci_dict["date_paid"])

    def variable_maker(self):
        """Creates variables for use in add_new_details_button_func"""
        self.name_var = self.name_label.item_entry_name.get()
        self.serv_add_1_var = self.service_add_1_label.item_entry_name.get()
        self.serv_add_2_var = self.service_add_2_label.item_entry_name.get()
        self.serv_add_3_var = self.service_add_3_label.item_entry_name.get()
        self.serv_postcode_var = self.service_postcode_label.item_entry_name.get()
        self.email_var = self.email_label.item_entry_name.get()
        self.home_num_var = self.home_number_label.item_entry_name.get()
        self.mobile_num_var = self.mobile_number_label.item_entry_name.get()
        self.job_desc_var = self.job_desc_label.item_entry_name.get()
        if self.client_ref_label.item_entry_name.get() == " " or self.client_ref_label.item_entry_name.get() == "":
            self.client_ref_var = None
        else:
            self.client_ref_var = self.client_ref_label.item_entry_name.get()
        self.job_add_1_var = self.job_add_1_label.item_entry_name.get()
        self.job_add_2_var = self.job_add_2_label.item_entry_name.get()
        self.job_add_3_var = self.job_add_3_label.item_entry_name.get()
        self.job_postcode_var = self.job_postcode_label.item_entry_name.get()
        self.quote_sent_var = self.date_quote_sent_label.item_entry_name.get()
        self.invoice_sent_var = self.date_invoice_sent_label.item_entry_name.get()
        self.paid_var = self.date_paid_label.item_entry_name.get()

    def entry_field_clear(self):
        """Clears entry fields, will most likely not need to use this method"""
        self.name_label.item_entry_name.delete(0, END)
        self.service_add_1_label.item_entry_name.delete(0, END)
        self.service_add_2_label.item_entry_name.delete(0, END)
        self.service_add_3_label.item_entry_name.delete(0, END)
        self.service_postcode_label.item_entry_name.delete(0, END)
        self.email_label.item_entry_name.delete(0, END)
        self.home_number_label.item_entry_name.delete(0, END)
        self.mobile_number_label.item_entry_name.delete(0, END)
        self.job_desc_label.item_entry_name.delete(0, END)
        self.client_ref_label.item_entry_name.delete(0, END)
        self.job_add_1_label.item_entry_name.delete(0, END)
        self.job_add_2_label.item_entry_name.delete(0, END)
        self.job_add_3_label.item_entry_name.delete(0, END)
        self.job_postcode_label.item_entry_name.delete(0, END)
        self.date_quote_sent_label.item_entry_name.delete(0, END)
        self.date_invoice_sent_label.item_entry_name.delete(0, END)
        self.date_paid_label.item_entry_name.delete(0, END)

    def add_new_details_button_func(self, event):
        """Calls all methods involved in the process of adding new data to client database"""
        cci_sounds.play_click()
        self.variable_maker()
        conf_message = messagebox.askyesno(title="Confirm Data Change", message="Are you sure you want to change"
                                                                                " modified data?")
        if not conf_message:
            pass
        else:
            self.change_client_info(self.cci_key, self.name_var, self.serv_add_1_var, self.serv_add_2_var,
                                    self.serv_add_3_var, self.serv_postcode_var, self.email_var, self.home_num_var,
                                    self.mobile_num_var, self.job_desc_var, self.client_ref_var, self.job_add_1_var,
                                    self.job_add_2_var, self.job_add_3_var, self.job_postcode_var, self.quote_sent_var,
                                    self.invoice_sent_var, self.paid_var)
            self.entry_field_clear()
            self.fnc()


class AddCciFields:
    pad = 40
    """Class to create labels and entry fields, created to save time creating each of the instances
     individually from scratch"""
    def __init__(self, frame, row_param, column_param, label_cci_name):
        self.row_param = row_param
        self.column_param = column_param
        self.frame = frame
        self.label_cci_name = label_cci_name
        self.class_font = ("Arial", "16")
        self.class_background_colour = "#8e94a4"
        pad = AddCciFields.pad

        self.label_name = Label(self.frame)
        self.label_name.config(font=self.class_font, text=self.label_cci_name, bg=self.class_background_colour)
        self.item_entry_name = Entry(self.frame)
        self.item_entry_name.config(width=25, font=self.class_font)

        self.label_name.grid(row=self.row_param, column=self.column_param, pady=13, padx=(pad, 0))
        self.item_entry_name.grid(row=self.row_param, column=self.column_param+1, sticky="w", pady=13)



