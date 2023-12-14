import flet as ft

def main(page: ft.Page):
    import random
    
    def print_Rock(e):
        Player = "Rock"
        choices = ["Rock","Paper","Scissors"]
        Computer = random.choice(choices)
        if Computer == "Paper":
            winner = "Computer wins"
        elif Computer =="Scissors":
            winner = "Player wins"
        else:
            winner = "It's a tie "
        Choices_text.value = f"{Player} vs {Computer}"
        output_textfield.value = winner
        page.update()
        
    def print_Paper(e):
        Player = "Paper"
        choices = ["Rock","Paper","Scissors"]
        Computer = random.choice(choices)
        if Computer == "Scissors":
            winner = "Computer wins"
        elif Computer == "Rock":
            winner = "Player wins"
        else:
            winner = "It's a tie"
        Choices_text.value = f"{Player} vs {Computer}"
        output_textfield.value = winner
        page.update()

    def print_Scissors(e):
        Player = "Scissors"
        choices = ["Rock","Paper","Scissors"]
        Computer = random.choice(choices)
        if Computer == "Rock":
            winner = "Computer wins"
        elif Computer == "Paper":
            winner = "Player wins"
        else:
            winner = "It's a tie "
        Choices_text.value = f"{Player} vs {Computer}"
        output_textfield.value = winner
        page.update()
        
    def reset(e):
        Choices_text.value = "Player vs Computer"
        output_textfield.value = " "
        page.update()
            
        
                
        page.update()

    page.title="Rock Paper Scissors App"
    page.window_width=1000
    page.window_height=700
    page.bgcolor="CYAN"
    page.vertical_alignment=ft.MainAxisAlignment.SPACE_EVENLY
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER


    title_text = ft.Text("Rock Paper Scissors", color="RED", size=25)
   
    #Choices Text
    Choices_text = ft.Text("Player vs Computer", color="BLACK", size=30    

    )
      
       #Rock Button
    Rock = ft.ElevatedButton(
        content=ft.ResponsiveRow([ft.Text("Rock", size=20, text_align="center")]),
        width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=print_Rock
    )
     
        #Paper Button
    Paper = ft.ElevatedButton(
         content=ft.ResponsiveRow([ft.Text("Paper", size=20, text_align="center")]),
         width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=print_Paper
    )   

         #Scissors Button
    Scissors = ft.ElevatedButton(
         content=ft.ResponsiveRow([ft.Text("Scissor", size=20, text_align="center")]),
         width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=print_Scissors

     )
    
    button_row = ft.Row(
        controls=[Rock, Paper, Scissors],
        alignment=ft.MainAxisAlignment.CENTER
    )
  
    output_textfield = ft.TextField(
        width=200, height=100, color="BLACK", text_size=20, text_align="center",
        
    )

    reset_button = ft.ElevatedButton(
        content=ft.Row([ft.Text("Reset Button", size=20, text_align="center")]),
        width=300, height=100, bgcolor="BLUE", color="WHITE", on_click=reset
   )
    
    page.add(
        title_text,
        Choices_text,
        button_row,
        output_textfield,
        reset_button
    )
    
ft.app(target=main)
        
