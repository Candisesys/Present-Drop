from pyray import * 
import classes
import tkinter.messagebox

init_window(800, 600, "Present Drop")

latte = load_font_ex("data/gfx/latte.ttf", 24, None, 0)
set_target_fps(120)

guy = classes.Guy(Vector2(300, 300 - 40), Vector2(0, 0))
houses = []
presents = []
i = 0
coll_gh = 0
score = 0


tkinter.messagebox.showinfo("Hello!", "Drop presents by pressing the S key.")
while not window_should_close(): 
    # Update 
    i += 1
    guy.update()
    guy.pos_vec.x += 350
    for house in houses:
        house.update()
        if (house.pos_vec.x < -(house.texture.width)):
            houses.remove(house)
        for present in presents:
            if (check_collision_recs(present.collrec, house.collrec)):
                coll_gh+=1
                if(coll_gh%(55-3)==0):
                    score += 1

    
    for present in presents:
        present.update()
    if (is_key_pressed(ord("S"))):
        newPresent = classes.Present(Vector2(0, 0), Vector2(0, 5))
        newPresent.pos_vec.y = guy.pos_vec.y + 10
        newPresent.pos_vec.x = guy.pos_vec.x + 10
        presents.append(newPresent)
    if (i%90==0):
        newHouse = classes.House(Vector2(850, 500), Vector2(-2, 0))
        houses.append(newHouse)
    # Draw 
    begin_drawing() 
    clear_background(SKYBLUE) 
    for present in presents:
        present.draw()
    guy.draw()
    for house in houses:
        house.draw()
    draw_text_ex(latte, str(score), Vector2(10, 0), 72, 0, BLACK)
    end_drawing()
 
close_window() 
