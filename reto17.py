"""/*
* Reto #17
* LA CARRERA DE OBSTÁCULOS
* Fecha publicación enunciado: 25/04/22
* Fecha publicación resolución: 02/05/22
* Dificultad: MEDIA
*
* Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
* carrera de obstáculos.
* - La función recibirá dos parámetros:
*      - Un array que sólo puede contener String con las palabras "run" o "jump"
*      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
* - La función imprimirá cómo ha finalizado la carrera:
*      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
*        variará el símbolo de esa parte de la pista.
*      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
*      - Si hace "run" en "|" (valla), se variará la pista por "/".
* - La función retornará un Boolean que indique si ha superado la carrera.
* Para ello tiene que realizar la opción correcta en cada tramo de la pista.
*
* Información adicional:
* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
* - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
* - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
*
*/"""

class Obstacle_Race:
    def __init__(self, race):
        self.athlete_tracker = []
        self.race = list(race)
        self.comparison = list(race)
    def run(self):
        return "_"
    def jump(self):
        return "|"
    def check_race(self,actions):
        if len(self.race) == len(actions):
            if len(self.race) :
                if actions[0] == self.race[0]:
                    self.athlete_tracker.append(actions[0])
                    del actions[0]
                    del self.race[0]
                    return self.check_race(actions)
                self.athlete_tracker.append("/") if self.run() == self.race[0] else self.athlete_tracker.append("/")
                del actions[0]
                del self.race[0]                
                return self.check_race(actions)
            else :
                return "The athelet completed race" if self.athlete_tracker == self.comparison else "The athelet no completed race"
        else :
            return "The athelet no completed race"
if __name__ == "__main__":
    athlete_1= Obstacle_Race("_|_|_")
    athlete_2= Obstacle_Race("_|_|_")
    athlete_3= Obstacle_Race("______")
    athlete_4= Obstacle_Race("_|_|_")
    athlete_5= Obstacle_Race("_|_|_")
    athlete_6= Obstacle_Race("|||||")
    athlete_7= Obstacle_Race("|??||")
    print(athlete_1.check_race([athlete_1.run(), athlete_1.jump(), athlete_1.run(), athlete_1.jump(), athlete_1.run()]))
    print(athlete_2.check_race([athlete_2.run(), athlete_2.run(), athlete_2.run(), athlete_2.jump(), athlete_2.run()]))
    print(athlete_3.check_race([athlete_3.run(), athlete_3.run(), athlete_3.run(), athlete_3.run(), athlete_3.run(), athlete_3.run()]))
    print(athlete_4.check_race([athlete_4.run(), athlete_4.run(), athlete_4.jump(), athlete_4.jump(), athlete_4.run()]))
    print(athlete_5.check_race([athlete_5.run(), athlete_5.jump(), athlete_5.run(), athlete_5.jump()]))
    print(athlete_6.check_race([athlete_6.jump(), athlete_6.jump(), athlete_6.jump(), athlete_6.jump(), athlete_6.jump()]))
    print(athlete_7.check_race([athlete_7.jump(), athlete_7.jump(), athlete_7.jump(), athlete_7.jump(), athlete_7.jump()]))
      
                
