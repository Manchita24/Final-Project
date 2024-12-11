define hombre = Character ("Victor")
define prota = Character ("Jace")
define jugador = Character ("Rory")


label start:
  scene fondo1

  " It is 2040, after the third war all the world has changed. humans are not alone anymore"
  "A new predador has appeared"
  " The Zombies"

  show main1

  prota " Hola Rory"
  " I am happy that you are alive "
  " please join us on this advnture"

  jugador " ehh, what adventure"
  prota " Maybe you do not remeber, but we have a mission"
  " saving the planet"
  " what is your answer"

  menu:
    "yes":
        jump respuestayes
    "No":
        call respuestano
  return 




label respuestayes:
    "esta es una instruccion...yes"
    return
label respuestano:
    "esta es una instruccion..no"
    return