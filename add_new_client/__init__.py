from tkinter import *
from sound_player import SoundPlayer
from data_handler import DataCreator, ClientListPopulate, FavouriteInfoDictCreate

anc_sounds = SoundPlayer()


class AddNewClient(DataCreator, ClientListPopulate, FavouriteInfoDictCreate):
    def __init__(self):
        DataCreator.__init__(self)
        ClientListPopulate.__init__(self)
        FavouriteInfoDictCreate.__init__(self)
        self.project_background_colour = "#8e94a4"
        self.project_bar_colour = "#3b415b"
        self.label_background_colour = "white"
        self.test_colour = "black"
        self.height = 720
        self.width = 1280
        self.frame_height = 496
        self.add_new_client_font = ("Arial", "20")
        self.cid_font = ("Arial", "16")
        self.cid_font_large = ("Arial", "24", "underline")
        self.cid_font_large_no_line = ("Arial", "24")
        self.cid_font_small = ("Arial", "10")
        self.cid_font_underline = ("Arial", "16", "underline")

    def start_anc_page(self, main_frame, main_root):
        self.main_frame = main_frame
        self.main_root = main_root
        self.create_anc_page()

    def create_anc_page(self):
        self.create_anc_frames()
        self.create_new_customer_name_and_address_labels()
        self.create_anc_service()
        self.create_email_and_phone()
        self.create_job_desc_and_job_address()
        self.create_instructions()
        self.create_entries()
        self.create_buttons()

    def create_anc_frames(self):
        self.anc_info_frame = Frame(self.main_frame)
        self.anc_info_frame.config(width=self.width, height=self.frame_height, borderwidth=0, highlightthickness=0,
                                   bg=self.project_background_colour)
        self.anc_info_frame.grid(row=0, column=0, columnspan=5, padx=30)

        self.customer_details_frame = Frame(self.anc_info_frame)
        self.customer_details_frame.config(width=600, height=self.frame_height, borderwidth=0, highlightthickness=0,
                                           bg=self.project_background_colour)
        self.customer_details_frame.grid(row=0, column=0, columnspan=3)

    def create_new_customer_name_and_address_labels(self):
        self.new_customer_name_label = Label(self.customer_details_frame)
        self.new_customer_name_label.config(font=self.add_new_client_font, bg=self.project_background_colour,
                                            text="Client Name:")
        self.new_customer_name_label.grid(row=0, column=0, sticky="w", pady=5)

        self.new_customer_address_label = Label(self.customer_details_frame)
        self.new_customer_address_label.config(font=self.add_new_client_font, bg=self.project_background_colour,
                                               text="Address:")
        self.new_customer_address_label.grid(row=1, column=0, sticky="w", pady=5)

        self.new_customer_name_label_entry = Entry(self.customer_details_frame)
        self.new_customer_name_label_entry.config(font=self.add_new_client_font, width=30)
        self.new_customer_name_label_entry.grid(row=0, column=1)

    def create_anc_service(self):
        self.service_address_line1_entry = Entry(self.customer_details_frame)
        self.service_address_line1_entry.config(font=self.add_new_client_font, width=30)
        self.service_address_line1_entry.grid(row=1, column=1, pady=10)
        self.service_address_line2_entry = Entry(self.customer_details_frame)
        self.service_address_line2_entry.config(font=self.add_new_client_font, width=30)
        self.service_address_line2_entry.grid(row=2, column=1, pady=10)
        self.service_address_line3_entry = Entry(self.customer_details_frame)
        self.service_address_line3_entry.config(font=self.add_new_client_font, width=30)
        self.service_address_line3_entry.grid(row=3, column=1, pady=10)
        self.new_customer_postcode_label = Label(self.customer_details_frame)
        self.new_customer_postcode_label.config(font=self.add_new_client_font, bg=self.project_background_colour,
                                                text="Postcode:")
        self.new_customer_postcode_label.grid(row=4, column=0, pady=10, sticky="w")
        self.service_postcode_entry = Entry(self.customer_details_frame)
        self.service_postcode_entry.config(font=self.add_new_client_font, width=8)
        self.service_postcode_entry.grid(row=4, column=1, pady=10, sticky="w")

    def create_email_and_phone(self):
        self.customer_email_label = Label(self.customer_details_frame, text="Client Email:")
        self.customer_email_label.config(font=self.add_new_client_font, bg=self.project_background_colour)
        self.customer_email_label.grid(row=5, column=0, pady=(40, 10), sticky="w")
        self.customer_email_entry = Entry(self.customer_details_frame)
        self.customer_email_entry.config(font=self.add_new_client_font, width=30)
        self.customer_email_entry.grid(row=5, column=1, pady=(40, 10))

        self.customer_mobile_label = Label(self.customer_details_frame)
        self.customer_mobile_label.config(font=self.add_new_client_font, bg=self.project_background_colour,
                                          text="Mobile Number:")
        self.customer_mobile_label.grid(row=6, column=0, pady=10)
        self.customer_mobile_entry = Entry(self.customer_details_frame)
        self.customer_mobile_entry.config(font=self.add_new_client_font, width=15)
        self.customer_mobile_entry.grid(row=6, column=1, pady=10, sticky="w")

        self.customer_landline_label = Label(self.customer_details_frame)
        self.customer_landline_label.config(font=self.add_new_client_font, bg=self.project_background_colour,
                                            text="Home Number:")
        self.customer_landline_label.grid(row=7, column=0, pady=10)
        self.customer_landline_entry = Entry(self.customer_details_frame)
        self.customer_landline_entry.config(font=self.add_new_client_font, width=15)
        self.customer_landline_entry.grid(row=7, column=1, pady=10, sticky="w")

    def create_job_desc_and_job_address(self):
        self.service_address_frame = Frame(self.anc_info_frame)
        self.service_address_frame.config(bg=self.project_background_colour, borderwidth=0, highlightthickness=0,
                                          height=self.frame_height, width=500)
        self.service_address_frame.grid(row=0, column=3, columnspan=2, padx=60)
        self.service_address_frame.grid_propagate(False)

        self.job_desc_label = Label(self.service_address_frame, text="Job Title")
        self.job_desc_label.config(font=self.add_new_client_font, bg=self.project_background_colour)
        self.job_desc_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

        self.job_desc_entry = Entry(self.service_address_frame)
        self.job_desc_entry.config(font=self.add_new_client_font, width=30)
        self.job_desc_entry.grid(row=1, column=0, columnspan=3, pady=10)

        self.service_address_label = Label(self.service_address_frame, text="Job Address")
        self.service_address_label.config(font=self.add_new_client_font, bg=self.project_background_colour)
        self.service_address_label.grid(row=2, column=0, columnspan=3, pady=(20, 10))

    def create_instructions(self):
        self.service_address_instruction_label = Label(self.service_address_frame,
                                                       text=("leave all fields blank if job address is the same as"
                                                             " service address"))
        self.service_address_instruction_label.config(font=("Arial", "8"), bg=self.project_background_colour)
        self.service_address_instruction_label.grid(row=2, column=0, columnspan=3, pady=(70, 0))

    def create_entries(self):
        self.customer_address_line_1_entry = Entry(self.service_address_frame)
        self.customer_address_line_1_entry.config(font=self.add_new_client_font, width=30)
        self.customer_address_line_1_entry.grid(row=3, column=0, columnspan=3, pady=10)
        self.customer_address_line_2_entry = Entry(self.service_address_frame)
        self.customer_address_line_2_entry.config(font=self.add_new_client_font, width=30)
        self.customer_address_line_2_entry.grid(row=4, column=0, columnspan=3, pady=10)
        self.customer_address_line_3_entry = Entry(self.service_address_frame)
        self.customer_address_line_3_entry.config(font=self.add_new_client_font, width=30)
        self.customer_address_line_3_entry.grid(row=5, column=0, columnspan=3, pady=10)
        self.customer_postcode_entry = Entry(self.service_address_frame)
        self.customer_postcode_entry.config(font=self.add_new_client_font, width=8)
        self.customer_postcode_entry.grid(row=6, column=0, columnspan=3, pady=10, sticky="w")

    def create_buttons(self):
        self.add_details_button = Label(self.service_address_frame)
        self.add_details_button.config(font=("Arial", "28"), bg=self.project_bar_colour,
                                       text="Add New Client")
        self.add_details_button.grid(row=7, column=0, pady=20, columnspan=2, ipadx=15)
        self.add_details_button.bind("<Enter>", lambda _: self.add_details_button.config(relief="ridge"))
        self.add_details_button.bind("<Leave>", lambda _: self.add_details_button.config
                                     (relief="flat"))
        self.add_details_button.bind("<Button-1>", self.add_client_to_database)

        self.check_var = BooleanVar()
        self.check_var.set(False)
        self.add_details_check = Checkbutton(self.service_address_frame, text="Add To Favourites?",
                                             variable=self.check_var, onvalue=True)
        self.add_details_check.config(bg=self.project_background_colour,
                                      activebackground=self.project_background_colour, font=("Arial", "10"))
        self.add_details_check.grid(row=7, column=2, sticky="w", padx=10)
        self.main_root.bind("<Return>", self.open_favourites)

    def open_favourites(self, event):
        self.favourite_list = self.clv_populate_favourites()
        self.favourites_keys = self.clv_dict_key_maker()
        self.favourites_top = Toplevel(self.main_root)
        self.favourites_top.title("Favourites")
        self.favourites_top.iconbitmap("pictures/gj.ico")
        self.favourites_top.geometry("700x600")
        self.favourites_top.config(bg=self.project_background_colour)
        self.favourites_top.resizable(0, 0)
        self.favourites_top.grid_propagate(False)
        self.create_favourites_frames()
        self.populate_favourites()

    def create_favourites_frames(self):
        self.top_frame = Frame(self.favourites_top)
        self.top_frame.config(bg=self.project_bar_colour, width=700, height=50)
        self.top_frame.grid(row=0, column=0)

        self.middle_frame = Frame(self.favourites_top)
        self.middle_frame.config(bg=self.project_background_colour, width=700, height=500)
        self.middle_frame.grid(row=1, column=0)
        self.middle_frame.grid_propagate(False)

        self.bottom_frame = Frame(self.favourites_top)
        self.bottom_frame.config(bg=self.project_bar_colour, width=700, height=50)
        self.bottom_frame.grid(row=2, column=0)

        self.header_label = Label(self.middle_frame)
        self.header_label.config(text="Click On Client To Add Details To Entry Fields",
                                 bg=self.project_background_colour, font=self.cid_font_large_no_line)
        self.header_label.grid(row=0, column=0, pady=20, sticky="we", padx=20)

    def populate_favourites(self):
        self.favourites_list_box = Listbox(self.middle_frame)
        self.favourites_list_box.config(height=16, width=55, bg=self.label_background_colour, borderwidth=0,
                                        highlightthickness=0, selectbackground="white", selectforeground="black",
                                        activestyle="none", font=self.cid_font)
        self.favourites_list_box.grid(row=1, column=0, padx=20)
        for item in self.favourite_list:
            self.favourites_list_box.insert(END, item)
        self.favourites_list_box.bind("<<ListboxSelect>>", self.add_selected_favourite_to_anc)

        self.favourites_scroller = Scrollbar(self.favourites_list_box)
        self.favourites_list_box.config(yscrollcommand=self.favourites_scroller.set)
        self.favourites_scroller.config(command=self.favourites_list_box.yview)

    def add_selected_favourite_to_anc(self, event):
        anc_sounds.play_click()
        try:
            favourite_client_key = str(self.favourites_keys[self.favourites_list_box.curselection()[0]])
            favourite_client_dict = self.create_favourite_info_dict(favourite_client_key)
            self.new_customer_name_label_entry.insert(0, favourite_client_dict["name"])
            self.customer_email_entry.insert(0, favourite_client_dict["email"])
            self.customer_mobile_entry.insert(0, favourite_client_dict["mobile_number"])
            self.customer_landline_entry.insert(0, favourite_client_dict["home_number"])
            self.service_address_line1_entry.insert(0, favourite_client_dict["service_address"]["service_add_1"])
            self.service_address_line2_entry.insert(0, favourite_client_dict["service_address"]["service_add_2"])
            self.service_address_line3_entry.insert(0, favourite_client_dict["service_address"]["service_add_3"])
            self.service_postcode_entry.insert(0, favourite_client_dict["service_address"]["service_postcode"])
            self.favourites_top.destroy()
        except IndexError:
            pass

    def add_client_to_database(self, event):
        anc_sounds.play_click()
        anc_service_name = self.new_customer_name_label_entry.get()
        anc_service_add_1 = self.service_address_line1_entry.get()
        anc_service_add_2 = self.service_address_line2_entry.get()
        anc_service_add_3 = self.service_address_line3_entry.get()
        anc_service_postcode = self.service_postcode_entry.get()
        anc_home_number = self.customer_landline_entry.get()
        anc_mobile_number = self.customer_mobile_entry.get()
        anc_email = self.customer_email_entry.get()
        anc_job_desc = self.job_desc_entry.get()
        check_list = [self.customer_address_line_1_entry.get(), self.customer_address_line_2_entry.get(),
                      self.customer_address_line_3_entry.get(), self.customer_postcode_entry.get()]
        self.job_same_as_service = True
        for item in check_list:
            if item != "":
                self.job_same_as_service = False
            else:
                pass

        if self.job_same_as_service:

            anc_add_1 = self.service_address_line1_entry.get()
            anc_add_2 = self.service_address_line2_entry.get()
            anc_add_3 = self.service_address_line3_entry.get()
            anc_postcode = self.service_postcode_entry.get()
        else:
            anc_add_1 = self.customer_address_line_1_entry.get()
            anc_add_2 = self.customer_address_line_2_entry.get()
            anc_add_3 = self.customer_address_line_3_entry.get()
            anc_postcode = self.customer_postcode_entry.get()

        fave = self.check_var.get()
        self.check_var.set(False)

        self.add_client(anc_service_name, address_1=anc_add_1, address_2=anc_add_2, address_3=anc_add_3,
                        postcode=anc_postcode, home_number=anc_home_number, mobile_number=anc_mobile_number,
                        email=anc_email, job_desc=anc_job_desc, service_address_1=anc_service_add_1,
                        service_address_2=anc_service_add_2, service_address_3=anc_service_add_3,
                        service_postcode=anc_service_postcode, favourite=fave)
        self.delete_entries()

    def delete_entries(self):
        self.new_customer_name_label_entry.delete(0, END)
        self.customer_address_line_1_entry.delete(0, END)
        self.customer_address_line_2_entry.delete(0, END)
        self.customer_address_line_3_entry.delete(0, END)
        self.customer_postcode_entry.delete(0, END)
        self.customer_landline_entry.delete(0, END)
        self.customer_mobile_entry.delete(0, END)
        self.customer_email_entry.delete(0, END)
        self.job_desc_entry.delete(0, END)
        self.service_address_line1_entry.delete(0, END)
        self.service_address_line2_entry.delete(0, END)
        self.service_address_line3_entry.delete(0, END)
        self.service_postcode_entry.delete(0, END)
