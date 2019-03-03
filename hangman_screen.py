import turtle as t

NUMBER_TO_FAIL = 10

def draw_word(word_so_far):
    t.penup()
    t.setpos(50,225)
    t.write(word_so_far, font=("Arial", 28, "normal"))


def draw_hangman(failed_letters):
    Letters = len(failed_letters)
    t.penup()
    t.setpos(50,25)

    t.speed(4)
    t.pensize(6)
    t.penup()
    t.left(180)
    t.forward(150)
    t.left(90)
    t.forward(100)
    t.pencolor("saddle brown")

    if Letters >= 1:
        t.pendown()
        t.right(90)
        t.forward(100)

    if Letters >= 2:
        t.right(90)
        t.forward(200)

    if Letters >= 3:
        t.right(90)
        t.forward(200)

    if Letters >= 4:
        t.left(180)
        t.forward(150)
        t.left(45)
        t.forward(70)
        t.right(180)
        t.forward(70)
        t.right(45)
        t.forward(50)

    if Letters >= 5:
        t.pencolor("sandy brown")
        t.right(90)
        t.forward(50)

    if Letters >= 6:
        t.pencolor("firebrick3")
        t.circle(10)

    if Letters >= 7:
        t.forward(55)

    if Letters >= 8:
        t.right(45)
        t.forward(25)
        t.left(180)
        t.forward(25)

    if Letters >= 9:
        t.right(90)
        t.forward(25)
        t.left(180)
        t.forward(25)

    if Letters >= 10:
        t.right(45)
        t.forward(25)
        t.right(90)
        t.forward(25)
        t.left(180)
        t.forward(50)


def draw(word_so_far, failed_letters):
    """Draw the word so far and the hangman

    (Might also draw the list of failed letters)
    Useful:
      reset -- starts again with a clear screen
      write -- writes text to the screen
    """
    
    t.reset()
    draw_word(" ".join(word_so_far))
    draw_hangman(failed_letters)

	
    #print("Word So Far : ",word_so_far,"\nFailed Letters : ",failed_letters)

	
def get_a_letter():
    """Prompt the user to enter a letter
    """
    #
    # HINT: turtle.textinput might help
    #
    
    text = t.textinput("Hangman", "Set me one").upper()
    
    return text

def get_difficulty():
    """Return a number showing how difficult
    """
    
    return int(t.textinput("Hangman", "How difficult?"))

def win_or_lose(wl):
	"""wl means win or lose
	"""
	
	
	if wl:
		
		t.reset()
		t.penup()
		t.setpos(50,225)
		
		t.write("You Won !!!", font=("Arial", 28, "normal"))
	
	else:
		
		t.reset()
		t.penup()
		t.setpos(50,225)
		
		t.write("You Lost !!!", font=("Arial", 28, "normal"))
	


if __name__=="__main__":
    
    draw(list("Memes"),list("irrelevent") )
