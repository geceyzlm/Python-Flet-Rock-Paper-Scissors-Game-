import flet as ft
import random

liste=["taş","kağıt","makas"] #rock->taş  #paper->kağıt #scissors->makas
oyuncuskor=0
pcskor=0

tasrsm="https://i2.wp.com/www.yazilimbilisim.net/wp-content/uploads/2016/03/tas-300x215.png?resize=300%2C215"
makasrsm="https://www.pngarts.com/files/1/Scissor-PNG-Image.png"
kagitrsm="https://w7.pngwing.com/pngs/316/967/png-transparent-paper-scroll-paper-miscellaneous-presentation-parchment-thumbnail.png"


def main(page: ft.Page):
    page.title = "taş-kağıt-makas oyunu (rock paper scissors game)"
    page.window_width=600
    page.window_height=700
    page.vertical_alignment = "center"
    page.horizontal_alignment="center"
    
    def kiyasla(e):
        global liste
        global oyuncuskor
        global pcskor
        global gamesecim
        random.shuffle(liste)

        #1
        if liste[0]=="taş" and gamesecim=="makas":
            pcsecim.image_src=tasrsm 
            benimsecim.image_src=makasrsm
            pcskor+=1
            pcpuan.value=f"pc puan:{pcskor}" 
            page.update()
        
        if liste[0]=="taş" and gamesecim=="kağıt":
            pcsecim.image_src=tasrsm 
            benimsecim.image_src=kagitrsm
            oyuncuskor+=1
            benimpuan.value=f"benim puanım:{oyuncuskor}"
            page.update()
        #2
        if liste[0]=="makas" and gamesecim=="kağıt":
            pcsecim.image_src=makasrsm
            benimsecim.image_src=kagitrsm
            pcskor+=1
            pcpuan.value=f"pc puan:{pcskor}"
            page.update()
        
        if liste[0]=="makas" and gamesecim=="taş":
            pcsecim.image_src=makasrsm
            benimsecim.image_src=tasrsm
            oyuncuskor+=1
            benimpuan.value=f"benim puanım:{oyuncuskor}"
            page.update()
        #3
        if liste[0]=="kağıt" and gamesecim=="taş":
            pcsecim.image_src=kagitrsm
            benimsecim.image_src=tasrsm
            pcskor+=1
            pcpuan.value=f"pc puan:{pcskor}"
            page.update()

        if liste[0]=="kağıt" and gamesecim=="makas":
            pcsecim.image_src=kagitrsm
            benimsecim.image_src=makasrsm
            oyuncuskor+=1
            benimpuan.value=f"benim puanım:{oyuncuskor}"
            page.update()

    
        
    def tas(e):
        global gamesecim
        gamesecim="taş"
        kiyasla(e)
        

    def kagit(e):
        global gamesecim
        gamesecim="kağıt"
        kiyasla(e)

    def makas(e):
        global gamesecim
        gamesecim="makas"
        
        kiyasla(e)
        
        
    makas =ft.Container(
        bgcolor="#D01CBA",
        width=100,
        height=100,
        border_radius=100,
        image_src=makasrsm,
        image_fit="contain",
        on_click=makas,
       
        )
    
    kagit =ft.Container(
        bgcolor="#D01CBA",
        width=100,
        height=100,
        border_radius=100,
        image_src=kagitrsm,
        image_fit="contain",
        on_click=kagit,
        )
    
    tas=ft.Container(
        bgcolor="#D01CBA",
        width=100,
        height=100,
        border_radius=100,
        image_src=tasrsm,
        image_fit="contain",
        on_click=tas,
        )
    
    pctext=ft.Text("PC")
    pcsecim=ft.Container(
        bgcolor="#A5A2A4",
        width=200,
        height=200,
        )
    
    bentext=ft.Text("BEN")
    benimsecim=ft.Container(
        bgcolor="#23CADB",
        width=200,
        height=200,
        )
    
    pcpuan=ft.Text("PC PUAN:")
    benimpuan=ft.Text("BENİM PUAN:")

    rw1=ft.Row(
        controls=[
            makas,kagit,tas
        ],
        top=0,
        left=125
    )
    rw2=ft.Row(
        controls=[
            ft.Column(
                controls=[pctext,pcsecim]
                
            ),
            ft.Column(
                controls=[bentext,benimsecim]
            )
        ],
        spacing=50,
        top=200,
        left=75
    )

    rw3=ft.Row(
        controls=[
            pcpuan,benimpuan
        ],
        spacing=175,
        top=500,
        left=120
    )

    st=ft.Stack(
        controls=[
            rw1,rw2,rw3
        ]
    )

    page.add(st)
    page.update()


ft.app(target=main)