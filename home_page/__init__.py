from tkinter import *
from PIL import ImageTk, Image

from sound_player import SoundPlayer
from add_new_client import AddNewClient
from client_list_viewer import DisplayClientList

global gj_image
hp_sounds = SoundPlayer()


class HomePage(AddNewClient, DisplayClientList):
    """Class containing methods for home page"""
    def __init__(self):
        AddNewClient.__init__(self)
        DisplayClientList.__init__(self)
        self.project_background_colour = "#8e94a4"
        self.project_bar_colour = "#3b415b"

        self.test_colour = "black"
        self.height = 720
        self.width = 1280
        self.frame_height = 496

    def start_home(self, main_frame, home_button, main_root, start_cond):
        """Constructs home page"""
        try:
            self.anc_info_frame.destroy()
        except AttributeError:
            pass
        try:
            self.dcl_main_frame.destroy()
        except AttributeError:
            pass
        try:
            self.home_button.grid_forget()
        except AttributeError:
            pass
        try:
            self.sci_info_frame.destroy()
        except AttributeError:
            pass
        try:
            self.cci_info_frame.destroy()
        except AttributeError:
            pass

        self.home_button = home_button
        self.main_frame = main_frame
        self.main_root = main_root
        self.main_root.unbind("<Return>")
        self.start_cond = start_cond
        self.main_root.title("Database System")
        if self.start_cond:
            hp_sounds.play_click()

        self.homepage_frame = Frame(self.main_frame)
        self.homepage_frame.config(width=self.width, height=self.frame_height, bg=self.project_background_colour,
                                   borderwidth=0,
                                   highlightthickness=0)
        self.homepage_frame.grid(row=0, column=0, columnspan=5, padx=150)

        self.homepage_image_frame = Frame(self.homepage_frame)

        global gj_image
        gj_image = ImageTk.PhotoImage(Image.open("pictures/gj.png"))
        self.homepage_image_frame.config(height=500, width=500, highlightthickness=0, borderwidth=0)
        self.homepage_image_frame.grid(row=0, column=0, columnspan=2, padx=(25, 0), pady=40)
        self.homepage_image_label = Label(self.homepage_image_frame, image=gj_image, highlightthickness=0,
                                          borderwidth=0)
        self.homepage_image_label.pack()

        self.options_frame = Frame(self.homepage_frame)
        self.options_frame.config(bg=self.project_background_colour, height=500, width=640)
        self.options_frame.grid(row=0, column=2, columnspan=3, sticky="w", padx=(25, 0), pady=5)

        # Options Widgets
        options_font = (None, "30")
        self.add_client_label = Label(self.options_frame)
        self.add_client_label.config(text="Add New Client", font=options_font, bg=self.project_background_colour)
        self.add_client_label.grid(row=0, column=0, sticky="w", pady=15, padx=45)
        self.add_client_label.bind("<Enter>", lambda _: self.add_client_label.config(bg=self.project_bar_colour))
        self.add_client_label.bind("<Leave>", lambda _: self.add_client_label.config(bg=self.project_background_colour))
        self.add_client_label.bind("<Button-1>", self.add_new_client)

        self.view_client_list_label = Label(self.options_frame)
        self.view_client_list_label.config(text="Client List", font=options_font, bg=self.project_background_colour)
        self.view_client_list_label.grid(row=1, column=0, sticky="w", pady=15, padx=45)
        self.view_client_list_label.bind("<Enter>", lambda _: self.view_client_list_label.config
                                         (bg=self.project_bar_colour))
        self.view_client_list_label.bind("<Leave>", lambda _: self.view_client_list_label.config
                                         (bg=self.project_background_colour))
        self.view_client_list_label.bind("<Button-1>", self.open_client_list)

        self.view_ip_quotes_label = Label(self.options_frame)
        self.view_ip_quotes_label.config(text="Quotes Pending", font=options_font, bg=self.project_background_colour)
        self.view_ip_quotes_label.grid(row=2, column=0, sticky="w", pady=15, padx=45)
        self.view_ip_quotes_label.bind("<Enter>", lambda _: self.view_ip_quotes_label.config(bg=self.project_bar_colour)
                                       )
        self.view_ip_quotes_label.bind("<Leave>", lambda _: self.view_ip_quotes_label.config
                                       (bg=self.project_background_colour))
        self.view_ip_quotes_label.bind("<Button-1>", self.open_quotes_pending)

        self.view_wip_label = Label(self.options_frame)
        self.view_wip_label.config(text="Accepted Quotes", font=options_font, bg=self.project_background_colour)
        self.view_wip_label.grid(row=3, column=0, sticky="w", pady=15, padx=45)
        self.view_wip_label.bind("<Enter>", lambda _: self.view_wip_label.config(bg=self.project_bar_colour))
        self.view_wip_label.bind("<Leave>", lambda _: self.view_wip_label.config(bg=self.project_background_colour))
        self.view_wip_label.bind("<Button-1>", self.open_quotes_accepted)

        self.view_unpaid_clients_label = Label(self.options_frame)
        self.view_unpaid_clients_label.config(text="Awaiting Payment", font=options_font,
                                              bg=self.project_background_colour)
        self.view_unpaid_clients_label.grid(row=4, column=0, sticky="w", pady=15, padx=45)
        self.view_unpaid_clients_label.bind("<Enter>", lambda _: self.view_unpaid_clients_label.config
                                            (bg=self.project_bar_colour))
        self.view_unpaid_clients_label.bind("<Leave>", lambda _: self.view_unpaid_clients_label.config
                                            (bg=self.project_background_colour))
        self.view_unpaid_clients_label.bind("<Button-1>", self.open_awaiting_payments)

        self.completed_jobs_label = Label(self.options_frame)
        self.completed_jobs_label.config(text="Completed Jobs", font=options_font, bg=self.project_background_colour)
        self.completed_jobs_label.grid(row=5, column=0, sticky="w", pady=15, padx=45)
        self.completed_jobs_label.bind("<Enter>", lambda _: self.completed_jobs_label.config
                                       (bg=self.project_bar_colour))
        self.completed_jobs_label.bind("<Leave>", lambda _: self.completed_jobs_label.config
                                       (bg=self.project_background_colour))
        self.completed_jobs_label.bind("<Button-1>", self.open_completed_jobs)

    def add_new_client(self, event):
        """Opens add new client page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width-120)
        self.start_anc_page(self.main_frame, self.main_root)
        self.main_root.title("Database System - Add New Client")

    def open_client_list(self, event):
        """Opens client list page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width-120)
        self.display_client_list(self.main_frame, self.main_root)
        self.display_all_clients()
        self.main_root.title("Database System - View Client List")

    def open_quotes_pending(self, event):
        """Open quotes pending page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width - 120)
        self.display_client_list(self.main_frame, self.main_root)
        self.display_quotes_pending_clients()
        self.main_root.title("Database System - View Quotes Pending List")

    def open_quotes_accepted(self, event):
        """Open quotes accepted page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width - 120)
        self.display_client_list(self.main_frame, self.main_root)
        self.display_quotes_accepted_clients()
        self.main_root.title("Database System - View Accepted Quotes List")

    def open_awaiting_payments(self, event):
        """Open awaiting payment page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width - 120)
        self.display_client_list(self.main_frame, self.main_root)
        self.display_awaiting_payment_clients()
        self.main_root.title("Database System - View Awaiting Payments List")

    def open_completed_jobs(self, event):
        """Open completed jobs page"""
        hp_sounds.play_click()
        self.homepage_frame.grid_forget()
        self.home_button.grid(row=0, column=0, pady=18, padx=self.width - 120)
        self.display_client_list(self.main_frame, self.main_root)
        self.display_job_completed_clients()
        self.main_root.title("Database System - View Completed Jobs List")
