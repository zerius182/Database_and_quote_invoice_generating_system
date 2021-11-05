from tkinter import *
from tkinter import messagebox
from sound_player import SoundPlayer
from data_handler import ClientInfoDictCreate, ClientMarkFunctions, AddNewClientRef, AddNote, MatAndLabListBoxPopulate,\
    AddPayment, ViewNotes
from add_to_mat_and_lab import AddToMatAndLab
from change_client_info import ChangeClientInfo

sci_sounds = SoundPlayer()


class ClientInfoDisplay(ClientMarkFunctions, AddNewClientRef, AddNote, AddToMatAndLab, MatAndLabListBoxPopulate,
                        AddPayment, ClientInfoDictCreate, ViewNotes, ChangeClientInfo):
    def __init__(self):
        ClientMarkFunctions.__init__(self)
        AddNewClientRef.__init__(self)
        AddNote.__init__(self)
        AddToMatAndLab.__init__(self)
        MatAndLabListBoxPopulate.__init__(self)
        AddPayment.__init__(self)
        ClientInfoDictCreate.__init__(self)
        ViewNotes.__init__(self)
        ChangeClientInfo.__init__(self)
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
        self.filename = "client_database.json"

    def populate_client_info_page(self, key, sci_frame, sci_root):
        self.client_info_key = key
        self.sci_frame = sci_frame
        self.sci_root = sci_root
        self.client_dict = self.create_client_info_dict(self.client_info_key)
        self.create_sci_and_job_frames()
        self.create_client_info_frame_and_job_label()
        self.create_client_info_labels()
        self.create_contact_frame_and_labels()
        self.create_sci_service_frame()
        self.create_service_details()
        self.create_other_details()
        self.create_sci_mat_and_lab()
        self.create_sci_functions_menu()

    def create_sci_and_job_frames(self):
        self.sci_info_frame = Frame(self.sci_frame)
        self.sci_info_frame.config(bg=self.project_background_colour, height=self.frame_height, width=self.width,
                                   highlightthickness=0, borderwidth=0)
        self.sci_info_frame.grid(row=0, column=0)

        self.job_details_frame = Frame(self.sci_info_frame)
        self.job_details_frame.config(bg=self.project_background_colour, height=40)
        self.job_details_frame.grid(row=0, column=0, pady=(0, 20), columnspan=2)
        # This code isn't used anymore but I'm leaving it in, just in case the client wants to change it
        """self.job_ref_label = Label(self.job_details_frame, text=f"#{self.client_dict['ref_number']}")
        self.job_ref_label.config(font=self.cid_font_large_no_line, bg=self.project_background_colour)
        self.job_ref_label.grid(row=0, column=0)"""
        self.job_title_label = Label(self.job_details_frame, text=self.client_dict['job_desc'])
        self.job_title_label.config(font=self.cid_font_large_no_line, bg=self.project_background_colour)
        self.job_title_label.grid(row=0, column=0, padx=20)

    def create_client_info_frame_and_job_label(self):
        self.client_info_frame = Frame(self.sci_info_frame)
        self.client_info_frame.config(height=245, width=400, bg=self.label_background_colour)
        self.client_info_frame.grid(row=1, column=1)
        self.client_info_frame.grid_propagate(False)

        self.job_address_label = Label(self.client_info_frame)
        self.job_address_label.config(font=("Arial", "20", "underline"), bg=self.label_background_colour,
                                      text="Job Address")
        self.job_address_label.place(x="200", y="30", anchor="center")

    def create_client_info_labels(self):
        self.client_name_label = Label(self.client_info_frame, text=self.client_dict["name"])
        self.client_name_label.config(font=self.cid_font, bg=self.label_background_colour)

        self.client_add1_label = Label(self.client_info_frame, text=self.client_dict["address"]["add_1"])
        self.client_add1_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_add1_label.place(x="200", y="80", anchor="center")

        self.client_add2_label = Label(self.client_info_frame, text=self.client_dict["address"]["add_2"])
        self.client_add2_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_add2_label.place(x="200", y="110", anchor="center")

        self.client_add3_label = Label(self.client_info_frame, text=self.client_dict["address"]["add_3"])
        self.client_add3_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_add3_label.place(x="200", y="140", anchor="center")

        self.client_postcode_label = Label(self.client_info_frame, text=self.client_dict["address"]["postcode"])
        self.client_postcode_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_postcode_label.place(x="200", y="170", anchor="center")

    def create_contact_frame_and_labels(self):
        self.contact_details_frame = Frame(self.sci_info_frame)
        self.contact_details_frame.config(bg=self.label_background_colour, width=400, height=170)
        self.contact_details_frame.grid(row=2, column=0, pady=(20, 0), padx=(30, 10))
        self.contact_details_frame.grid_propagate(False)

        self.contact_details_label = Label(self.contact_details_frame, text="Contact Details")
        self.contact_details_label.config(font=("Arial", "20", "underline"), bg=self.label_background_colour)
        self.contact_details_label.place(x="200", y="30", anchor="center")
        self.client_email_label = Label(self.contact_details_frame, text=self.client_dict["email"])
        self.client_email_label.config(font=self.cid_font, bg=self.label_background_colour, fg="blue")
        self.client_email_label.place(x="200", y="80", anchor="center")
        self.client_email_label.bind("<Enter>", lambda _: self.client_email_label.config(font=self.cid_font_underline,
                                     bg=self.project_background_colour))
        self.client_email_label.bind("<Leave>", lambda _: self.client_email_label.config(font=self.cid_font,
                                     bg=self.label_background_colour))
        self.client_mobile_label = Label(self.contact_details_frame, text=self.client_dict["mobile_number"])
        self.client_mobile_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_mobile_label.place(x="200", y="110", anchor="center")
        self.client_home_label = Label(self.contact_details_frame, text=self.client_dict["home_number"])
        self.client_home_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.client_home_label.place(x="200", y="140", anchor="center")

    def create_sci_service_frame(self):
        self.service_address_frame = Frame(self.sci_info_frame)
        self.service_address_frame.config(height=245, width=400, bg=self.label_background_colour)
        self.service_address_frame.grid(row=1, column=0, padx=(30, 10))
        self.service_address_frame.grid_propagate(False)

    def create_service_details(self):
        self.service_address_label = Label(self.service_address_frame, text="Service Address")
        self.service_address_label.config(font=("Arial", "20", "underline"), bg=self.label_background_colour)
        self.service_address_label.place(x="200", y="30", anchor="center")
        if self.client_dict["client_ref"] is None:
            self.service_address_name_label = Label(self.service_address_frame, text=self.client_dict["name"])
        else:
            self.service_address_name_label = Label(self.service_address_frame, text=f"{self.client_dict['name']}({self.client_dict['client_ref']})")
        self.service_address_name_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.service_address_name_label.place(x="200", y="80", anchor="center")
        self.service_add1_label = Label(self.service_address_frame, text=self.client_dict["service_address"]
                                        ["service_add_1"])
        self.service_add1_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.service_add1_label.place(x="200", y="110", anchor="center")
        self.service_add2_label = Label(self.service_address_frame, text=self.client_dict["service_address"]
                                        ["service_add_2"])
        self.service_add2_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.service_add2_label.place(x="200", y="140", anchor="center")
        self.service_add3_label = Label(self.service_address_frame, text=self.client_dict["service_address"]
                                        ["service_add_3"])
        self.service_add3_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.service_add3_label.place(x="200", y="170", anchor="center")
        self.service_postcode_label = Label(self.service_address_frame, text=self.client_dict["service_address"]
                                            ["service_postcode"])
        self.service_postcode_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.service_postcode_label.place(x="200", y="200", anchor="center")

    def create_other_details(self):
        self.other_details_frame = Frame(self.sci_info_frame)
        self.other_details_frame.config(bg=self.label_background_colour, width=400, height=170)
        self.other_details_frame.grid(row=2, column=1, pady=(20, 0))
        self.other_details_frame.grid_propagate(False)
        self.quote_total = format(float(self.client_dict["price"]), '.2f')
        self.quote_amount_label = Label(self.other_details_frame, text=f"Quote Amount:"
                                                                       f" £{self.quote_total}")
        self.quote_amount_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.quote_amount_label.place(x="200", y="20", anchor="center")
        quote_date_to_add = self.client_dict['date_quote_sent']
        self.quote_sent_label = Label(self.other_details_frame, text=f"Date Quote Sent: "
                                                                     f"{quote_date_to_add}")
        self.quote_sent_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.quote_sent_label.place(x="200", y="50", anchor="center")
        invoice_date_to_add = self.client_dict['date_invoice_sent']
        self.invoice_sent_label = Label(self.other_details_frame, text=f"Date Invoice Sent: "
                                                                       f"{invoice_date_to_add}")
        self.invoice_sent_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.invoice_sent_label.place(x="200", y="80", anchor="center")
        to_pay = format(float(self.client_dict['price']) - float(self.client_dict['amount_paid']), ".2f")
        self.to_pay_amount_label = Label(self.other_details_frame, text=f"Amount Outstanding: £{to_pay}")
        self.to_pay_amount_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.to_pay_amount_label.place(x="200", y="110", anchor="center")
        paid_date_to_add = self.client_dict['date_paid']
        self.date_paid_label = Label(self.other_details_frame, text=f"Date Paid: {paid_date_to_add}")
        self.date_paid_label.config(font=self.cid_font, bg=self.label_background_colour)
        self.date_paid_label.place(x="200", y="140", anchor="center")

    def create_sci_mat_and_lab(self):
        self.materials_and_labour_frame = Frame(self.sci_info_frame)
        self.materials_and_labour_frame.config(height=self.frame_height, width=400, borderwidth=0, highlightthickness=0,
                                               bg=self.project_background_colour)
        self.materials_and_labour_frame.grid(row=0, column=2, rowspan=3, padx=10, sticky="n")
        self.materials_and_labour_frame.grid_propagate(False)
        self.mat_and_labour_label = Label(self.materials_and_labour_frame, text="Materials and Labour")
        self.mat_and_labour_label.config(font=self.cid_font_large_no_line, bg=self.project_background_colour)
        self.mat_and_labour_label.grid(row=0, column=0, pady=(0, 20), padx=(0, 5))
        self.mat_and_labour_listbox = Listbox(self.materials_and_labour_frame)
        self.mat_and_labour_listbox.config(font=self.cid_font, bg=self.label_background_colour, height=15, width=35,
                                           borderwidth=0, highlightthickness=0, selectbackground="white",
                                           selectforeground="black", activestyle="none")
        self.mat_and_labour_listbox.grid(row=1, column=0)
        self.mat_listbox_scroller = Scrollbar(self.mat_and_labour_listbox)
        self.mat_and_labour_listbox.config(yscrollcommand=self.mat_listbox_scroller.set)
        self.mat_listbox_scroller.config(command=self.mat_and_labour_listbox.yview)

    def create_sci_functions_menu(self):
        self.function_options = ["Change Client Details",
                                 "Add Client Nickname",
                                 "Add to Materials And Labour",
                                 "View Materials And Labour",
                                 "Add Payment To Account",
                                 "Add Note",
                                 "View Notes",
                                 "Mark As Quote sent",
                                 "Mark As Quote Accepted",
                                 "Mark As Invoice Sent",
                                 "Mark As Paid",
                                 "Mark As Quote Declined",
                                 ]
        self.function_options_var = StringVar()
        self.function_options_var.set("Function Menu")
        self.client_info_dropdown_menu = OptionMenu(self.materials_and_labour_frame, self.function_options_var,
                                                    *self.function_options, command=self.option_function)
        self.client_info_dropdown_menu.config(font=self.cid_font, height=2,
                                              bg=self.project_bar_colour,
                                              activebackground=self.project_bar_colour
                                              , borderwidth=0, highlightthickness=0, direction="above", indicatoron=0)
        self.client_info_dropdown_menu["menu"].config(bg="white", font=self.cid_font)
        self.client_info_dropdown_menu.grid(row=2, column=0, sticky="we", pady=(8, 0))
        self.client_mat_and_lab_list = self.populate_mat_lab_listbox(self.client_info_key, display_full=False)
        for item in self.client_mat_and_lab_list:
            self.mat_and_labour_listbox.insert(END, item)

    def mark_quote_sent(self):
        msg = messagebox.askyesno(title="Mark As Quote Sent",
                                  message="Are you sure you want to mark this client as quote sent?")
        if msg:
            self.dict_quote_sent(self.client_info_key)
            self.client_dict = self.create_client_info_dict(self.client_info_key)
            self.quote_sent_label.config(text=f"Date Quote Sent: {self.client_dict['date_quote_sent']}")

    def mark_quote_accepted(self):
        msg = messagebox.askyesno(title="Mark As Quote Accepted",
                                  message="Are you sure you want to mark this client as quote accepted?")
        if msg:
            self.dict_quote_accepted(self.client_info_key)

    def mark_quote_declined(self):
        msg = messagebox.askyesno(title="Mark As Quote Declined",
                                  message="Are you sure you want to mark this client as quote declined?")
        if msg:
            self.dict_quote_declined(self.client_info_key)

    def mark_as_invoice_sent(self):
        msg = messagebox.askyesno(title="Mark As Invoice Sent",
                                  message="Are you sure you want to mark this client as invoice sent?")
        if msg:
            self.dict_invoice_sent(self.client_info_key)
            self.client_dict = self.create_client_info_dict(self.client_info_key)
            self.invoice_sent_label.config(text=f"Date Invoice Sent: {self.client_dict['date_invoice_sent']}")

    def mark_as_paid(self):
        msg = messagebox.askyesno(title="Mark as Paid",
                                  message="Are you sure you want to mark this client as paid?")
        if msg:
            self.dict_paid(self.client_info_key)
            self.client_dict = self.create_client_info_dict(self.client_info_key)
            self.date_paid_label.config(text=f"Date Paid: {self.client_dict['date_paid']}")
            to_pay = format(float(self.client_dict['price']) - float(self.client_dict['amount_paid']), ".2f")
            self.to_pay_amount_label.config(text=f"Amount Outstanding: £{to_pay}")

    def option_function(self, event):
        sci_sounds.play_click()
        self.create_newest_cmf_dict()
        if self.function_options_var.get() == "Mark As Quote sent":
            self.mark_quote_sent()
        if self.function_options_var.get() == "Mark As Quote Accepted":
            self.mark_quote_accepted()
        if self.function_options_var.get() == "Mark As Quote Declined":
            self.mark_quote_declined()
        if self.function_options_var.get() == "Mark As Invoice Sent":
            self.mark_as_invoice_sent()
        if self.function_options_var.get() == "Mark As Paid":
            self.mark_as_paid()
        if self.function_options_var.get() == "Add Client Nickname":
            self.add_client_ref_top_level_maker()
        if self.function_options_var.get() == "Add Note":
            self.add_note_to_dict_top_level_maker()
        if self.function_options_var.get() == "Add to Materials And Labour":
            self.add_to_materials_and_labour()
        if self.function_options_var.get() == "View Materials And Labour":
            self.view_materials_and_labour_toplevel_maker()
        if self.function_options_var.get() == "Add Payment To Account":
            self.add_payment_to_account()
        if self.function_options_var.get() == "View Notes":
            self.view_notes_toplevel_maker()
        if self.function_options_var.get() == "Change Client Details":
            self.open_change_client_info()

    def add_client_ref_top_level_maker(self):
        self.add_new_client_top_level = Toplevel(self.sci_root)
        self.add_new_client_top_level.title("Add Client Reference")
        self.add_new_client_top_level.config(bg=self.project_background_colour)
        self.add_new_client_top_level.resizable(0, 0)
        self.add_new_client_top_level.geometry("600x350")
        self.add_new_client_top_level.iconbitmap("pictures/gj.ico")
        self.create_acr_frames()
        self.create_acr_labels_and_entries()

    def create_acr_frames(self):
        self.anctl_top_frame = Frame(self.add_new_client_top_level)
        self.anctl_top_frame.config(height=50, width=600, bg=self.project_bar_colour)
        self.anctl_top_frame.grid(row=0, column=0)
        self.anctl_top_frame.grid_propagate(False)
        self.anctl_main_frame = Frame(self.add_new_client_top_level)
        self.anctl_main_frame.config(height=250, width=600, bg=self.project_background_colour)
        self.anctl_main_frame.grid(row=1, column=0)
        self.anctl_main_frame.grid_propagate(False)
        self.anctl_bottom_frame = Frame(self.add_new_client_top_level)
        self.anctl_bottom_frame.config(height=50, width=600, bg=self.project_bar_colour)
        self.anctl_bottom_frame.grid(row=2, column=0)
        self.anctl_bottom_frame.grid_propagate(False)

    def create_acr_labels_and_entries(self):
        self.anctl_header_label = Label(self.anctl_main_frame)
        self.anctl_header_label.config(font=self.cid_font_large_no_line, text="Add Reference Name To Client",
                                       bg=self.project_background_colour)
        self.anctl_header_label.place(x="300", y="50", anchor="center")
        self.anctl_entry = Entry(self.anctl_main_frame)
        self.anctl_entry.config(font=self.cid_font_large_no_line, width=10)
        self.anctl_entry.place(x="100", y="100")
        self.anctl_entry_label = Label(self.anctl_main_frame)
        self.anctl_entry_label.config(font=self.cid_font_small, bg=self.project_background_colour,
                                      text="(Nickname can be ten characters max)")
        self.anctl_entry_label.place(x="290", y="110")
        self.anctl_button = Label(self.anctl_main_frame)
        self.anctl_button.config(bg=self.project_bar_colour, font=self.cid_font_large_no_line, text="Add Reference",
                                 width=15)
        self.anctl_button.place(x="300", y="190", anchor="center")

        self.anctl_button.bind("<Enter>", lambda _: self.anctl_button.config(relief="ridge"))
        self.anctl_button.bind("<Leave>", lambda _: self.anctl_button.config(relief="flat"))
        self.anctl_button.bind("<Button-1>", self.add_client_ref_button_function)

    def add_client_ref_button_function(self, event):
        self.new_ref = self.anctl_entry.get()
        if len(self.new_ref) >= 11:
            messagebox.showinfo(title="Too Many Characters", message="Max 10 Characters Allowed, please try again",
                                parent=self.add_new_client_top_level)
            self.anctl_entry.delete(0, END)
        elif self.new_ref == "":
            messagebox.showinfo(title="No Data", message="No Reference Provided", parent=self.add_new_client_top_level)
        else:
            sci_sounds.play_click()
            self.add_new_client_top_level.destroy()
            self.add_ref_to_dict(self.client_info_key, self.new_ref)
            self.service_address_name_label = Label(self.service_address_frame, text=self.client_dict["name"] +
                                                    f" ({self.new_ref})")
            self.service_address_name_label.config(font=self.cid_font, bg=self.label_background_colour)
            self.service_address_name_label.place(x="200", y="80", anchor="center")
        self.client_dict = self.create_client_info_dict(self.client_info_key)

    def add_note_to_dict_top_level_maker(self):
        self.add_note_top_level = Toplevel(self.sci_root)
        self.add_note_top_level.title("Add Note To Client")
        self.add_note_top_level.config(bg=self.project_background_colour)
        self.add_note_top_level.geometry("600x300")
        self.add_note_top_level.resizable(0, 0)
        self.add_note_top_level.iconbitmap("pictures/gj.ico")
        self.create_antl_frames()
        self.create_antl_labels_entries_buttons()

    def create_antl_frames(self):
        self.antl_top_frame = Frame(self.add_note_top_level)
        self.antl_top_frame.config(height=50, width=600, bg=self.project_bar_colour)
        self.antl_top_frame.grid(row=0, column=0)
        self.antl_top_frame.grid_propagate(False)
        self.antl_main_frame = Frame(self.add_note_top_level)
        self.antl_main_frame.config(height=200, width=600, bg=self.project_background_colour)
        self.antl_main_frame.grid(row=1, column=0)
        self.antl_main_frame.grid_propagate(False)
        self.antl_bottom_frame = Frame(self.add_note_top_level)
        self.antl_bottom_frame.config(height=50, width=600, bg=self.project_bar_colour)
        self.antl_bottom_frame.grid(row=2, column=0)
        self.antl_bottom_frame.grid_propagate(False)

    def create_antl_labels_entries_buttons(self):
        self.antl_header_label = Label(self.antl_main_frame)
        self.antl_header_label.config(text="Add Note To Client Database", font=self.cid_font_large_no_line,
                                      bg=self.project_background_colour)
        self.antl_header_label.place(x="300", y="40", anchor="center")

        self.antl_entry = Entry(self.antl_main_frame)
        self.antl_entry.config(font=self.cid_font_large_no_line, width=30)
        self.antl_entry.place(x="300", y="100", anchor="center")

        self.antl_entry_button = Label(self.antl_main_frame)
        self.antl_entry_button.config(bg=self.project_bar_colour, font=self.cid_font_large_no_line, text="Add Note",
                                      width=10)
        self.antl_entry_button.place(x="300", y="160", anchor="center")

        self.antl_entry_button.bind("<Enter>", lambda _: self.antl_entry_button.config(relief="ridge"))
        self.antl_entry_button.bind("<Leave>", lambda _: self.antl_entry_button.config(relief="flat"))
        self.antl_entry_button.bind("<Button-1>", self.add_note_button_function)

    def add_note_button_function(self, event):
        self.note_to_add = self.antl_entry.get()
        if self.note_to_add == "":
            messagebox.showinfo(title="No Data", message="Entry Field Left Blank", parent=self.add_note_top_level)
        else:
            sci_sounds.play_click()
            self.add_note_top_level.destroy()
            self.add_note_to_dict(self.client_info_key, self.note_to_add)

    def add_to_materials_and_labour(self):
        sci_sounds.play_click()
        self.job_details_frame.grid_forget()
        self.service_address_frame.grid_forget()
        self.other_details_frame.grid_forget()
        self.client_info_frame.grid_forget()
        self.client_info_dropdown_menu.grid_forget()
        self.contact_details_frame.grid_forget()
        self.sci_root.title("Database System - Add To Materials And Labour")
        self.back_button = Label(self.materials_and_labour_frame)
        self.back_button.config(font=self.cid_font_large_no_line, bg=self.project_bar_colour,
                                text="Back To Client Info")
        self.back_button.grid(row=2, column=0, sticky="we", pady=(17, 0))
        self.back_button.bind("<Enter>", lambda _: self.back_button.config(relief="ridge"))
        self.back_button.bind("<Leave>", lambda _: self.back_button.config(relief="flat"))
        self.back_button.bind("<Button-1>", self.back_to_client)
        self.create_add_mat_and_lab_page(self.client_info_key, self.sci_info_frame, self.sci_root,
                                         self.materials_and_labour_frame, self.mat_and_labour_listbox)

    def view_materials_and_labour_toplevel_maker(self):
        self.vmalt_toplevel = Toplevel(self.sci_root)
        self.vmalt_toplevel.title("View Materials And Labour")
        self.vmalt_toplevel.iconbitmap("pictures/gj.ico")
        self.vmalt_toplevel.config(bg=self.project_background_colour)
        self.vmalt_toplevel.geometry("1000x600")
        self.vmalt_toplevel.resizable(0, 0)
        self.create_vmalt_frames()
        self.create_vmalt_label()
        self.create_vmalt_listbox_and_scroller()
        self.populate_vmalt_listbox()

    def create_vmalt_frames(self):
        self.vmalt_top_frame = Frame(self.vmalt_toplevel)
        self.vmalt_top_frame.config(height=75, width=1000, bg=self.project_bar_colour)
        self.vmalt_top_frame.grid(row=0, column=0)
        self.vmalt_top_frame.grid_propagate(False)
        self.vmalt_main_frame = Frame(self.vmalt_toplevel)
        self.vmalt_main_frame.config(height=450, width=1000, bg=self.project_background_colour)
        self.vmalt_main_frame.grid(row=1, column=0)
        self.vmalt_main_frame.grid_propagate(False)
        self.vmalt_bottom_frame = Frame(self.vmalt_toplevel)
        self.vmalt_bottom_frame.config(height=75, width=1000, bg=self.project_bar_colour)
        self.vmalt_bottom_frame.grid(row=2, column=0)
        self.vmalt_bottom_frame.grid_propagate(False)

    def create_vmalt_label(self):
        self.vmalt_client_label = Label(self.vmalt_main_frame)
        self.vmalt_client_label.config(text=f"Viewing materials and labour for client - "
                                            f"{self.client_dict['name']}", bg=self.project_background_colour,
                                       font=self.cid_font)
        self.vmalt_client_label.grid(row=0, column=0, pady=25, sticky="w", padx=20)

    def create_vmalt_listbox_and_scroller(self):
        self.vmalt_listbox = Listbox(self.vmalt_main_frame)
        self.vmalt_listbox.config(height=14, width=80, bg=self.label_background_colour, borderwidth=0,
                                  highlightthickness=0, selectbackground="white", selectforeground="black",
                                  activestyle="none", font=self.cid_font)
        self.vmalt_listbox.grid(row=1, column=0, padx=20, pady=(0, 25))

        self.vmalt_scroller = Scrollbar(self.vmalt_listbox)
        self.vmalt_listbox.config(yscrollcommand=self.vmalt_scroller.set)
        self.vmalt_scroller.config(command=self.vmalt_listbox.yview)

    def populate_vmalt_listbox(self):
        vmal_list = self.populate_mat_lab_listbox(self.client_info_key, display_full=True)
        for item in vmal_list:
            self.vmalt_listbox.insert(END, item)

    def back_to_client(self, event):
        sci_sounds.play_click()
        self.atmal_frame.destroy()
        self.populate_client_info_page(self.client_info_key, self.sci_frame, self.sci_root)

    def add_payment_to_account(self):
        sci_sounds.play_click()
        self.apto_top_level = Toplevel(self.sci_root)
        self.apto_top_level.title("Add Payment To Account")
        self.apto_top_level.config(bg=self.project_background_colour)
        self.apto_top_level.geometry("300x200")
        self.apto_top_level.resizable(0, 0)
        self.apto_top_level.iconbitmap("pictures/gj.ico")
        self.create_apto_frames()
        self.create_apto_labels_entries_buttons()

    def create_apto_frames(self):
        self.apto_top_frame = Frame(self.apto_top_level)
        self.apto_top_frame.config(width=300, height=25, bg=self.project_bar_colour)
        self.apto_top_frame.grid(row=0, column=0)
        self.apto_main_frame = Frame(self.apto_top_level)
        self.apto_main_frame.config(width=300, height=150, bg=self.project_background_colour)
        self.apto_main_frame.grid(row=1, column=0)
        self.apto_main_frame.grid_propagate(False)
        self.apto_bottom_frame = Frame(self.apto_top_level)
        self.apto_bottom_frame.config(width=300, height=25, bg=self.project_bar_colour)
        self.apto_bottom_frame.grid(row=2, column=0)

    def create_apto_labels_entries_buttons(self):
        self.apto_header_label = Label(self.apto_main_frame)
        self.apto_header_label.config(text="Add Payment To Account", font=self.cid_font,
                                      bg=self.project_background_colour)
        self.apto_header_label.place(x="150", y="30", anchor="center")
        self.apto_entry = Entry(self.apto_main_frame)
        self.apto_entry.config(width=10, font=self.cid_font)
        self.apto_entry.place(x="150", y="70", anchor="center")
        self.apto_button = Label(self.apto_main_frame)
        self.apto_button.config(font=self.cid_font, text="Add Payment", bg=self.project_bar_colour, width=13)
        self.apto_button.place(x="150", y="115", anchor="center")
        self.apto_button.bind("<Enter>", lambda _: self.apto_button.config(relief="ridge"))
        self.apto_button.bind("<Leave>", lambda _: self.apto_button.config(relief="flat"))
        self.apto_button.bind("<Button-1>", self.add_payment_to_dict)

    def add_payment_to_dict(self, event):
        sci_sounds.play_click()
        payment_to_add = self.apto_entry.get()
        if payment_to_add == "":
            messagebox.showinfo("No Value To Add", message="Amount Entry Has Been Left Blank",
                                parent=self.apto_top_level)
        else:
            message = messagebox.askyesno("Add Payment To Account?", message=f"Would You Like To Add A Payment Of "
                                          f"{payment_to_add} To This Account?", parent=self.apto_top_level)
            if message:
                try:
                    self.add_payment(self.client_info_key, payment_to_add)
                    self.apto_top_level.destroy()
                    self.client_dict = self.create_client_info_dict(self.client_info_key)
                    to_pay = format(float(self.client_dict['price']) - float(self.client_dict['amount_paid']), '.2f')
                    self.to_pay_amount_label.config(text=f"Amount Outstanding: £{to_pay}")
                except ValueError:
                    messagebox.showinfo("Bad Entry", "Value Entered Isn't A Number!")
                    self.apto_entry.delete(0, END)
            else:
                self.apto_entry.delete(0, END)

    def view_notes_toplevel_maker(self):
        self.vn_toplevel = Toplevel(self.sci_root)
        self.vn_toplevel.title("View Client Notes")
        self.vn_toplevel.iconbitmap("pictures/gj.ico")
        self.vn_toplevel.config(bg=self.project_background_colour)
        self.vn_toplevel.geometry("800x600")
        self.vn_toplevel.resizable(0, 0)
        self.create_vn_frames()
        self.create_vn_label()
        self.create_vn_listbox_and_scroller()
        self.populate_vn_listbox()

    def create_vn_frames(self):
        self.vn_top_frame = Frame(self.vn_toplevel)
        self.vn_top_frame.config(height=75, width=800, bg=self.project_bar_colour)
        self.vn_top_frame.grid(row=0, column=0)
        self.vn_top_frame.grid_propagate(False)
        self.vn_main_frame = Frame(self.vn_toplevel)
        self.vn_main_frame.config(height=450, width=800, bg=self.project_background_colour)
        self.vn_main_frame.grid(row=1, column=0)
        self.vn_main_frame.grid_propagate(False)
        self.vn_bottom_frame = Frame(self.vn_toplevel)
        self.vn_bottom_frame.config(height=75, width=800, bg=self.project_bar_colour)
        self.vn_bottom_frame.grid(row=2, column=0)
        self.vn_bottom_frame.grid_propagate(False)

    def create_vn_label(self):
        self.vn_client_label = Label(self.vn_main_frame)
        self.vn_client_label.config(text=f"Viewing Notes for client - "
                                         f"{self.client_dict['name']}", bg=self.project_background_colour,
                                         font=self.cid_font)
        self.vn_client_label.grid(row=0, column=0, pady=25, sticky="w", padx=20)

    def create_vn_listbox_and_scroller(self):
        self.vn_listbox = Listbox(self.vn_main_frame)
        self.vn_listbox.config(height=14, width=63, bg=self.label_background_colour, borderwidth=0,
                               highlightthickness=0, selectbackground="white", selectforeground="black",
                               activestyle="none", font=self.cid_font)
        self.vn_listbox.grid(row=1, column=0, padx=20, pady=(0, 25))

        self.vn_scroller = Scrollbar(self.vn_listbox)
        self.vn_listbox.config(yscrollcommand=self.vn_scroller.set)
        self.vn_scroller.config(command=self.vn_listbox.yview)

    def populate_vn_listbox(self):
        vn_list = self.view_notes(self.client_info_key)
        for item in vn_list:
            self.vn_listbox.insert(END, item)

    def back_from_cci(self):
        self.cci_info_frame.destroy()
        self.populate_client_info_page(self.client_info_key, self.sci_frame, self.sci_root)

    def open_change_client_info(self):
        sci_sounds.play_click()
        self.sci_info_frame.destroy()
        self.create_change_client_info(self.client_key, self.sci_frame, self.sci_root, self.client_dict,
                                       self.back_from_cci)
        self.sci_root.title("Database System - Change Client Info")
