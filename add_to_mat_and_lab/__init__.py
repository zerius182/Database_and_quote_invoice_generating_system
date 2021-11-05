from tkinter import *
from sound_player import SoundPlayer
from data_handler import AddDataToMatAndLabour, MatAndLabListBoxPopulate

atmal_sounds = SoundPlayer()


class AddToMatAndLab(AddDataToMatAndLabour):
    def __init__(self):
        AddDataToMatAndLabour.__init__(self)
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

    def create_add_mat_and_lab_page(self, atmal_key, atmal_frame, atmal_root, mat_frame, mat_box):
        self.atmal_frame = atmal_frame
        self.atmal_key = atmal_key
        self.atmal_root = atmal_root
        self.mat_frame = mat_frame
        self.mat_box = mat_box
        self.create_atmal_frame_and_label()
        self.create_atmal_labels()
        self.create_atmal_button()

    def create_atmal_frame_and_label(self):
        self.atmal_info_frame = Frame(self.atmal_frame)
        self.atmal_info_frame.config(bg=self.project_background_colour, height=self.frame_height, width=810,
                                     highlightthickness=0, borderwidth=0)
        self.atmal_info_frame.grid(row=0, column=0, padx=(30, 0), columnspan=2)
        self.atmal_info_frame.grid_propagate(False)

        self.atmal_header_label = Label(self.atmal_info_frame)
        self.atmal_header_label.config(font=self.cid_font_large_no_line,
                                       text="Enter Material/Labour Descriptions And Costs",
                                       bg=self.project_background_colour)
        self.atmal_header_label.grid(row=0, column=0, columnspan=5, sticky="we", pady=(0, 10))
        self.mat_frame.config(height=self.frame_height)
        self.mat_box.config(height=15)

    def create_atmal_labels(self):
        self.first_label = AddEntryFields(self.atmal_info_frame, 1, 0)
        self.second_label = AddEntryFields(self.atmal_info_frame, 2, 0)
        self.third_label = AddEntryFields(self.atmal_info_frame, 3, 0)
        self.fourth_label = AddEntryFields(self.atmal_info_frame, 4, 0)
        self.fifth_label = AddEntryFields(self.atmal_info_frame, 5, 0)
        self.sixth_label = AddEntryFields(self.atmal_info_frame, 6, 0)
        self.seventh_label = AddEntryFields(self.atmal_info_frame, 7, 0)
        self.eighth_label = AddEntryFields(self.atmal_info_frame, 8, 0)

    def create_atmal_button(self):
        self.atmal_button_label = Label(self.atmal_info_frame)
        self.atmal_button_label.config(font=self.cid_font_large_no_line, bg=self.project_bar_colour,
                                       text="Add To Materials And Labour")
        self.atmal_button_label.grid(row=9, column=0, columnspan=5, sticky="we", pady=(3, 0))
        self.atmal_button_label.bind("<Enter>", lambda _: self.atmal_button_label.config(relief="ridge"))
        self.atmal_button_label.bind("<Leave>", lambda _: self.atmal_button_label.config(relief="flat"))
        self.atmal_button_label.bind("<Button-1>", self.get_mat_and_lab_details)

    def get_mat_and_lab_details(self, event):
        atmal_sounds.play_click()
        to_check = {self.first_label.item_entry_name.get(): self.first_label.price_entry.get(),
                    self.second_label.item_entry_name.get(): self.second_label.price_entry.get(),
                    self.third_label.item_entry_name.get(): self.third_label.price_entry.get(),
                    self.fourth_label.item_entry_name.get(): self.fourth_label.price_entry.get(),
                    self.fifth_label.item_entry_name.get(): self.fifth_label.price_entry.get(),
                    self.sixth_label.item_entry_name.get(): self.sixth_label.price_entry.get(),
                    self.seventh_label.item_entry_name.get(): self.seventh_label.price_entry.get(),
                    self.eighth_label.item_entry_name.get(): self.eighth_label.price_entry.get()}
        info_dict = {}
        for item in to_check:
            if item == "":
                pass
            else:
                info_dict[item] = to_check[item]
        self.add_to_dict(self.atmal_key, info_dict)
        self.clear_data_fields()
        self.repopulate_client_mat_and_lab_listbox()

    def clear_data_fields(self):
        self.first_label.item_entry_name.delete(0, END)
        self.first_label.price_entry.delete(0, END)
        self.second_label.item_entry_name.delete(0, END)
        self.second_label.price_entry.delete(0, END)
        self.third_label.item_entry_name.delete(0, END)
        self.third_label.price_entry.delete(0, END)
        self.fourth_label.item_entry_name.delete(0, END)
        self.fourth_label.price_entry.delete(0, END)
        self.fifth_label.item_entry_name.delete(0, END)
        self.fifth_label.price_entry.delete(0, END)
        self.sixth_label.item_entry_name.delete(0, END)
        self.sixth_label.price_entry.delete(0, END)
        self.seventh_label.item_entry_name.delete(0, END)
        self.seventh_label.price_entry.delete(0, END)
        self.eighth_label.item_entry_name.delete(0, END)
        self.eighth_label.price_entry.delete(0, END)

    def repopulate_client_mat_and_lab_listbox(self):
        self.mat_box.delete(0, END)
        new_mat_and_lab_list = MatAndLabListBoxPopulate().populate_mat_lab_listbox(self.atmal_key, display_full=False)
        for item in new_mat_and_lab_list:
            self.mat_box.insert(END, item)


class AddEntryFields:
    def __init__(self, frame, row_param, column_param):
        self.row_param = row_param
        self.column_param = column_param
        self.frame = frame
        self.class_font = ("Arial", "16")
        self.class_background_colour = "#8e94a4"

        self.label_name = Label(self.frame)
        self.label_name.config(font=self.class_font, text="Item To Add:", bg=self.class_background_colour)
        self.item_entry_name = Entry(self.frame)
        self.item_entry_name.config(width=40, font=self.class_font)
        self.price_label = Label(self.frame)
        self.price_label.config(font=self.class_font, text="Price: £", bg=self.class_background_colour)
        self.price_entry = Entry(self.frame)
        self.price_entry.config(width=8, font=self.class_font)

        self.label_name.grid(row=self.row_param, column=self.column_param, pady=10)
        self.item_entry_name.grid(row=self.row_param, column=self.column_param+1, sticky="w", pady=10)
        self.price_label.grid(row=self.row_param, column=self.column_param+2, sticky="w", pady=10)
        self.price_entry.grid(row=self.row_param, column=self.column_param+3, sticky="w", pady=10)
