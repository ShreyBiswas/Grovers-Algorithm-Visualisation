from manim import *
import grover_algorithm

############ ANIMATION ####################

def statevec_to_points(statevec,x_coords,colours):
    points = []
    lines = []
    old_point = False

    for i in range(len(statevec)):
        y_coord = statevec[i]*1.5*UP

        new_point = Dot(x_coords[i]+y_coord,color=colours[i],radius=0.02,fill_opacity=1)
        points.append(new_point)

        if old_point:
            line = Line(old_point,new_point,color=colours[i])
            line.set_opacity(0.2)
            lines.append(line)

        old_point = new_point

    return points,lines


def statevec_to_circle(statevec,circle_centre,circle_angles,colours):
    lines = []

    for i in range(len(statevec)):
        endpoint = circle_centre + 3*RIGHT*statevec[i]*np.cos(circle_angles[i]) + 3*UP*statevec[i]*np.sin(circle_angles[i]) # calculate end of line with trigonometry

        line = Line(circle_centre,endpoint,color=colours[i])
        line.set_opacity(0.3)
        lines.append(line)

    return lines

class Grover_Animation(GraphScene):

    def construct(self):


        length = 4

        statevectors = grover_algorithm.Get_Grover_Statevectors()
        statevectors /= np.amax(statevectors) # normalise for display
        point_count = len(statevectors[0])

        graph_centre = ORIGIN + (2.5*DOWN)
        circle_centre = ORIGIN + (1.5*UP)
        counter = ORIGIN + 4*LEFT

        x_axis = Line(graph_centre+3*LEFT,graph_centre+3*RIGHT,color=LIGHT_GREY)
        x_axis.set_opacity(0.3)

        x_coords = np.linspace(graph_centre+3*LEFT,graph_centre+3*RIGHT,num=point_count)
        circle_angles = np.linspace(0,2*np.pi,num=point_count)-np.pi/2 # start at the top, loop around

        statevectors = abs(statevectors)    #deal with complex numbers
        colours = color_gradient((RED,YELLOW,GREEN,BLUE,PURPLE),point_count) # rainbow

        old_points,old_points_lines = statevec_to_points(statevectors[0],x_coords,colours) # generate bar/line graph
        old_circle_lines = statevec_to_circle(statevectors[0],circle_centre,circle_angles,colours) # generate rose chart
        old_count = Tex(r'$0$',color=BLUE,fill_color=GREEN)
        old_count.next_to(counter)

        statevectors = statevectors[1:] # remove first statevector, already animated

        animation = AnimationGroup(*[ShowCreation(old_point) for old_point in old_points], # animate creation
                                *[ShowCreation(old_point_line) for old_point_line in old_points_lines],
                                *[ShowCreation(old_circle_line) for old_circle_line in old_circle_lines],
                                ShowCreation(x_axis),
                                ShowCreation(old_count))
        self.play(animation)
        self.wait(0.5)

        for i in range(len(statevectors)):

            new_points,new_points_lines = statevec_to_points(statevectors[i],x_coords,colours)
            new_circle_lines = statevec_to_circle(statevectors[i],circle_centre,circle_angles,colours)
            new_count = Tex(r'$'+str(i+1)+r'$',color=BLUE,fill_color=GREEN)
            new_count.next_to(counter)

            # smooth transition
            animation = AnimationGroup(*[Transform(old_point,new_point) for old_point,new_point in zip(old_points,new_points)],
                                        *[Transform(old_point_line,new_point_line) for old_point_line,new_point_line in zip(old_points_lines,new_points_lines)],
                                        *[TransformFromCopy(old_circle_line,new_circle_line) for old_circle_line,new_circle_line in zip(old_circle_lines,new_circle_lines)],
                                        Transform(old_count,new_count))

            fade = AnimationGroup(*[FadeOut(old_circle_line) for old_circle_line in old_circle_lines])

            self.play(animation,fade)

            old_circle_lines = new_circle_lines

        self.wait(0.5)


