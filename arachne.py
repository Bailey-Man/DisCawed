# imports
from stitch_generator.collection.subdivision.tatami import tatami
from stitch_generator.subdivision.subdivide_by_length import regular
from stitch_generator.subdivision.subdivision_modifiers import alternate_direction, add_start
from stitch_generator.stitch_effects.path_effects.satin import satin
from stitch_generator.shapes.line import line
from stitch_generator.framework.path import Path
from stitch_generator.functions.functions_1d import constant
from stitch_generator.shapes.bezier import bezier
from pyembroidery import EmbPattern, write_png

def main(args):
    # get image from specified input path
    input_image_path = ''
    
    # specify output path
    output_image_path = ''


# script start

line_subdivision = add_start(alternate_direction(
    tatami(segment_length=3, steps=5, repetitions=1, minimal_segment_size=2)))

effect = satin(spacing_function=regular(2),
               line_subdivision=line_subdivision)

control_points = [(-50, 0), (-20, 20), (20, -20), (50, 0)]
shape, direction = bezier(control_points)
path = Path(shape=shape, direction=direction, width=constant(10), stroke_alignment=constant(0.5))

stitches = effect(path)

# use pyembroidery to save to path
scale_factor = 10  # convert from millimeters to embroidery file scale 1/10 mm

scaled_stitches = stitches * scale_factor
pattern = EmbPattern()
pattern.add_block(scaled_stitches.tolist(), "red")

write_png(pattern, 'test.png')

# # main function
# def function_a():
#     print("Function A")

# print("before function_b")
# def function_b():
#     print("Function B {}".format(math.sqrt(100)))

# print("before __name__ guard")
# if __name__ == '__main__':
#     function_a()
#     function_b()
# print("after __name__ guard")