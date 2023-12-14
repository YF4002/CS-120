import flet as ft

def main(page: ft.Page):
    
    def leapyears(e):
        days_in_month = {1: 31, 3: 31, 4: 30, 5:31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31   }
        month = int(EnterMonth_textField.value)
        year = int(EnterYear_textField.value)
        
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        elif year % 4 == 0:
            leap_year = True
        else:
            leap_year = False
    
        if month == 2 :
            if leap_year:
                days_in_month[2] = 29
            else:
                days_in_month[2]= 28
       
                
    
        output_textfield.value= str(days_in_month[month])
        page.update()
    
    def clear(e):
        output_textfield.value= ""
        page.update()
    
    
    page.title="Days in a Month"
    page.window_width=1000
    page.window_height=700
    page.bgcolor="CYAN"
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER


    title_text = ft.Text("Days in a Month", color="RED", size=25)
   
    #Month Text
    EnterMonth_text = ft.Text("Enter Month (1-12)", color="BLACK", size=30  ) 
    EnterMonth_textField = ft.TextField(
        width=200, height=100, color="BLACK", text_size=20, text_align="center",
    )
    Month_Row = ft.Row(
        controls=[EnterMonth_text, EnterMonth_textField,],
        alignment=ft.MainAxisAlignment.CENTER
    )
                    
    #Years Text
    EnterYear_text = ft.Text("Enter Year", color="BLACK", size=30)
    EnterYear_textField = ft.TextField(
        width=200, height=100, color="BLACK", text_size=20, text_align="center",
    )
    Year_Row = ft.Row(
        controls= [EnterYear_text, EnterYear_textField,],
        alignment=ft.MainAxisAlignment.CENTER
    )
    #Days Button
    Days = ft.ElevatedButton(
        content=ft.ResponsiveRow([ft.Text("Days", size=20, text_align="center")]),
        width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=leapyears
    )
        
    #Days Output
    output_textfield = ft.TextField(
        width=200, height=100, color="BLACK", text_size=20, text_align="center",
    )
    
    #Clear Button
    Clear = ft.ElevatedButton(
        content=ft.ResponsiveRow([ft.Text("Clear", size=20, text_align="center")]),
        width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=clear
    )
    
    page.add(
        title_text,
        Month_Row,
        Year_Row,
        Days,
        output_textfield,
        Clear,
        )
        
ft.app(target=main)
    

