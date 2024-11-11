# module_4_2

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    
    inner_function()

# Вызов функции test_function
test_function()

# Попытка вызова inner_function вне функции test_function
try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
  
