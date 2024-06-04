# recreate apple top red green yellow buttons lol, follow apple color scheme calculator
import customtkinter
import time
import math_works as mw
import pygame
from PIL import Image

# Tag Stuff


def new_tag_config(self, tagName, **kwargs):
    return self._textbox.tag_config(tagName, **kwargs)


customtkinter.CTkTextbox.tag_config = new_tag_config
# --------------------------------------------------------------------------------------------------------------- #
adding_state = False
subtracting_state = False
multiplying_state = False
dividing_state = False
Start_of_number2 = False
zoomed_in = False
number1_chosen = False
number2_chosen = False
dot_activated = False
equation_completed = True
commas_on = True
mac_on = True
previous_mac_on = False
settings_running = False
default_on = True
color_operations = "#ff9f0a"
color_operations_hover = "#fcc585"
# --------------------------------------------------------------------------------------------------------------- #
window = customtkinter.CTk()
window.overrideredirect(True)
# Get screen width and height
w = 222
h = 350

# Get screen width and height
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

# Calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Set the dimensions of the screen
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False, False)
# --------------------------------------------------------------------------------------------------------------- #
background_frame = customtkinter.CTkButton(
    window, bg_color="#000000", fg_color="#000000", width=222, height=350, text="", state="disabled", hover=False)
background_frame.place(x=0, y=0)
# --------------------------------------------------------------------------------------------------------------- #
def settings_screen():
    global settings_running, settings
    if settings_running == True:
        settings.destroy()
    elif settings_running == False:
        pass
    settings = customtkinter.CTkToplevel()

    settings_running = True

    def callback():
        settings_running == False
        settings.destroy()
    settings.protocol("WM_DELETE_WINDOW", callback)

    # Get screen width and height
    w = 220
    h = 146

    # Get screen width and height
    ws = settings.winfo_screenwidth()
    hs = settings.winfo_screenheight()

    # Calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Set the dimensions of the screen
    settings.geometry('%dx%d+%d+%d' % (w, h, x, y))
    settings.resizable(False, False)
    settings.title("Settings")

    label1 = customtkinter.CTkLabel(settings, text="Comma's On #", font=customtkinter.CTkFont(
        "SF Pro Display Medium", size=15), bg_color="#242424")
    label1.place(x=7, y=3)

    def checkbox1_callback():
        global commas_on
        on_off = checkbox1.get()
        if on_off == 1:
            commas_on = True
            mw.comma_state(True)
        elif on_off == 0:
            commas_on = False
            mw.comma_state(False)

    checkbox1 = customtkinter.CTkCheckBox(
        settings, checkbox_width=17, checkbox_height=17, bg_color="#242424", text="", command=checkbox1_callback)
    if commas_on == True:
        checkbox1.select()
    elif commas_on == False:
        pass
    checkbox1.place(x=197, y=6)

    label2 = customtkinter.CTkLabel(settings, text="Mac Mode", font=customtkinter.CTkFont(
        "SF Pro Display Medium", size=15), bg_color="#242424")
    label2.place(x=7, y=33)

    def checkbox2_callback():
        global mac_on, previous_mac_on
        on_off2 = checkbox2.get()
        if on_off2 == 1:
            mac_on = True
            previous_mac_on = False
        elif on_off2 == 0:
            mac_on = False
            previous_mac_on = True
        if previous_mac_on == True:
            red_button.destroy()
            yellow_button.destroy()
            green_button.destroy()
            credit_button.destroy()
            settings_icon.destroy()
        elif previous_mac_on == False:
            first_frame.destroy()
            second_frame.destroy()
            credit_button.destroy()
            settings_icon.destroy()
            close_button.destroy()
            maximize_button.destroy()
            minimize_button.destroy()
        create_ui()

    checkbox2 = customtkinter.CTkCheckBox(
        settings, checkbox_width=17, checkbox_height=17, bg_color="#242424", text="", command=checkbox2_callback)
    if mac_on == True:
        checkbox2.select()
    elif mac_on == False:
        pass
    checkbox2.place(x=197, y=36)

    label3 = customtkinter.CTkLabel(settings, text="Default Theme", font=customtkinter.CTkFont(
        "SF Pro Display Medium", size=15), bg_color="#242424")
    label3.place(x=7, y=63)

    def checkbox3_callback():
        global default_on, color_operations, color_operations_hover, enter_button, addition_button, subtraction_button, multiplication_button, division_button
        default = checkbox3.get()
        if default == 1:
            default_on = True
            color_operations = "#ff9f0a"
            color_operations_hover = "#fcc585"
            enter_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            addition_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            subtraction_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            multiplication_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            division_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
        elif default == 0:
            default_on = False
            color_operations = "#0043b0"
            color_operations_hover = "#3559bd"
            enter_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            addition_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            subtraction_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            multiplication_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)
            division_button.configure(
                fg_color=color_operations, hover_color=color_operations_hover)

    checkbox3 = customtkinter.CTkCheckBox(
        settings, checkbox_width=17, checkbox_height=17, bg_color="#242424", text="", command=checkbox3_callback)
    if default_on == True:
        checkbox3.select()
    elif default_on == False:
        pass
    checkbox3.place(x=197, y=66)

    def copyright_button_callback():
        import webbrowser as wb
        wb.open("https://creativecommons.org/licenses/by-nc-sa/4.0/",
                new=1, autoraise=True)

    copyright_button = customtkinter.CTkButton(
        settings, bg_color="#242424", fg_color="#6a6a6b", border_color="#3c3c3d", hover_color="#7e7e7f", border_width=1, text="Copyright", width=208, height=10, font=customtkinter.CTkFont("SF Pro Display Semibold"), command=copyright_button_callback)
    copyright_button.configure(corner_radius=7)
    copyright_button.place(x=6, y=93)  # 158

    def reset_defaults_callback():
        checkbox1_state = checkbox1.get()
        checkbox2_state = checkbox2.get()
        checkbox3_state = checkbox3.get()

        if checkbox1_state == True:
            pass
        elif checkbox1_state == False:
            checkbox1.toggle()
        if checkbox2_state == True:
            pass
        elif checkbox2_state == False:
            checkbox2.toggle()
        if checkbox3_state == True:
            pass
        elif checkbox3_state == False:
            checkbox3.toggle()

    reset_defaults = customtkinter.CTkButton(
        settings, bg_color="#242424", fg_color="#6a6a6b", border_color="#3c3c3d", hover_color="#7e7e7f", border_width=1, text="Reset To Default", width=208, height=10, font=customtkinter.CTkFont("SF Pro Display Semibold"), command=reset_defaults_callback)
    reset_defaults.configure(corner_radius=7)
    reset_defaults.place(x=6, y=118)  # 158

    settings.mainloop()


def settings_icon_callback():
    settings_screen()
# --------------------------------------------------------------------------------------------------------------- #


def credit_button_callback():
    info = customtkinter.CTkToplevel()
    # Get screen width and height
    w = 200
    h = 128

    # Get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    # Calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # Set the dimensions of the screen
    info.geometry('%dx%d+%d+%d' % (w, h, x, y))
    info.resizable(False, False)
    info.title("Credits")

    calc_icon = customtkinter.CTkImage(dark_image=Image.open("/Users/aiden/Desktop/Python/For funz/icon.png"),
                                       size=(80, 80))

    calc_icon_place = customtkinter.CTkButton(
        info, bg_color="#242424", text="", image=calc_icon, fg_color="#242424", state="disabled")
    calc_icon_place.place(x=78, y=7)

    first_line = customtkinter.CTkLabel(info, bg_color="#242424", text="Made By:", font=customtkinter.CTkFont(
        "SF Pro Display Bold", size=18), anchor="w")
    first_line.place(x=13, y=12)

    second_line = customtkinter.CTkLabel(info, bg_color="#242424", text="Aiden Sorabji", font=customtkinter.CTkFont(
        "SF Pro Display Medium", size=14), anchor="w", height=5)
    second_line.place(x=13, y=42)

    import datetime

    today = datetime.date.today()

    year = today.year
    year = str(year)

    third_line_writing = "Copyright © " + year

    third_line = customtkinter.CTkLabel(
        info, bg_color="#242424", text=third_line_writing, font=customtkinter.CTkFont("SF Pro Display Thin", size=10), anchor="w", height=3)
    third_line.place(x=13, y=67)

    def github_button_callback():
        import webbrowser as wb
        wb.open("https://github.com/AidenSorabji", new=1, autoraise=True)

    github_button = customtkinter.CTkButton(
        info, bg_color="#242424", fg_color="#6a6a6b", border_color="#3c3c3d", hover_color="#7e7e7f", border_width=1, text="Github", width=84, height=9, font=customtkinter.CTkFont("SF Pro Display Medium"), command=github_button_callback)
    github_button.configure(corner_radius=7)
    github_button.place(x=13, y=95)

    info.mainloop()


def red_button_callback():
    window.destroy()
    time.sleep(0.7)
    exit()


def green_button_callback():
    global zoomed_in
    if zoomed_in == True:
        window.overrideredirect(False)
        window.wm_state('normal')
        window.overrideredirect(True)
        zoomed_in = False
    elif zoomed_in == False:
        window.overrideredirect(False)
        window.wm_state('zoomed')
        window.overrideredirect(True)
        zoomed_in = True

# --------------------------------------------------------------------------------------------------------------- #


def create_ui():
    global red_button, green_button, yellow_button, credit_button, settings_icon

    if mac_on == True:
        red_button = customtkinter.CTkButton(
            window, text="", corner_radius=20, bg_color="#000000", width=13, height=13, fg_color="#ff5f57", border_color="#be504a", border_width=1, hover_color="#f09389", command=red_button_callback)
        red_button.place(x=10, y=10)

        yellow_button = customtkinter.CTkButton(
            window, text="", corner_radius=20, bg_color="#000000", width=13, height=13, fg_color="#febc2e", border_color="#ac8332", border_width=1, hover_color="#fcfe74")
        yellow_button.place(x=30, y=10)

        green_button = customtkinter.CTkButton(
            window, text="", corner_radius=20, bg_color="#000000", width=13, height=13, fg_color="#29c840", border_color="#2d983b", border_width=1, hover_color="#86f37f", command=green_button_callback)
        green_button.place(x=50, y=10)

        credit_button = customtkinter.CTkButton(
            window, bg_color="#000000", fg_color="#6a6a6b", border_color="#3c3c3d", hover_color="#7e7e7f", border_width=1, text="Credits", width=50, height=6, font=customtkinter.CTkFont("SF Pro Display Medium"), command=credit_button_callback)
        credit_button.configure(corner_radius=7)
        credit_button.place(x=129, y=5)  # 158

        settings_icon = customtkinter.CTkButton(
            window, bg_color="#000000", fg_color="#6a6a6b", border_color="#3c3c3d", hover_color="#7e7e7f", border_width=1, text="⚙", width=10, height=6, font=customtkinter.CTkFont("SF Pro Display Bold", size=13), command=settings_screen)
        settings_icon.configure(corner_radius=7)
        settings_icon.place(x=193, y=5)  # 158

    elif mac_on == False:
        global first_frame, second_frame, close_button, maximize_button, minimize_button
        first_frame = customtkinter.CTkButton(
            window, bg_color="#000000", fg_color="#3d3d3d", text="", width=69, height=25, border_width=1, border_color="#616161", corner_radius=0)
        first_frame.place(x=0, y=0)

        credit_button = customtkinter.CTkButton(
            window, bg_color="#616161", fg_color="#3d3d3d", text="Credits", width=35, height=25, font=customtkinter.CTkFont("SF Pro Display light", size=12), command=credit_button_callback, corner_radius=0, hover_color="#949494")
        credit_button.place(x=30, y=0)  # 158

        settings_icon = customtkinter.CTkButton(
            window, bg_color="#616161", fg_color="#3d3d3d", text="⚙", width=30, height=25, font=customtkinter.CTkFont("SF Pro Display Bold", size=16), command=settings_screen, corner_radius=0, hover_color="#949494")
        settings_icon.place(x=0, y=0)  # 158

        second_frame = customtkinter.CTkButton(
            window, bg_color="#000000", fg_color="#3d3d3d", text="", width=99, height=25, border_width=1, border_color="#616161", corner_radius=0)
        second_frame.place(x=130, y=0)

        close_button = customtkinter.CTkButton(
            window, text="X", bg_color="#616161", corner_radius=0, height=25, width=30, command=red_button_callback, fg_color="#3d3d3d", hover_color="#e34347")
        close_button.place(x=192, y=0)

        maximize_button = customtkinter.CTkButton(
            window, text="□", bg_color="#616161", corner_radius=0, height=25, width=30, command=green_button_callback, fg_color="#3d3d3d", hover_color="#43e346")
        maximize_button.place(x=162, y=0)

        minimize_button = customtkinter.CTkButton(
            window, text="﹣", bg_color="#616161", corner_radius=0, height=25, width=30, fg_color="#3d3d3d", hover_color="#e3d043")
        minimize_button.place(x=132, y=0)


create_ui()
# --------------------------------------------------------------------------------------------------------------- #
right_tag = "right_align"
visible_label = customtkinter.CTkTextbox(window, font=customtkinter.CTkFont(
    "SF Display Medium", size=37, weight="bold"), height=40, width=200, bg_color="#000000", fg_color="#000000", activate_scrollbars=False)
visible_label.tag_config("right", justify="right")
visible_label.configure(state="disabled")
visible_label.place(x=12, y=33)
# --------------------------------------------------------------------------------------------------------------- #


def zero_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif commas_on == False:
                pass
    visible_label.insert("end", "0", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


zero_button = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="0", height=55, width=108, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=zero_button_callback)
zero_button.place(x=0, y=296)


def dot_button_callback():
    global dot_activated, equation_completed
    if equation_completed == True:
        visible_label.configure(state="normal")
        visible_label.delete(1.0, "end")
        visible_label.insert("end", "0", "right")
        visible_label.configure(state="normal")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False

    if dot_activated == True:
        pass
    elif dot_activated == False:
        visible_label.configure(state="normal")
        visible_label.insert("end", ".", "right")
        text_length = len(visible_label.get("1.0", "end-1c"))
        if text_length == 8:
            visible_label.delete("end-2c", "end-1c")
        visible_label.configure(state="disabled")
        dot_activated = True


dot_button = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="•", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=dot_button_callback)
dot_button.place(x=108, y=296)


def one_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif commas_on == False:
                pass
    visible_label.insert("end", "1", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


one = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="1", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=one_button_callback)
one.place(x=0, y=243)


def two_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif commas_on == False:
                pass
    visible_label.insert("end", "2", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


two = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="2", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=two_button_callback)
two.place(x=54, y=243)


def three_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif commas_on == False:
                pass
    visible_label.insert("end", "3", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


three = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="3", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=three_button_callback)
three.place(x=108, y=243)


def four_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "4", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


four = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="4", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=four_button_callback)
four.place(x=0, y=190)


def five_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "5", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


five = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="5", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=five_button_callback)
five.place(x=54, y=190)


def six_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)

    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "6", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


six = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="6", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=six_button_callback)
six.place(x=108, y=190)


def seven_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "7", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


seven = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="7", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=seven_button_callback)
seven.place(x=0, y=137)


def eight_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "8", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


eight = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="8", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=eight_button_callback)
eight.place(x=54, y=137)


def nine_button_callback():
    global Start_of_number2, equation_completed
    visible_label.configure(state="normal")
    if equation_completed == True:
        visible_label.delete(1.0, "end")
        visible_label.configure(font=customtkinter.CTkFont(size=37))
        equation_completed = False
    if Start_of_number2 == True:
        visible_label.delete(1.0, "end")
        Start_of_number2 = False
        if adding_state == True:
            addition_button.configure(fg_color=color_operations)
        elif subtracting_state == True:
            subtraction_button.configure(fg_color=color_operations)
        elif multiplying_state == True:
            multiplication_button.configure(fg_color=color_operations)
        elif dividing_state == True:
            division_button.configure(fg_color=color_operations)
    text_length = len(visible_label.get("1.0", "end-1c"))
    if dot_activated == False:
        if commas_on == True:
            if text_length == 3:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string[:1] + "," + text_string[1:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 5:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:2] + "," + text_string[2:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
            elif text_length == 6:
                text_string = visible_label.get("1.0", "end-1c")
                text_string = text_string.replace(",", "")
                text_string = text_string[:3] + "," + text_string[3:]
                visible_label.delete(1.0, "end")
                visible_label.insert("end", text_string, "right")
        elif commas_on == False:
            pass
    visible_label.insert("end", "9", "right")
    text_length = len(visible_label.get("1.0", "end-1c"))
    if text_length == 8:
        visible_label.delete("end-2c", "end-1c")
    visible_label.configure(state="disabled")


nine = customtkinter.CTkButton(
    window, fg_color="#333333", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="9", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), hover_color="#6f6f6f", command=nine_button_callback)
nine.place(x=108, y=137)
# --------------------------------------------------------------------------------------------------------------- #


def enter_button_callback():
    global adding_state, subtracting_state, multiplying_state, dividing_state, dot_activated, equation_completed
    text_length = visible_label.get("1.0", "end-1c")
    mw.math_term2(text_length)

    if adding_state == True:
        mw.addition(commas_on)
        from math_works import addition
        final_answer = addition(commas_on)
    elif subtracting_state == True:
        mw.subtraction(commas_on)
        from math_works import subtraction
        final_answer = subtraction(commas_on)
    elif multiplying_state == True:
        mw.multiplication(commas_on)
        from math_works import multiplication
        final_answer = multiplication(commas_on)
    elif dividing_state == True:
        mw.division(commas_on)
        from math_works import division
        final_answer = division(commas_on)

    final_answer_characters = len(final_answer)
    if final_answer_characters == 9:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=35))
    elif final_answer_characters == 10:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=33))
    elif final_answer_characters == 11:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=31))
    elif final_answer_characters == 12:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=29))
    elif final_answer_characters == 13:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=27))
    elif final_answer_characters == 14:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=25))
    elif final_answer_characters == 15:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=23))
    elif final_answer_characters == 16:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=21))
    elif final_answer_characters == 17:
        visible_label.configure(
            state="normal", font=customtkinter.CTkFont(size=19))

    adding_state = False
    subtracting_state = False
    multiplying_state = False
    dividing_state = False
    number1_chosen = False
    number2_chosen = False
    visible_label.configure(state="normal")
    visible_label.delete(1.0, "end")
    visible_label.insert("end", final_answer, "right")
    visible_label.configure(state="disabled")
    dot_activated = False
    equation_completed = True


enter_button = customtkinter.CTkButton(
    window, fg_color=color_operations, bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="=", height=55, width=60, font=customtkinter.CTkFont("SF Display", size=21), hover_color=color_operations_hover, command=enter_button_callback)
enter_button.place(x=162, y=296)
# --------------------------------------------------------------------------------------------------------------- #


def addition_button_callback():
    global Start_of_number2, dot_activated, adding_state
    adding_state = True
    number1_chosen = True
    Start_of_number2 = True
    dot_activated = False
    text_length = visible_label.get("1.0", "end-1c")
    mw.math_term1(text_length)
    addition_button.configure(fg_color=color_operations_hover)


addition_button = customtkinter.CTkButton(
    window, fg_color=color_operations, bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="+", height=55, width=60, font=customtkinter.CTkFont("SF Display", size=21), hover_color=color_operations_hover, command=addition_button_callback)
addition_button.place(x=162, y=243)


def subtraction_button_callback():
    global Start_of_number2, dot_activated, subtracting_state
    subtracting_state = True
    number1_chosen = True
    Start_of_number2 = True
    dot_activated = False
    text_length = visible_label.get("1.0", "end-1c")
    mw.math_term1(text_length)
    subtraction_button.configure(fg_color=color_operations_hover)


subtraction_button = customtkinter.CTkButton(
    window, fg_color=color_operations, bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="﹣", height=55, width=60, font=customtkinter.CTkFont("SF Display", size=32), hover_color=color_operations_hover, command=subtraction_button_callback)
subtraction_button.place(x=162, y=190)


def multiplication_button_callback():
    global Start_of_number2, dot_activated, multiplying_state
    multiplying_state = True
    number1_chosen = True
    Start_of_number2 = True
    dot_activated = False
    text_length = visible_label.get("1.0", "end-1c")
    mw.math_term1(text_length)
    multiplication_button.configure(fg_color=color_operations_hover)


multiplication_button = customtkinter.CTkButton(
    window, fg_color=color_operations, bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="𝕏", height=55, width=60, font=customtkinter.CTkFont("SF Display", size=21), hover_color=color_operations_hover, command=multiplication_button_callback)
multiplication_button.place(x=162, y=137)


def divition_button_callback():
    global Start_of_number2, dot_activated, dividing_state
    dividing_state = True
    number1_chosen = True
    Start_of_number2 = True
    dot_activated = False
    text_length = visible_label.get("1.0", "end-1c")
    mw.math_term1(text_length)
    division_button.configure(fg_color=color_operations_hover)


division_button = customtkinter.CTkButton(
    window, fg_color=color_operations, bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="÷", height=55, width=60, font=customtkinter.CTkFont("SF Display", size=28), hover_color=color_operations_hover, command=divition_button_callback)
division_button.place(x=162, y=84)
# --------------------------------------------------------------------------------------------------------------- #


def ac_button_callback():
    global dot_activated
    adding_state = False
    subtracting_state = False
    multiplying_state = False
    dividing_state = False
    number1_chosen = False
    number2_chosen = False
    visible_label.configure(state="normal")
    visible_label.delete(1.0, "end")
    visible_label.configure(state="disabled")
    dot_activated = False
    addition_button.configure(fg_color=color_operations)
    subtraction_button.configure(fg_color=color_operations)
    multiplication_button.configure(fg_color=color_operations)
    division_button.configure(fg_color=color_operations)


ac_button = customtkinter.CTkButton(
    window, fg_color="#a5a5a5", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="AC", height=55, width=108, font=customtkinter.CTkFont("SF Display", size=21), text_color="#000000", hover_color="#d9d9d9", command=ac_button_callback)
ac_button.place(x=0, y=84)


def charge_button_callback():
    text_inside_label = visible_label.get("1.0", "end-1c")
    if "-" in text_inside_label:
        visible_label.configure(state="normal")
        visible_label.delete(1.0, "end")
        text_inside_label = text_inside_label.replace("-", "")
        visible_label.insert("end", text_inside_label, "right")
        visible_label.configure(state="disabled")
    else:
        visible_label.configure(state="normal")
        visible_label.delete(1.0, "end")
        visible_label.insert("end", "-", "right")
        visible_label.insert("end", text_inside_label, "right")
        visible_label.configure(state="disabled")


charge_button = customtkinter.CTkButton(
    window, fg_color="#a5a5a5", bg_color="#000000", border_width=1, border_color="#000000", corner_radius=8, text="⁺∕₋", height=55, width=55, font=customtkinter.CTkFont("SF Display", size=21), text_color="#000000", hover_color="#d9d9d9", command=charge_button_callback)
charge_button.place(x=108, y=84)
# --------------------------------------------------------------------------------------------------------------- #
window.mainloop()
