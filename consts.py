# URLs
SENCE_LOGIN_URL = "https://auladigital.sence.cl/login/index.php"
CLAVEUNICA_LOGIN_URL = "https://accounts.claveunica.gob.cl/accounts/login"

# Enlace principal del modulo
# Aca nos redirige el sitio de sence al entrar
MAIN_MODULE_URL = "https://auladigital.sence.cl/course/view.php"

# Enlace al que vamos a estar navegando de forma iterativa
SECONDARY_MODULE_URL = "https://auladigital.sence.cl/mod/quiz/view.php?id=679757"

# Nombre del curso donde queremos mantener el sistema corriendo
COURSE_NAME = "DESARROLLO DE APLICACIONES FULL STACK PYTHON TRAINEE V2.0 RTD-24-01-14-0039-2"

# Cada cuanto entra al navegador para actualizar el contador (minutos)
TIMER = 15

# El mismo timer en segundos
TIMER_SEGS = TIMER * 60

# Cuanto espera para navegar de una página a otra (segundos)
TIMER_BETWEEN_NAVIGATION = 2

# Duracion del curso por dia (minutos)
DURACION_CURSO_X_DIA = 180

# Cantidad maxima de loops
# Esto no valida la cantidad de veces que visito la pagina
# Solo es para no tener corriendo la aplicacion de forma infinita
# El calculo es así:
# - Las clases duran 3 horas (de 3pm a 6pm) = 180minutos
# - Hay que navegar en el aula para que el sistema sume el tiempo cada 15mins aprox
#   - Este punto es configurable pero debería ser inferior a 30 minutos
# - 180/15 = 12
MAX_LOOPS = DURACION_CURSO_X_DIA // TIMER
