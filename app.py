from streamlit import *
import sys
from streamlit.web import cli as stcli
from streamlit import runtime
from utils import nav_page, hide_pages


def main():
    set_page_config(initial_sidebar_state="collapsed")
    hide_pages()

    title("Computer RM")

    subheader("Bienvenido a nuestra tienda virtual!\nLa contraseña por defecto es 'password'")
    usuario = text_input("Usuario")
    password = text_input("Escriba su contraseña", type="password")
    button_ = button("Log In" , key="log in")
    if password == "password"  and usuario != "" and button_:
        nav_page("tienda")

    if password != "password" and usuario != "" and button_:
        if password == "":
            warning("Faltan datos")
        else:
            warning("Datos incorrectos")    
    


if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
