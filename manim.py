from asyncore import write
from tkinter import BOTTOM, LEFT, RIGHT
from turtle import color, fillcolor
from typing import Text
from venv import create
from xml.etree.ElementTree import PI
from manim import *
from manimpango import *




class Dawal_Func_Def(Scene):
    def construct(self):
        sq = Square(color=GREEN,fill_opacity=0.4)
        ar1 = Arrow(color= GREEN)
        ar1.next_to(sq,LEFT)
        ar2 = Arrow(color= GREEN)
        ar2.next_to(sq,RIGHT)
        fx = Text("f ")
        x_char = Text("x")
        x_char.next_to(ar1, LEFT)
        y_char = Text("y")
        y_char.next_to(ar2, RIGHT)
        self.play(Create(VGroup(sq , fx),color=RED))
        self.play(Create(VGroup(x_char,ar1 , ar2,y_char)))
        self.wait()
        self.play(Indicate(VGroup(sq , fx)),run_time=5)
        self.play(Indicate(VGroup(x_char,ar1 ),color=RED),run_time=5)
        self.play(Wiggle(sq,n_wiggles=5,rotation_angle=PI/3,run_time=5))  
        self.play(Indicate(VGroup(ar2,y_char ),color=RED),run_time=5) 
        self.play(Indicate(VGroup(x_char,ar1 ),color=RED),run_time=5)
        self.play(Indicate(VGroup(ar2,y_char ),color=RED),run_time=5)  
        text = Tex("f: X $\longrightarrow$ Y",font_size=70).shift(2*DOWN)
        self.add(text)
        self.wait()



        