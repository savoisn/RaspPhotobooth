"""First API, local access only"""
import hug

@hug.get()
@hug.cli()
def add(number_1:hug.types.number, number_2:hug.types.number):
    """retruns a number being the result of the addition of the 2 arguments"""
    return number_1 + number_2

if __name__ == '__main__':
    add.interface.cli()

