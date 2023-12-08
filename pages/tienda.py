from streamlit import * 
from streamlit_option_menu import option_menu
from utils import hide_pages, back_to_page
import requests
from streamlit_lottie import st_lottie
from classes import *

def cargar_lottie(url):
    a = requests.get(url)
    if a.status_code != 200:
        return None
    return a.json()

lottie = cargar_lottie("https://assets6.lottiefiles.com/private_files/lf30_qajpmo77.json")
lottie2 = cargar_lottie("https://assets4.lottiefiles.com/packages/lf20_qoqtgkus.json")
lottie3 = cargar_lottie("https://assets1.lottiefiles.com/packages/lf20_47pyyfcf.json")

if 'precio' not in session_state:
	session_state.precio = 0

def incremento(incremento=0):
    session_state.precio += incremento

def reinicio(reinicio=0):
    session_state.precio = incremento*0


hide_pages()

with sidebar:
    selected = option_menu(
        menu_title = "Computer RM",
        options=["Productos","Motherboards", "Procesadores", "Tarjetas gráficas", "Laptops", "Carrito", "Cerrar sesion"],
        icons=["bag-check", "device-ssd", "cpu" , "controller", "laptop", "cart", "backspace"],
        menu_icon="list-nested"
    )

if selected == "Productos":
    title("Productos disponibles en nuestra tienda!")
    write("---")
    
    with container():
        col_izquierda, col_derecha = columns(2)
        with col_izquierda:
            subheader(str(mobos[0].get_prod_name()))
            write("La ASUS ROG Strix Z690-A Gaming WiFi D4 es una placa base de gama media para la plataforma Intel Z690. Cuenta con una gran cantidad de funciones y características, incluyendo soporte para la memoria DDR4, PCIe 5.0, WiFi 6E y una amplia gama de puertos y conectores.")
        with col_derecha:
            image("imgs\mb_1.jpg",width=290)
        write("---")

    with container():
        col_izquierda1, col_derecha1 = columns(2)
        with col_izquierda1:
           subheader(str(mobos[1].get_prod_name()))
           write("La ASUS TUF Gaming Z690-Plus WiFi D4 es una placa base de gama media para la plataforma Intel Z690. Ofrece una buena relación calidad-precio y cuenta con una serie de características que la convierten en una opción atractiva para los usuarios de juegos y creadores de contenido.")   
        with col_derecha1:
            image("imgs\mb_2.jpg", width=290)
        write("---")

    with container():
        col_izquierda2, col_derecha2 = columns(2)
        with col_izquierda2:
           subheader(str(mobos[2].get_prod_name()))
           write("La Gigabyte Z690 Aorus Master es una placa base de gama alta para la plataforma Intel Z690. Ofrece un rendimiento y una funcionalidad de primera línea, incluyendo soporte para la memoria DDR5, PCIe 5.0, WiFi 6E y una amplia gama de puertos y conectores.")
        with col_derecha2:
            image("imgs\mb_3.jpg" ,width= 290)
        write("---")

    with container():
        col_izquierda3, col_derecha3 = columns(2)
        with col_izquierda3:
           subheader(str(mobos[3].get_prod_name()))
           write("La ASUS ROG Strix X670E Gaming WiFi es una placa base de gama alta para la plataforma AMD X670E. Ofrece un rendimiento y una funcionalidad de primera línea, incluyendo soporte para la memoria DDR5, PCIe 5.0, WiFi 6E y una amplia gama de puertos y conectores.")
        with col_derecha3:
            image("imgs\mb_4.jpg", width= 290)
        write("---")

    with container():
        col_izquierda4, col_derecha4 = columns(2)
        with col_izquierda4:
           subheader(str(mobos[4].get_prod_name()))
           write("La Gigabyte X670 AORUS Master es una placa base de gama alta para la plataforma AMD X670. Ofrece un rendimiento y una funcionalidad de primera línea, incluyendo soporte para la memoria DDR5, PCIe 5.0, WiFi 6E y una amplia gama de puertos y conectores.")
        with col_derecha4:
            image("imgs\mb_5.jpg", width=290)
        write("---")

    with container():
        col_izquierda5, col_derecha5 = columns(2)
        with col_izquierda5:
           subheader(str(processors[0].get_prod_name()))
           write("El AMD Ryzen 7 7800X es un procesador de gama alta para juegos y creación de contenido. Ofrece un rendimiento excelente gracias a su arquitectura Zen 4 y 8 núcleos / 16 hilos.")   
        with col_derecha5:
            image("imgs\pr_1.jpg", width=290)
        write("---")

    with container():
        col_izquierda6, col_derecha6 = columns(2)
        with col_izquierda6:
           subheader(str(processors[1].get_prod_name()))
           write("El AMD Ryzen 9 7900X es un procesador de gama alta con 12 núcleos / 24 hilos. Ofrece un rendimiento aún mayor que el Ryzen 7 7800X, lo que lo hace ideal para tareas exigentes como renderizado 3D, simulaciones y edición de video profesional.")   
        with col_derecha6:
            image("imgs\pr_2.jpg", width=290)
        write("---") 

    with container():
        col_izquierda7, col_derecha7 = columns(2)
        with col_izquierda7:
           subheader(str(processors[2].get_prod_name()))
           write("El Intel Core i9-13900K es un procesador de gama alta para entusiastas. Ofrece un rendimiento excelente con 24 núcleos / 32 hilos y una frecuencia turbo de hasta 5.8 GHz.")   
        with col_derecha7:
            image("imgs\pr_3.jpg", width=290)
        write("---")

    with container():
        col_izquierda8, col_derecha8 = columns(2)
        with col_izquierda8:
           subheader(str(processors[3].get_prod_name()))
           write("El Intel Core i7-13700K es un procesador de gama alta con 8 núcleos / 16 hilos. Ofrece un rendimiento similar al Ryzen 7 7800X y es ideal para juegos exigentes y creación de contenido.")   
        with col_derecha8:
            image("imgs\pr_4.jpg", width=290)
        write("---")

    with container():
        col_izquierda9, col_derecha9= columns(2)
        with col_izquierda9:
           subheader(str(processors[4].get_prod_name()))
           write("El AMD Ryzen 5 7600X es un procesador de gama media para juegos. Ofrece un rendimiento excelente en juegos con 6 núcleos / 12 hilos y una frecuencia turbo de hasta 5.3 GHz.")   
        with col_derecha9:
            image("imgs\pr_5.jpg", width=290)
        write("---")

    with container():
        col_izquierda10, col_derecha10 = columns(2)
        with col_izquierda10:
           subheader(str(graphcards[0].get_prod_name()))
           write("La NVIDIA GeForce RTX 3080 Ti es una tarjeta gráfica de gama alta que ofrece un rendimiento excelente para juegos y creación de contenido. Cuenta con 12 GB de memoria GDDR6X y una frecuencia de reloj de hasta 1.860 MHz.")
        with col_derecha10:
            image("imgs\g_1.jpg", width=290)
        write("---")

    with container():
        col_izquierda11, col_derecha11 = columns(2)
        with col_izquierda11:
           subheader(str(graphcards[1].get_prod_name()))
           write("La NVIDIA GeForce RTX 3080 es una tarjeta gráfica de gama alta que ofrece un rendimiento muy bueno para juegos y creación de contenido. Cuenta con 10 GB de memoria GDDR6X y una frecuencia de reloj de hasta 1.710 MHz.")
        with col_derecha11:
            image("imgs\g_2.jpg", width=290)
        write("---")

    with container():
        col_izquierda12, col_derecha12 = columns(2)
        with col_izquierda12:
           subheader(str(graphcards[2].get_prod_name()))
           write("La AMD Radeon RX 7900 XT es una tarjeta gráfica de gama alta que ofrece un rendimiento comparable a la NVIDIA GeForce RTX 3080 Ti. Cuenta con 16 GB de memoria GDDR6 y una frecuencia de reloj de hasta 2.250 MHz.")
        with col_derecha12:
            image("imgs\g_3.jpg", width=290)
        write("---")

    with container():
        col_izquierda13, col_derecha13 = columns(2)
        with col_izquierda13:
           subheader(str(graphcards[3].get_prod_name()))
           write("La AMD Radeon RX 7800 XT es una tarjeta gráfica de gama alta que ofrece un rendimiento similar a la NVIDIA GeForce RTX 3080. Cuenta con 12 GB de memoria GDDR6 y una frecuencia de reloj de hasta 2.100 MHz.")
        with col_derecha13:
            image("imgs\g_4.jpg", width=290)
        write("---")

    with container():
        col_izquierda14, col_derecha14 = columns(2)
        with col_izquierda14:
           subheader(str(graphcards[0].get_prod_name()))
           write("La NVIDIA GeForce RTX 3070 Ti es una tarjeta gráfica de gama media-alta que ofrece un rendimiento excelente para juegos a 1440p y 4K. Cuenta con 8 GB de memoria GDDR6X y una frecuencia de reloj de hasta 1.860 MHz.")
        with col_derecha14:
            image("imgs\g_5.jpg", width=290)
        write("---")    

    with container():
        col_izquierda15, col_derecha15 = columns(2)
        with col_izquierda15:
           subheader(str(laptops[0].get_prod_name()))
           write("La Asus ROG Zephyrus G15 (2023) es una laptop gaming de gama alta que ofrece un excelente rendimiento y una gran portabilidad. Cuenta con un procesador AMD Ryzen 9 7900HS o Intel Core i9-13900H, una tarjeta gráfica NVIDIA GeForce RTX 3080 Ti o AMD Radeon RX 7900 XT, y hasta 64 GB de memoria RAM.")
        with col_derecha15:
            image("imgs\lap_1.jpg", width=290)
        write("---")

    with container():
        col_izquierda16, col_derecha16 = columns(2)
        with col_izquierda16:
           subheader(str(laptops[1].get_prod_name()))
           write("La Acer Predator Triton 500 SE (2023) es otra laptop gaming de gama alta que ofrece un rendimiento similar al de la Asus ROG Zephyrus G15. Cuenta con un procesador Intel Core i9-13900H, una tarjeta gráfica NVIDIA GeForce RTX 3080 Ti o AMD Radeon RX 7900 XT, y hasta 64 GB de memoria RAM.")
        with col_derecha16:
            image("imgs\lap_2.jpg", width=290)
        write("---")

    with container():
        col_izquierda17, col_derecha17 = columns(2)
        with col_izquierda17:
           subheader(str(laptops[2].get_prod_name()))
           write("La Gigabyte Aorus 15P XD (2023) es una laptop gaming de gama media-alta que ofrece un rendimiento excelente para juegos a 1440p y 4K. Cuenta con un procesador Intel Core i7-13700H, una tarjeta gráfica NVIDIA GeForce RTX 3070 Ti o AMD Radeon RX 7800 XT, y hasta 64 GB de memoria RAM.")
        with col_derecha17:
            image("imgs\lap_3.jpg", width=290)
        write("---")    

    with container():
        col_izquierda18, col_derecha18 = columns(2)
        with col_izquierda18:
           subheader(str(laptops[3].get_prod_name()))
           write("La MSI GE76 Raider (2023) es una laptop gaming de gama alta que ofrece un rendimiento excelente para juegos y creación de contenido. Cuenta con un procesador Intel Core i9-13900H, una tarjeta gráfica NVIDIA GeForce RTX 3080 Ti o AMD Radeon RX 7900 XT, y hasta 64 GB de memoria RAM.")   
        with col_derecha18:
            image("imgs\lap_4.jpg", width=290)
        write("---")

    with container():
        col_izquierda19, col_derecha19 = columns(2)
        with col_izquierda19:
           subheader(str(laptops[4].get_prod_name()))
           write("La Razer Blade 15 Advanced (2023) es una laptop gaming de gama alta que ofrece un diseño elegante y un rendimiento excelente. Cuenta con un procesador Intel Core i9-13900H, una tarjeta gráfica NVIDIA GeForce RTX 3080 Ti o AMD Radeon RX 7900 XT, y hasta 64 GB de memoria RAM.")
        with col_derecha19:
            image("imgs\lap_5.jpg", width=290)
        write("---")

# -----------------------------------------------------------------------------------------------------------------------

if selected == "Motherboards":
    title("Elige tu placa base!")
    with container():
        col_izquierda, col_derecha = columns(2)
        with col_izquierda:
            image("imgs\mb_1.jpg",width=290)
        with col_derecha:
            pr1 = mobos[0].get_price()
            text(f"Precio: {pr1} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad1"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar1",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda1, col_derecha1 = columns(2)
        with col_izquierda1:
           image("imgs\mb_2.jpg", width=290)
        with col_derecha1:
            pr2 = mobos[1].get_price()
            text(f"Precio: {pr2} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad2"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar2",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda2, col_derecha2 = columns(2)
        with col_izquierda2:
           image("imgs\mb_3.jpg" ,width= 290)
        with col_derecha2:
            pr3 = mobos[2].get_price()
            text(f"Precio: {pr3} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad3"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda3, col_derecha3 = columns(2)
        with col_izquierda3:
           image("imgs\mb_4.jpg" ,width= 290)
        with col_derecha3:
            pr4 = mobos[3].get_price()
            text(f"Precio: {pr4} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad4"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda4, col_derecha4 = columns(2)
        with col_izquierda4:
           image("imgs\mb_5.jpg" ,width= 290)
        with col_derecha4:
            pr5 = mobos[4].get_price()
            text(f"Precio: {pr5} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad5"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

# -----------------------------------------------------------------------------------------------------------------------

if selected == "Procesadores":
    title("Elige tu procesador!")
    with container():
        col_izquierda, col_derecha = columns(2)
        with col_izquierda:
            image("imgs\pr_1.jpg",width=290)
        with col_derecha:
            pr1 = processors[0].get_price()
            text(f"Precio: {pr1} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad1"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar1",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda1, col_derecha1 = columns(2)
        with col_izquierda1:
           image("imgs\pr_2.jpg", width=290)
        with col_derecha1:
            pr2 = processors[1].get_price()
            text(f"Precio: {pr2} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad2"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar2",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda2, col_derecha2 = columns(2)
        with col_izquierda2:
           image("imgs\pr_3.jpg" ,width= 290)
        with col_derecha2:
            pr3 = processors[2].get_price()
            text(f"Precio: {pr3} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad3"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda3, col_derecha3 = columns(2)
        with col_izquierda3:
           image("imgs\pr_4.jpg" ,width= 290)
        with col_derecha3:
            pr4 = processors[3].get_price()
            text(f"Precio: {pr4} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad4"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda4, col_derecha4 = columns(2)
        with col_izquierda4:
           image("imgs\pr_5.jpg" ,width= 290)
        with col_derecha4:
            pr5 = processors[4].get_price()
            text(f"Precio: {pr5} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad5"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

#------------------------------------------------------------------------------------------------------------------------

if selected == "Tarjetas gráficas":
    title("Elige tu tarjeta gráfica!")
    with container():
        col_izquierda, col_derecha = columns(2)
        with col_izquierda:
            image("imgs\g_1.jpg",width=290)
        with col_derecha:
            pr1 = graphcards[0].get_price()
            text(f"Precio: {pr1} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad1"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar1",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda1, col_derecha1 = columns(2)
        with col_izquierda1:
           image("imgs\g_2.jpg", width=290)
        with col_derecha1:
            pr2 = graphcards[1].get_price()
            text(f"Precio: {pr2} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad2"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar2",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda2, col_derecha2 = columns(2)
        with col_izquierda2:
           image("imgs\g_3.jpg" ,width= 290)
        with col_derecha2:
            pr3 = graphcards[2].get_price()
            text(f"Precio: {pr3} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad3"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda3, col_derecha3 = columns(2)
        with col_izquierda3:
           image("imgs\g_4.jpg" ,width= 290)
        with col_derecha3:
            pr4 = graphcards[3].get_price()
            text(f"Precio: {pr4} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad4"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda4, col_derecha4 = columns(2)
        with col_izquierda4:
           image("imgs\g_5.jpg" ,width= 290)
        with col_derecha4:
            pr5 = graphcards[4].get_price()
            text(f"Precio: {pr5} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad5"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

#------------------------------------------------------------------------------------------------------------------------
if selected == "Laptops":
    title("Elige tu laptop!")
    with container():
        col_izquierda, col_derecha = columns(2)
        with col_izquierda:
            image("imgs\lap_1.jpg",width=290)
        with col_derecha:
            pr1 = laptops[0].get_price()
            text(f"Precio: {pr1} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad1"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar1",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda1, col_derecha1 = columns(2)
        with col_izquierda1:
           image("imgs\lap_2.jpg", width=290)
        with col_derecha1:
            pr2 = laptops[1].get_price()
            text(f"Precio: {pr2} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad2"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar2",on_click=incremento,kwargs=dict(incremento = 1*cantidad*20))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda2, col_derecha2 = columns(2)
        with col_izquierda2:
           image("imgs\lap_3.jpg" ,width= 290)
        with col_derecha2:
            pr3 = laptops[2].get_price()
            text(f"Precio: {pr3} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad3"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda3, col_derecha3 = columns(2)
        with col_izquierda3:
           image("imgs\lap_4.jpg" ,width= 290)
        with col_derecha3:
            pr4 = laptops[3].get_price()
            text(f"Precio: {pr4} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad4"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

    with container():
        col_izquierda4, col_derecha4 = columns(2)
        with col_izquierda4:
           image("imgs\lap_5.jpg" ,width= 290)
        with col_derecha4:
            pr5 = laptops[4].get_price()
            text(f"Precio: {pr5} USD")
            text("Tiempo de envio: 1 día")
            cantidad = int(number_input("Escoge la cantidad", 0,10,key="cantidad5"))
            if cantidad >= 1:
                button2 = button("Añadir al carrito", key="comprar3", on_click=incremento,kwargs=dict(incremento = 1*cantidad*300))
                if button2:
                    success("Añadido al carrito!")
        write("---")

#------------------------------------------------------------------------------------------------------------------------

if selected == "Carrito":
    title("Carrito")
    write("Gracias por tu elección! Este es el total de tu compra.")
    confirmar_compra = button("Confirmar compra", key= "confirmar")
    if confirmar_compra:
        session_state.precio = 0
        success("Compra exitosa!")
    write("Precio total a pagar: ")
    st_lottie(lottie3, key="carritodecompras")
    
if selected == "Cerrar sesion":
    title("Hasta luego! , Vuelva pronto")
    write("Despedida aqui")
    back_to_page("","Cerrar sesion")
    st_lottie(lottie2, key="despedida")    