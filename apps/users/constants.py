WEBMASTER = 1
PROPRIETARIO = 2
OPERADOR = 3
VENDEDOR = 4


USER_TYPE_NAME = {
    WEBMASTER: "Webmaster",
    PROPRIETARIO: "Proprietário",
    OPERADOR: "Operador",
    VENDEDOR: "Vendedor",
}

USER_TYPE_CHOICES = (
    (WEBMASTER, USER_TYPE_NAME[WEBMASTER]),
    (PROPRIETARIO, USER_TYPE_NAME[PROPRIETARIO]),
    (OPERADOR, USER_TYPE_NAME[OPERADOR]),
    (VENDEDOR, USER_TYPE_NAME[VENDEDOR]),
)