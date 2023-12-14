import flet as ft

def main(page: ft.Page):
 #Function
    def calc_perimeter(p):
        perimeter = int(length_textField.value) + int(width_textField.value)
        perimeter_textField.value = f"{perimeter}"
        page.update()

    page.title="Find Perimeter App"
    page.window_width=700
    page.window_height=700
    page.bgcolor="CYAN"
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER


    content_title_text = ft.Text("Find Perimeter", color="RED", size=25)
   
    #length row
    length_text = ft.Text("Length:", color="BLACK", size=30)
    length_textField = ft.TextField(
        width=100, height=100, color="BLACK", text_size=20, text_align="center"    
    )
    length_row = ft.Row(
        controls=[length_text, length_textField],
        alignment=ft.MainAxisAlignment.CENTER
    )
       #width
    width_text = ft.Text("Width:", color="BLACK", size=30)
    width_textField = ft.TextField(
        width=100, height=100, color="BLACK", text_size=20, text_align="center"    
    )
    width_row = ft.Row(
        controls=[width_text, width_textField],
        alignment=ft.MainAxisAlignment.CENTER
    )
       #Button
    calc_perimeter_button = ft.ElevatedButton(
        content=ft.Row([ft.Text("Calculate Perimeter", size=20, text_align="center")]),
        width=250, height=100, bgcolor="BLUE", color="WHITE", on_click=calc_perimeter
    )

    # perimeter row 
    perimeter_text = ft.Text("Perimeter:", color="BLACK", size=30)
    perimeter_textField = ft.TextField(
        width=100, height=100, color="BLACK", text_size=20, text_align="start"    
    )
    perimeter_row = ft.Row(
        controls = {perimeter_text, perimeter_textField},
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        content_title_text,
        length_row,
        width_row,
        calc_perimeter_button,
        perimeter_row
        )

ft.app(target=main)