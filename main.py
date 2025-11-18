import os
import time
from consts import (COURSE_NAME, SENCE_LOGIN_URL, CLAVEUNICA_LOGIN_URL,
                    MAIN_MODULE_URL, SECONDARY_MODULE_URL,
                    TIMER_SEGS, TIMER_BETWEEN_NAVIGATION, MAX_LOOPS)
from playwright.sync_api import Page, sync_playwright
from utils import logger
from dotenv import load_dotenv

load_dotenv()


def login_sence(page: Page):
    # Visita el primer enlace de login sence
    page.wait_for_selector(selector="button[id=btnLogin]", timeout=60000)

    # Campo RUT
    rut_field = page.locator("input[name=username]")
    rut_field.press_sequentially(os.environ["RUT"])

    # Campo flecha
    # Realmente solo necesitamos perder el foco del campo RUT
    # Igualmente, para estar 100% seguros presionaremos la fecha
    arrow_btn = page.locator(
        'span.input-group-addon > i.fa-arrow-circle-right')
    arrow_btn.click()

    # Esperamos que aparezca el campo con los cursos
    course_name_field = page.locator("select[name=curso]")
    course_name_field.click()

    # Toma el boton para iniciar sesion
    login_button = page.locator("button[id=btnLogin]")
    login_button.click()


def login_claveunica(page: Page):
    # Campo de usuario ClaveUnica
    run_field = page.locator("input[name=run]")
    run_field.wait_for(state="visible")
    run_field.press_sequentially(os.environ["RUT"])

    # Campo clave ClaveUnica
    cu_field = page.locator("input[name=password]")
    cu_field.wait_for(state="visible")
    cu_field.press_sequentially(os.environ["CLAVE_UNICA"])

    # Boton login
    page.wait_for_selector(
        "button[class='w-100 gob-btn-primary']", timeout=60000)
    login_button = page.locator("button[id=login-submit]")
    login_button.click()


def run():

    if not os.environ["RUT"]:
        raise ValueError("Debes especificar tu RUT")

    if not os.environ["CLAVE_UNICA"]:
        raise ValueError(
            "Debes especificar tu clave única. IMPORTANTE: NO LA COMPARTAS NI LA SUBAS")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()

        # Login sence
        logger.debug(f"[run] Navegacion [1] a {SENCE_LOGIN_URL}")
        page.goto(SENCE_LOGIN_URL, wait_until="domcontentloaded")

        login_sence(page)

        logger.debug(f"[run] Navegacion [2] a {CLAVEUNICA_LOGIN_URL}")
        page.wait_for_url(CLAVEUNICA_LOGIN_URL + "/**",
                          wait_until="domcontentloaded", timeout=60000)

        login_claveunica(page)

        # Luego esperamos por el enlace del modulo al que nos dirige por defecto
        logger.debug(f"[run] Navegacion [3] a {MAIN_MODULE_URL}")

        page.wait_for_url(MAIN_MODULE_URL + "?id=**",
                          wait_until="domcontentloaded", timeout=60000)

        logger.info(f"[run] Entrando al loop")
        module_url = page.url
        loop_counter = 1

        while True:
            logger.info(f"[run] Iteración número [{loop_counter}]")
            logger.debug(f"[run] Navegacion [4] a {MAIN_MODULE_URL}")

            # Ya estamos en la pagina principal del modulo
            # Asi que comenzamos el loop navegando a la pagina secundaria
            logger.debug(f"[run] Navegacion [5] a {SECONDARY_MODULE_URL}")
            page.goto(SECONDARY_MODULE_URL,
                      wait_until="domcontentloaded", timeout=60000)

            # Un espacio de tiempo para no parecer tan bot
            logger.debug(
                f"[run] Esperando {TIMER_BETWEEN_NAVIGATION} segundos")
            time.sleep(TIMER_BETWEEN_NAVIGATION)

            # Volvemos a "module_url"
            logger.debug(f"[run] Navegacion [6] a {module_url}")
            page.goto(module_url, wait_until="domcontentloaded", timeout=60000)

            # Dormimos basado en TIMER
            logger.debug(
                f"[run] Esperando {TIMER_SEGS} segundos")
            time.sleep(TIMER_SEGS)

            # Cierra el navegador
            if loop_counter >= MAX_LOOPS:
                logger.info(f"[run] Se alcanzó el máximo de iteraciones")
                browser.close()
                break
            loop_counter += 1

        logger.info(f"[run] Saliendo al loop")


if __name__ == "__main__":
    try:
        logger.info(f"[main] Comienzo del proceso para curso")
        logger.info(f"[main] {COURSE_NAME}")
        run()
    except Exception as e:
        logger.error("Error en la ejecución")
        logger.error(e, exc_info=True)
    finally:
        logger.info(f"[main] Fin del proceso")
