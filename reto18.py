"""/*
* Reto #18
* TRES EN RAYA
* Fecha publicación enunciado: 02/05/22
* Fecha publicación resolución: 09/05/22
* Dificultad: DIFÍCIL
*
* Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
* - "X" si han ganado las "X"
* - "O" si han ganado los "O"
* - "Empate" si ha habido un empate
* - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
* Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
*
* Información adicional:
* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
* - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
* - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
*
*/"""

from enum import Enum

class Value(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ''
class Triqui:
    combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    def __init__(self,grid):
        self.grid = grid
    def check_triqui(self):
        result = 'Draw'
        play_x = []
        play_o = []
        x_count = 0
        o_count = 0
        if len(self.grid) != 3 :
            return "Nulo"
        else:
            b = 1
            for row in self.grid:
                if len(row) !=  3 :
                    return "Nulo"
                for box in row :
                    if box == Value.X :
                        play_x.append(b)
                        x_count += 1
                    elif box == Value.O :
                        play_o.append(b)
                        o_count += 1
                    b += 1
            if abs(x_count - o_count) > 1:
                return "Nulo"
            for win in self.combinations:
                if len(set(win) & set(play_o)) == 3:
                    if result == 'Draw' :
                        result = Value.O.value
                    else:
                        return 'Nulo'
                elif len(set(win) & set(play_x)) == 3:
                    if result == 'Draw':
                        result = Value.X.value
                    else :
                        return "Nulo"
            return result if result == 'Draw' else f'Win {result}'
            
if __name__ == "__main__":
    grid_1 = [[Value.X, Value.O, Value.X],[Value.O, Value.X, Value.O],[Value.O, Value.O, Value.X]]
    grid_2 = [[Value.EMPTY, Value.O, Value.X],[Value.EMPTY, Value.X, Value.O],[Value.EMPTY, Value.O, Value.X]]
    grid_3 = [[Value.O, Value.O, Value.EMPTY],[Value.O, Value.X, Value.X],[Value.O, Value.X, Value.X]]
    grid_4 = [[Value.X, Value.O, Value.X],[Value.X, Value.X, Value.O],[Value.X, Value.X, Value.X]]
    triqui_1 = Triqui(grid_1)
    triqui_2 = Triqui(grid_2)
    triqui_3 = Triqui(grid_3)
    triqui_4 = Triqui(grid_4)
    print(triqui_1.check_triqui())        
    print(triqui_2.check_triqui())
    print(triqui_3.check_triqui())
    print(triqui_4.check_triqui())   
