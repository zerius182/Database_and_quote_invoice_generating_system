from tkinter import *
from tkinter import messagebox

from sound_player import SoundPlayer
from home_page import HomePage
from data_handler import BackUpDatabase, RecoverDatabase


class MainApp(SoundPlayer, HomePage, BackUpDatabase, RecoverDatabase):
    """Customer database and quote/invoice generating application"""
    #  Initial config
    def __init__(self):
        SoundPlayer.__init__(self)
        HomePage.__init__(self)
        BackUpDatabase.__init__(self)
        RecoverDatabase.__init__(self)
        root = Tk()

        project_background_colour = "#8e94a4"

        self.master = root
        self.start_up_jingle()
        self.master.iconbitmap("pictures/gj.ico")
        if self.master.winfo_screenheight() == 720 and self.master.winfo_screenwidth() == 1280:
            self.master.attributes("-fullscreen", True)
        else:
            self.master.geometry("1280x720")
        self.master.config(bg=project_background_colour)
        self.master.bind("<Escape>", self.exit)
        self.master.bind("<Shift-Tab>", self.manual_backup)
        self.master.bind("<Shift-Return>", self.make_recover_database_toplevel)
        self.height = 720
        self.width = 1280
        self.frame_height = 496
        self.master.resizable(0, 0)
        self.home_page_config()
        self.check_started()

    def home_page_config(self):
        """Creates header, footer, home button and main frame"""
        project_background_colour = "#8e94a4"
        project_bar_colour = "#3b415b"
        self.homepage_header_frame = Frame(self.master)
        self.homepage_header_frame.config(width=self.width, height=self.height/10, bg=project_bar_colour)
        self.homepage_header_frame.grid(row=0, column=0, columnspan=5, pady=(0, 40))
        self.homepage_header_frame.grid_propagate(False)

        self.homepage_button = Label(self.homepage_header_frame, text="Home")
        self.homepage_button.config(font=(None, "20"), bg=project_bar_colour)
        self.homepage_button.bind("<Enter>", lambda _: self.homepage_button.config(bg=project_background_colour))
        self.homepage_button.bind("<Leave>", lambda _: self.homepage_button.config(bg=project_bar_colour))
        self.homepage_button.bind("<Button-1>", lambda _: self.start_home(self.main_frame, self.homepage_button,
                                                                          self.master, self.started))

        self.main_frame = Frame(self.master)
        self.main_frame.config(width=self.width, height=self.frame_height, bg=project_background_colour, borderwidth=0,
                               highlightthickness=0)
        self.main_frame.grid(row=1, column=0, columnspan=5)
        self.main_frame.grid_propagate(False)

        self.homepage_footer_frame = Frame(self.master)
        self.homepage_footer_frame.config(width=self.width, height=self.height / 10, bg=project_bar_colour)
        self.homepage_footer_frame.grid(row=2, column=0, columnspan=5, pady=(40, 0))
        self.homepage_footer_frame.grid_propagate(False)

        self.homepage_footer_label = Label(self.homepage_footer_frame)
        self.homepage_footer_label.config(text="Garry Joynes \xa9 2021. All rights reserved.",
                                          bg=project_bar_colour, font=(None, "18"))
        self.homepage_footer_label.place(x=str(self.width / 2), y=str(self.homepage_footer_frame.winfo_reqheight() / 2),
                                         anchor="center")

    def check_started(self):
        """Checks whether to play button click sound when start_home function is called"""
        self.started = False
        self.start_home(self.main_frame, self.homepage_button, self.master, self.started)
        self.started = True
        self.master.mainloop()  # Mainloop is here

    def exit(self, event):
        """Exits application"""
        self.master.quit()

    def manual_backup(self, event):
        """Calls back_up method"""
        self.back_up()
        messagebox.showinfo(title="Manual Backup", message="Backup Successful")

    def make_recover_database_toplevel(self, event):
        """Creates recover database top level"""
        self.mrdtl_top_level = Toplevel(self.master)
        self.mrdtl_top_level.title("Recover Database")
        self.mrdtl_top_level.config(bg=self.project_background_colour)
        self.mrdtl_top_level.geometry("400x200")
        self.mrdtl_top_level.resizable(0, 0)
        self.mrdtl_top_level.iconbitmap("pictures/gj.ico")
        self.create_mrdtl_frames()
        self.create_mrdtl_buttons()

    def create_mrdtl_frames(self):
        """Creates frames for mrdtl"""
        self.mrdtl_top_frame = Frame(self.mrdtl_top_level)
        self.mrdtl_top_frame.config(height=40, width=400, bg=self.project_bar_colour)
        self.mrdtl_top_frame.grid(row=0, column=0)
        self.mrdtl_top_frame.grid_propagate(False)

        self.mrdtl_main_frame = Frame(self.mrdtl_top_level)
        self.mrdtl_main_frame.config(height=120, width=400, bg=self.project_background_colour)
        self.mrdtl_main_frame.grid(row=1, column=0)
        self.mrdtl_main_frame.grid_propagate(False)

        self.mrdtl_bottom_frame = Frame(self.mrdtl_top_level)
        self.mrdtl_bottom_frame.config(height=40, width=400, bg=self.project_bar_colour)
        self.mrdtl_bottom_frame.grid(row=2, column=0)
        self.mrdtl_bottom_frame.grid_propagate(False)

        self.mrdtl_header_label = Label(self.mrdtl_main_frame)
        self.mrdtl_header_label.config(text="Enter Admin Password:", bg=self.project_background_colour,
                                       font=self.cid_font)
        self.mrdtl_header_label.place(x="30", y="20")

        self.mrdtl_entry = Entry(self.mrdtl_main_frame)
        self.mrdtl_entry.config(font=self.cid_font, width=8)
        self.mrdtl_entry.place(x="260", y="20")

    def create_mrdtl_buttons(self):
        """buttons for mrdtl"""
        self.mrdtl_button = Label(self.mrdtl_main_frame)
        self.mrdtl_button.config(font=self.cid_font, text="Submit Password", bg=self.project_bar_colour)
        self.mrdtl_button.place(x="200", y="80", anchor="center")
        self.mrdtl_button.bind("<Enter>", lambda _: self.mrdtl_button.config(relief="ridge"))
        self.mrdtl_button.bind("<Leave>", lambda _: self.mrdtl_button.config(relief="flat"))
        self.mrdtl_button.bind("<Button-1>", self.admin_button_function)

    def admin_button_function(self, event):
        """Checks inputted password is correct and if so calls recover_database method"""
        admin_password = "18269"  # This is a crude way to go about this but I don't want the client messing around with
        # the databases unless it's absolutely necessary
        if self.mrdtl_entry.get() == admin_password:
            self.mrdtl_entry.delete(0, END)
            self.recover_database()
            messagebox.showinfo("Database Recovered", "Database has been successfully recovered")
        else:
            self.mrdtl_entry.delete(0, END)
            messagebox.showinfo("Invalid Password", "Entered password is not valid, please try again or contact"
                                                    " administrator", parent=self.mrdtl_top_level)


if __name__ == "__main__":
    MainApp()
