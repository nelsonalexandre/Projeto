from manimlib.imports import *
from math import radians,sin,cos,sqrt

class Mediatriz(Scene):
    def construct(self):

        reta_r = Line(4*LEFT, 4*RIGHT, color=BLACK)
        ponto_a = Dot(4*LEFT, color=BLUE_F)
        A = TextMobject("A", color=BLACK)
        A.next_to(ponto_a, UP)

        ponto_b = Dot(4*RIGHT, color=BLUE_F)
        B = TextMobject("B", color=BLACK)
        B.next_to(ponto_b, UP)

        print("passo-1")
        self.play(ShowCreation(reta_r), ShowCreation(ponto_a), Write(A), ShowCreation(ponto_b), Write(B)) #1
        self.wait(1) #2

        print("passo-2")
        ponto_a.set_color(RED_F)
        arc1 = Arc(start_angle=math.radians(-50), angle=math.radians(100), arc_center=4*LEFT, radius=5, color=GREEN_F)
        self.play(ShowCreation(arc1)) #3
        ponto_a.set_color(BLUE_F)
        self.wait(1) #4

        print("passo-2")
        ponto_b.set_color(RED_F)
        arc2 = Arc(start_angle=math.radians(230), angle=math.radians(-100), arc_center=4*RIGHT, radius=5, color=PURPLE_F)
        self.play(ShowCreation(arc2)) #5
        ponto_b.set_color(BLUE_F)
        self.wait(1) #6

        ponto_C = Dot(3*UP, color=BLUE_F)
        C = TextMobject("C", color=BLACK)
        C.next_to(ponto_C, UP)

        ponto_D = Dot(3*DOWN, color=BLUE_F)
        D = TextMobject("D", color=BLACK)
        D.next_to(ponto_D, DOWN)

        print("passo-4")
        self.play(ShowCreation(ponto_C), ShowCreation(ponto_D), FadeOut(arc1), FadeOut(arc2))
        self.play(Write(C), Write(D))
        self.wait(1)

        reta_s = Line(3*DOWN, 3*UP, color=BLACK)
        ponto_M = Dot(color=BLUE_F)
        M = TextMobject("M")
        M.next_to(ponto_M, UP+RIGHT)

        print("passo-5")
        self.play(ShowCreation(reta_s))
        self.play(FadeOut(ponto_C), FadeOut(ponto_D), FadeOut(C), FadeOut(D))
        self.play(ShowCreation(ponto_M), Write(M))
        self.wait(1)

class Transferencia(Scene):
    def construct(self):

        reta_r = Line(4*LEFT, 4*RIGHT, color=BLACK)

        ponto_a = Dot(4*LEFT, color=BLUE_F)
        A = TextMobject("A", color=BLACK)
        A.next_to(ponto_a, UP)

        ponto_b = Dot(2*LEFT, color=BLUE_F)
        B = TextMobject("B", color=BLACK)
        B.next_to(ponto_b, UP)

        ponto_c = Dot(4*RIGHT, color=BLUE_F)
        C = TextMobject("C", color=BLACK)
        C.next_to(ponto_c, UP)

        print("passo-1")
        self.play(ShowCreation(reta_r), ShowCreation(ponto_a), Write(A))
        self.wait(1)

        print("passo-2")
        self.play(ShowCreation(ponto_b), ShowCreation(ponto_c), Write(C), Write(B))

        print("passo-3")
        circ1 = Arc(start_angle=math.radians(0), angle=math.radians(360), radius=2, arc_center=2*LEFT, color=GREEN_F)
        ponto_n = Dot(color=BLUE_F)
        N = TextMobject("N", color=BLACK)
        N.next_to(ponto_n, UP)

        ponto_b.set_color(RED_F)
        self.play(ShowCreation(circ1))
        ponto_b.set_color(BLUE_F)
        self.play(ShowCreation(ponto_n), Write(N), FadeOut(circ1))

        circ2 = Arc(start_angle=math.radians(0), angle=math.radians(360), radius=1, arc_center=RIGHT, color=PURPLE_F)
        ponto_m = Dot(RIGHT, color=BLUE_F)
        M = TextMobject("M", color=BLACK)
        M.next_to(ponto_m, UP)

        print("passo-4")
        self.play(ShowCreation(ponto_m), Write(M))

        print("passo-5")
        ponto_x = Dot(2*RIGHT, color=BLUE_F)
        X = TextMobject("X", color=BLACK)
        X.next_to(ponto_x, UP)
        ponto_m.set_color(RED_F)
        self.play(ShowCreation(circ2))
        ponto_m.set_color(BLUE_F)
        self.play(ShowCreation(ponto_x), Write(X), FadeOut(circ2))
        self.wait(1)

        print("passo-6")
        seg_ax = Line(np.array((-4, -1, 0)), np.array((2, -1, 0)), color=GREEN_F)
        AX = TextMobject("AX", color=BLACK)

        self.play(ShowCreation(seg_ax))
        self.play(ApplyMethod(seg_ax.move_to, np.array((-3, -2, 0))))
        AX.next_to(seg_ax, UP)
        self.play(Write(AX))
        self.wait(1)

        seg_bc = Line(np.array((-2, -1, 0)), np.array((4, -1, 0)), color=PURPLE_F)
        BC = TextMobject("BC", color=BLACK)

        self.play(ShowCreation(seg_bc))
        self.play(ApplyMethod(seg_bc.move_to, np.array((-3, -3, 0))))
        BC.next_to(seg_bc, UP)
        self.play(Write(BC))
        self.wait(1)

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))

class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

class Lema(Scene):
    def construct(self):

        ponto_O = Dot((-4, -3, 0), color=BLUE_F)
        O = Text("O")
        O.next_to(ponto_O, LEFT+DOWN)

        eixo_y = Line(ponto_O, np.array((-4, 8, 0)), color=BLACK)
        eixo_x = Line(ponto_O, np.array((6, -3, 0)), color=BLACK)

        ponto_1 = Dot(np.array((-4, -2,0)), color=BLUE_F)
        Um = Text("1")
        ponto_A = Dot(np.array((-1, -3, 0)), color=BLUE_F)
        A = Text("A")
        A.next_to(ponto_A, DOWN)
        ponto_B = Dot(np.array((0, -3, 0)), color=BLUE_F)
        B = Text("B")
        B.next_to(ponto_B, DOWN)
        ponto_C = Dot((3, -3, 0), color=BLUE_F)
        C = Text("A+B")
        C.next_to(ponto_C, UP)
        ponto_D = Dot((-3, -3,0), color=BLUE_F)
        D = Text("B - A")
        D.next_to(ponto_D, UP)

        seg_a = Line((-4, -3, 0),(-1, -3, 0), color=GREEN_F, stroke_width=10)
        seg_b = Line((0, -3, 0), (-1, -3, 0), color=PURPLE_F, stroke_width=10)

        centro = (0, -3, 0)

        raio = 3

        theta = ValueTracker(0)
        linha = Line(centro, centro+RIGHT*raio,color=GREEN_F, stroke_width=10)
        circ = Arc(start_angle=math.radians(0), angle=math.radians(360), arc_center=centro, radius=raio, color=PURPLE_F, stroke_width=10)

        alpha = TexMobject("\\alpha", color=BLACK)

        self.add(eixo_y, eixo_x, ponto_O) #0
        self.play(ShowCreation(ponto_A), ShowCreation(ponto_B))
        self.play(Write(A), Write(B), Write(O))
        self.wait() #3

#Compasso
        seg_a.rotate(theta.get_value(),about_point=centro)
        seg_a.add_updater(lambda m: m.set_angle(theta.get_value()))
        alpha.add_updater(lambda m: m.next_to(seg_a.get_center(), UP))
        self.play(ShowCreation(seg_a)) #4
        self.play(Write(alpha))
        self.wait() #5
        self.play(ApplyMethod(seg_a.move_to, np.array((1.5, -3, 0))))
        self.wait() #7
        self.add(ponto_A, ponto_B)
        self.wait()
        self.play(ShowCreation(circ), theta.increment_value,2*PI, rate_func=smooth, run_time=2)

#Pontos C e D
        self.play(
            FadeOut(seg_a),
            FadeOut(alpha),
            circ.set_stroke,{"opacity":0.5},
            ShowCreation(ponto_C),
            ShowCreation(ponto_D)
            )
        self.wait()
        self.play(Write(C),
            Write(D),
            FadeOut(circ))

class Lema2(Scene):
    def construct(self):
#A . B:
        ponto_O = Dot((-4, -3, 0), color=BLUE_F)
        O = Text("O")
        O.next_to(ponto_O, LEFT+DOWN)
        eixo_y = Line(ponto_O, np.array((-4, 8, 0)), color=BLACK)
        eixo_x = Line(ponto_O, np.array((6, -3, 0)), color=BLACK)

        ponto_A = Dot((-4, 0, 0), color=BLUE_F) # (0, 1.5)
        A = Text("A")
        A.next_to(ponto_A, LEFT)

        ponto_B = Dot((0, -3, 0), color=BLUE_F) # (2, 0)
        B = Text("B")
        B.next_to(ponto_B, DOWN)

        ponto_1 = Dot((-2, -3,0), color=BLUE_F) # (1, 0)
        Um = Text("1")
        Um.next_to(ponto_1, DOWN)

        ponto_1y = Dot((-4, -1,0), color=BLUE_F) # (0, 1)
        Um_y = Text("1")
        Um_y.next_to(ponto_1y, LEFT)

        ponto_AB = Dot((2, -3, 0), color=BLUE_F) # (3, 0)
        AB = Text("AB")
        AB.next_to(ponto_AB, UP)

        ponto_A_B = Dot((-4, -1.5, 0), color=BLUE_F) # (3, 0)
        A2 = Text("A")
        Underline = Text("_", stroke_width=5)
        B2 = Text("B")
        Underline.next_to(ponto_A_B, LEFT)
        A2.next_to(Underline, UP, buff=0.2)
        B2.next_to(Underline, DOWN, buff=0.2)

#Plot-pontos
        self.add(eixo_y, eixo_x, ponto_O, O) #0
        self.play(ShowCreation(ponto_1y))
        self.play(ShowCreation(ponto_A), ShowCreation(ponto_B))
        self.play(Write(A), Write(B), Write(Um_y))
        self.wait() #4

#Segmento_B1
        seg_b = Line((2, -4, 0), (-4, -1,0), color=GREEN_F)
        self.play(ShowCreation(seg_b)) #5
        self.wait() #6

#Segmento_AAB
        seg_a = Line((4, -5, 0), (-4, -1,0), color=GREEN_F)
        self.add(seg_a)
        self.play(ApplyMethod(seg_a.move_to, (0, -2, 0))) #7
        self.add(ponto_A, ponto_B)
        self.play(ShowCreation(ponto_AB))
        self.play(Write(AB))
        self.wait() #10
        self.play(FadeOut(seg_a), FadeOut(seg_b), FadeOut(Um_y), FadeOut(ponto_1y))
        self.wait() #12


#A/B:
#reta: y= -0.75x + 3
        seg_c = Line((4, -6, 0), (-4, 0, 0), color=PURPLE_F)
#reta: y= -1.5x + 1.5
        seg_d = Line((4, -6, 0), (-4, 0, 0), color=PURPLE_F)

        self.play(ShowCreation(ponto_1), Write(Um)) #13
        self.play(ShowCreation(seg_c))
        self.wait() #15
        self.play(ApplyMethod(seg_d.move_to, (0, -4.5, 0)))
        self.wait() #17
        self.add(ponto_A)
        self.play(ShowCreation(ponto_A_B))
        self.wait()
        self.play(Write(A2), Write(Underline), Write(B2))
        self.wait()
        self.play(FadeOut(seg_d), FadeOut(seg_c))
        self.wait()

class Compasso(Scene):
        def construct(self):
            centro = (-4, -3, 0)

            raio = 2

            theta = ValueTracker(0)
            linha = Line(centro, centro+RIGHT*raio,color=GREEN_F, stroke_width=10)
            circ = Arc(start_angle=math.radians(0), angle=math.radians(360), arc_center=centro, radius=raio, color=PURPLE_F, stroke_width=10)

            linha.rotate(theta.get_value(),about_point=centro)
            linha.add_updater(lambda m: m.set_angle(theta.get_value()))

            self.play(ShowCreation(linha))
            self.wait()
            self.play(ShowCreation(circ), theta.increment_value,2*PI, rate_func=smooth, run_time=2)

            self.play(
                FadeOut(linha),
                circ.set_stroke,{"opacity":0.5}
                )

class Lema3(Scene):
    def construct(self):
        ponto_O = Dot((-4, -3, 0), color=BLUE_F)
        O = Text("O")
        O.next_to(ponto_O, LEFT+DOWN)

        eixo_y = Line(ponto_O, np.array((-4, 8, 0)), color=BLACK)
        eixo_x = Line(ponto_O, np.array((6, -3, 0)), color=BLACK)
        self.add(eixo_y, eixo_x, ponto_O)

        ponto_1 = Dot(np.array((-2, -3,0)), color=BLUE_F)
        Um = Text("1")
        Um.next_to(ponto_1, DOWN)
        ponto_A = Dot(np.array((0, -3, 0)), color=BLUE_F)
        A = Text("A")
        A.next_to(ponto_A, DOWN)
        ponto_A1 = Dot(np.array((2, -3, 0)), color=BLUE_F)
        A1 = Text("A+1")
        A1.next_to(ponto_A1, DOWN)

        self.play(ShowCreation(ponto_A), ShowCreation(ponto_1))
        self.play(Write(A), Write(Um), Write(O))

        seg_1 = Line(ponto_O, ponto_1, color=GREEN_F, stroke_width=10)

        self.play(ApplyMethod(seg_1.move_to, (1, -3, 0)))
        self.play(ShowCreation(ponto_A1))
        self.play(FadeOut(seg_1))
        self.play(Write(A1))
        self.wait()

        ponto_M = Dot(np.array((-1, -3, 0)), color=BLUE_F)
        M = Text("M")
        M.next_to(ponto_M, DOWN)

        self.play(ShowCreation(ponto_M))
        self.wait()

        centro = (-1, -3, 0)

        raio = 3

        theta = ValueTracker(0)
        linha = Line(centro, centro+RIGHT*raio,color=GREEN_F, stroke_width=10)
        circ = Arc(start_angle=math.radians(0), angle=math.radians(360), arc_center=centro, radius=raio, color=PURPLE_F, stroke_width=10)

        linha.rotate(theta.get_value(),about_point=centro)
        linha.add_updater(lambda m: m.set_angle(theta.get_value()))

        self.play(ShowCreation(linha))
        self.wait()
        self.play(ShowCreation(circ), theta.increment_value,2*PI, rate_func=smooth, run_time=2)

        self.play(
            FadeOut(linha),
            circ.set_stroke,{"opacity":0.5}
            )

        raiz_8 = math.sqrt(8)


        ponto_P = Dot(np.array((0, -3+math.sqrt(8),0)), color=BLUE_F)
        P = Text("P")
        P.next_to(ponto_P, UP)

        perpendicular_A = Line(ponto_A, ponto_P, color=GREEN_F)

        self.play(ShowCreation(perpendicular_A), ShowCreation(ponto_P))
        self.play(Write(P))
        self.wait()

        lado_a = Line(ponto_O, ponto_A, color=GREEN_F)
        a_text = Text("a")
        a_text.next_to(lado_a.get_center(), UP)
        lado_1 = Line(ponto_A, ponto_A1, color=GREEN_F)
        um_text = Text("1")
        um_text.next_to(lado_1.get_center(), UP)
        lado_c = Line(ponto_O, ponto_P, color=GREEN_F)
        c_text = Text("c")
        c_text.next_to(lado_c.get_center(), UP)
        lado_b = Line(ponto_A1, ponto_P, color=GREEN_F)
        b_text = Text("b")
        b_text.next_to(lado_b.get_center(), RIGHT)
        altura_h = Text("h")
        altura_h.next_to(perpendicular_A, LEFT)

        self.play(ShowCreation(lado_c), ShowCreation(lado_b))
        self.play(FadeOut(circ), FadeOut(ponto_1), FadeOut(Um), FadeOut(ponto_M))
        self.play(Write(c_text), Write(b_text), Write(a_text), Write(um_text), Write(altura_h))
        self.wait()
