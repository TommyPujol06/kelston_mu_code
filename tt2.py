import turtle

def fizzbuzz(n):
    results = []
    if n % 5 == 0:
        results.append("fizz")
    if n % 3 == 0:
        results.append("buzz")
    return results
    
for i in range(100): 
    result = fizzbuzz(i) 
    if 'fizz' in result: 
        turtle.right(90) 
    elif 'buzz' in result: 
        turtle.left(90) 
    turtle.forward(10)