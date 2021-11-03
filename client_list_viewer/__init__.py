from tkinter import messagebox
from tkinter import *
from sound_player import SoundPlayer
from data_handler import ClientListPopulate
from show_client_info import ClientInfoDisplay

clv_sounds = SoundPlayer()


class DisplayClientList(ClientInfoDisplay, ClientListPopulate):
    """Shows Client Info"""
    def __init__(self):
        ClientInfoDisplay.__init__(self)
        ClientListPopulate.__init__(self)
        self.project_background_colour = "#8e94a4"
        self.project_bar_colour = "#3b415b"
        self.test_colour = "black"
        self.height = 720
        self.width = 1280
        self.frame_height = 496
        self.dcl_font = ("Arial", "20")
        self.dcl_font_large = ("Arial", "24")
        self.filename = "client_database.json"

    def display_client_list(self, main_frame, dcl_root):
        """Displays client list on client list viewer"""
        self.main_frame = main_frame
        self.dcl_root = dcl_root

        self.dcl_main_frame = Frame(self.main_frame)
        self.dcl_main_frame.config(bg=self.project_background_colour, height=self.frame_height, width=self.width,
                                   highlightthickness=0, borderwidth=0)
        self.dcl_main_frame.grid(row=0, column=0)
        self.dcl_main_frame.grid_propagate(False)

        # Search function widgets

        self.search_frame = Frame(self.dcl_main_frame)
        self.search_frame.config(bg=self.project_background_colour, width=self.width, height=100)
        self.search_frame.grid(row=1, column=0)
        self.search_frame.grid_propagate(False)

        self.search_label = Label(self.search_frame, text="Search Client Database:")
        self.search_label.config(font=self.dcl_font_large, bg=self.project_background_colour)
        self.search_label.grid(row=0, column=0, pady=(40, 0), padx=(35, 0), sticky="w")

        self.search_entry = Entry(self.search_frame)
        self.search_entry.config(font=self.dcl_font_large, width=24)
        self.search_entry.grid(row=0, column=1, pady=(40, 0), padx=10, sticky="w")

        self.search_button = Label(self.search_frame, text="Search")
        self.search_button.config(font=self.dcl_font_large, bg=self.project_bar_colour)
        self.search_button.grid(row=0, column=2, pady=(40, 0), padx=10, sticky="w")

        self.search_button.bind("<Enter>", lambda _: self.search_button.config(relief="ridge"))
        self.search_button.bind("<Leave>", lambda _: self.search_button.config(relief="flat"))
        self.search_button.bind("<Button-1>", self.client_search)

        self.refresh_button = Label(self.search_frame, text="Refresh Client List")
        self.refresh_button.config(font=self.dcl_font_large, bg=self.project_bar_colour)
        self.refresh_button.grid(row=0, column=3, pady=(40, 0), padx=10, sticky="w")


    def display_all_clients(self):
        """Displays a list of all clients"""
        self.to_display = self.clv_populate_all()
        self.dict_keys = self.clv_dict_key_maker()

        self.client_listbox = Listbox(self.dcl_main_frame)
        for item in self.to_display:
            self.client_listbox.insert(END, item)  # Place items from dict here
        self.client_listbox.config(height=12, width=81, font=self.dcl_font)
        self.client_listbox.grid(row=0, column=0, sticky="n,s")

        self.client_listbox_scroller = Scrollbar(self.client_listbox)
        self.client_listbox.config(yscrollcommand=self.client_listbox_scroller.set)
        self.client_listbox_scroller.config(command=self.client_listbox.yview)

        self.client_listbox.bind("<<ListboxSelect>>", self.get_listbox_info)

        self.refresh_button.bind("<Enter>", lambda _: self.refresh_button.config(relief="ridge"))
        self.refresh_button.bind("<Leave>", lambda _: self.refresh_button.config(relief="flat"))
        self.refresh_button.bind("<Button-1>", self.refresh_client_list)

        if " Client List Is Empty" in self.to_display:
            self.client_listbox.config(selectbackground="white", selectforeground="black", activestyle="none")

    def display_quotes_pending_clients(self):
        """Displays a list of all clients with pending quotes"""
        self.to_display = self.clv_populate_quotes_pending()
        self.dict_keys = self.clv_dict_key_maker()

        self.client_listbox = Listbox(self.dcl_main_frame)
        for item in self.to_display:
            self.client_listbox.insert(END, item)  # Place items from dict here
        self.client_listbox.config(height=12, width=81, font=self.dcl_font)
        self.client_listbox.grid(row=0, column=0, sticky="n,s")

        self.client_listbox_scroller = Scrollbar(self.client_listbox)
        self.client_listbox.config(yscrollcommand=self.client_listbox_scroller.set)
        self.client_listbox_scroller.config(command=self.client_listbox.yview)

        self.client_listbox.bind("<<ListboxSelect>>", self.get_listbox_info)

        self.refresh_button.bind("<Enter>", lambda _: self.refresh_button.config(relief="ridge"))
        self.refresh_button.bind("<Leave>", lambda _: self.refresh_button.config(relief="flat"))
        self.refresh_button.bind("<Button-1>", self.refresh_pending_quotes_list)

        if " No Pending Quotes" in self.to_display:
            self.client_listbox.config(selectbackground="white", selectforeground="black", activestyle="none")

    def display_quotes_accepted_clients(self):
        """Displays a list of all clients with accepted quotes"""
        self.to_display = self.clv_populate_quotes_accepted()
        self.dict_keys = self.clv_dict_key_maker()

        self.client_listbox = Listbox(self.dcl_main_frame)
        for item in self.to_display:
            self.client_listbox.insert(END, item)
        self.client_listbox.config(height=12, width=81, font=self.dcl_font)
        self.client_listbox.grid(row=0, column=0, sticky="n,s")

        self.client_listbox_scroller = Scrollbar(self.client_listbox)
        self.client_listbox.config(yscrollcommand=self.client_listbox_scroller.set)
        self.client_listbox_scroller.config(command=self.client_listbox.yview)

        self.client_listbox.bind("<<ListboxSelect>>", self.get_listbox_info)

        self.refresh_button.bind("<Enter>", lambda _: self.refresh_button.config(relief="ridge"))
        self.refresh_button.bind("<Leave>", lambda _: self.refresh_button.config(relief="flat"))
        self.refresh_button.bind("<Button-1>", self.refresh_accepted_quotes_list)

        if " No Accepted Quotes" in self.to_display:
            self.client_listbox.config(selectbackground="white", selectforeground="black", activestyle="none")

    def display_awaiting_payment_clients(self):
        """Displays a list of all clients with accepted quotes"""
        self.to_display = self.clv_populate_awaiting_payment()
        self.dict_keys = self.clv_dict_key_maker()

        self.client_listbox = Listbox(self.dcl_main_frame)
        for item in self.to_display:
            self.client_listbox.insert(END, item)  # Place items from dict here
        self.client_listbox.config(height=12, width=81, font=self.dcl_font)
        self.client_listbox.grid(row=0, column=0, sticky="n,s")

        self.client_listbox_scroller = Scrollbar(self.client_listbox)
        self.client_listbox.config(yscrollcommand=self.client_listbox_scroller.set)
        self.client_listbox_scroller.config(command=self.client_listbox.yview)

        self.client_listbox.bind("<<ListboxSelect>>", self.get_listbox_info)

        self.refresh_button.bind("<Enter>", lambda _: self.refresh_button.config(relief="ridge"))
        self.refresh_button.bind("<Leave>", lambda _: self.refresh_button.config(relief="flat"))
        self.refresh_button.bind("<Button-1>", self.refresh_awaiting_payment_list)

        if " No Jobs Awaiting Payment" in self.to_display:
            self.client_listbox.config(selectbackground="white", selectforeground="black", activestyle="none")

    def display_job_completed_clients(self):
        """Displays a list of all clients with accepted quotes"""
        self.to_display = self.clv_populate_jobs_completed()
        self.dict_keys = self.clv_dict_key_maker()

        self.client_listbox = Listbox(self.dcl_main_frame)
        for item in self.to_display:
            self.client_listbox.insert(END, item)
        self.client_listbox.config(height=12, width=81, font=self.dcl_font)
        self.client_listbox.grid(row=0, column=0, sticky="n,s")

        self.client_listbox_scroller = Scrollbar(self.client_listbox)
        self.client_listbox.config(yscrollcommand=self.client_listbox_scroller.set)
        self.client_listbox_scroller.config(command=self.client_listbox.yview)

        self.client_listbox.bind("<<ListboxSelect>>", self.get_listbox_info)

        self.refresh_button.bind("<Enter>", lambda _: self.refresh_button.config(relief="ridge"))
        self.refresh_button.bind("<Leave>", lambda _: self.refresh_button.config(relief="flat"))
        self.refresh_button.bind("<Button-1>", self.refresh_jobs_completed_list)

        if " No Completed Jobs" in self.to_display:
            self.client_listbox.config(selectbackground="white", selectforeground="black", activestyle="none")

    def get_listbox_info(self, event):
        """Gets client key details to display in show_client info, calls populate client info page method"""
        try:
            self.client_key = str(self.dict_keys[self.client_listbox.curselection()[0]])
            self.dcl_main_frame.destroy()
            self.populate_client_info_page(self.client_key, self.main_frame, self.dcl_root)
            self.dcl_root.title("Database System - Display Client Info")
            clv_sounds.play_click()
        except IndexError:
            pass

    def client_search(self, event):
        """Calls search method and repopulates page"""
        if self.search_entry.get() == "":
            messagebox.showinfo(title="Missing Parameter", message="No search information provided")
        else:
            clv_sounds.play_click()
            self.to_display = self.search_populate(self.search_entry.get())
            self.dict_keys = self.clv_dict_key_maker()
            self.search_entry.delete(0, END)
            self.client_listbox.delete(0, END)
            for item in self.to_display:
                self.client_listbox.insert(END, item)

    def refresh_client_list(self, event):
        """Deletes and repopulates listbox with all client list"""
        clv_sounds.play_click()
        self.client_listbox.delete(0, END)
        self.to_display = self.clv_populate_all()
        self.dict_keys = self.clv_dict_key_maker()
        for item in self.to_display:
            self.client_listbox.insert(END, item)

    def refresh_pending_quotes_list(self, event):
        """Deletes and repopulates listbox with quotes pending client list"""
        clv_sounds.play_click()
        self.client_listbox.delete(0, END)
        self.to_display = self.clv_populate_quotes_pending()
        self.dict_keys = self.clv_dict_key_maker()
        for item in self.to_display:
            self.client_listbox.insert(END, item)

    def refresh_accepted_quotes_list(self, event):
        """Deletes and repopulates listbox with accepted quotes list"""
        clv_sounds.play_click()
        self.client_listbox.delete(0, END)
        self.to_display = self.clv_populate_quotes_accepted()
        self.dict_keys = self.clv_dict_key_maker()
        for item in self.to_display:
            self.client_listbox.insert(END, item)

    def refresh_awaiting_payment_list(self, event):
        """Deletes and repopulates listbox with awaiting payment list"""
        clv_sounds.play_click()
        self.client_listbox.delete(0, END)
        self.to_display = self.clv_populate_awaiting_payment()
        self.dict_keys = self.clv_dict_key_maker()
        for item in self.to_display:
            self.client_listbox.insert(END, item)

    def refresh_jobs_completed_list(self, event):
        """Deletes and repopulates listbox with jobs completed list"""
        clv_sounds.play_click()
        self.client_listbox.delete(0, END)
        self.to_display = self.clv_populate_jobs_completed()
        self.dict_keys = self.clv_dict_key_maker()
        for item in self.to_display:
            self.client_listbox.insert(END, item)
















