from utils import get_sections, get_frames, make_gif
from PIL import Image, ImageChops

def test(n, f, tests, type_=None):
    success = failed = 0
    for inputs_, output_ in tests:
        try:
            if type_ == 'img':
                assert sum(sum(chanels) for chanels in ImageChops.difference(f(*inputs_), Image.open(output_)).getdata()) < 10
            elif type_ == 'gif':
                images = f(*inputs_)
                gif = Image.open(output_)
                n0 = 0
                i0 = i1 = 0
                while i0 < gif.n_frames and i1 < len(images):
                    gif.seek(i0)
                    diff = None
                    while diff is None and i0 < gif.n_frames:
                        try:
                            diff = sum(sum(chanels) for chanels in ImageChops.difference(images[i1], gif).getdata())
                        except ValueError:
                            i0 +=1
                            gif.seek(i0)
                    while diff > 10 and i1 < len(images):
                        diff = sum(sum(chanels) for chanels in ImageChops.difference(images[i1], gif).getdata())
                        i1 += 1
                    n0 += 1
                    i0 +=1
                    i1 += 1
                assert n0 > 0.9 * gif.n_frames
            else:
                assert f(*inputs_) == output_
            success += 1
        except AssertionError:
            failed += 1
    print(f"TEST {n}: {success} exitosos y {failed} erróneos")

tests1 = [
    (([-0.5, -0.4, 0.1, -0.2, 0.3, -0.1, -0.2, -0.7],), [
        {'acceleration': 4.5, 'time': 2.11, 'final_height': 295.0, 'final_x': 5.0, 'final_velocity': 9.49},
        {'acceleration': 3.6, 'time': 0.9, 'final_height': 291.0, 'final_x': 11.0, 'final_velocity': 12.73},
        {'acceleration': -0.9, 'time': 0.81, 'final_height': 292.0, 'final_x': 20.0, 'final_velocity': 12.0},
        {'acceleration': 1.8, 'time': 0.79, 'final_height': 290.0, 'final_x': 28.0, 'final_velocity': 13.42},
        {'acceleration': -2.7, 'time': 0.81, 'final_height': 293.0, 'final_x': 35.0, 'final_velocity': 11.23},
        {'acceleration': 0.9, 'time': 0.86, 'final_height': 292.0, 'final_x': 44.0, 'final_velocity': 12.0},
        {'acceleration': 1.8, 'time': 0.79, 'final_height': 290.0, 'final_x': 52.0, 'final_velocity': 13.42},
        {'acceleration': 6.3, 'time': 0.65, 'final_height': 283.0, 'final_x': 55.0, 'final_velocity': 17.5}]),
    (([-0.5, -0.4, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],), [
        {'acceleration': 4.5, 'time': 2.11, 'final_height': 295.0, 'final_x': 5.0, 'final_velocity': 9.49},
        {'acceleration': 3.6, 'time': 0.9, 'final_height': 291.0, 'final_x': 11.0, 'final_velocity': 12.73},
        {'acceleration': 0, 'time': 0.79, 'final_height': 291.0, 'final_x': 21.0, 'final_velocity': 12.73},
        {'acceleration': -0.9, 'time': 0.81, 'final_height': 292.0, 'final_x': 30.0, 'final_velocity': 12.0},
        {'acceleration': -1.8, 'time': 0.89, 'final_height': 294.0, 'final_x': 38.0, 'final_velocity': 10.39},
        {'acceleration': -2.7, 'time': 1.13, 'final_height': 297.0, 'final_x': 45.0, 'final_velocity': 7.35}])
    ]

tests2 = [
    (([
        {'acceleration': 4.5, 'time': 2.11, 'final_height': 295.0, 'final_x': 5.0, 'final_velocity': 9.49},
        {'acceleration': 3.6, 'time': 0.9, 'final_height': 291.0, 'final_x': 11.0, 'final_velocity': 12.73},
        {'acceleration': -0.9, 'time': 0.81, 'final_height': 292.0, 'final_x': 20.0, 'final_velocity': 12.0},
        {'acceleration': 1.8, 'time': 0.79, 'final_height': 290.0, 'final_x': 28.0, 'final_velocity': 13.42},
        {'acceleration': -2.7, 'time': 0.81, 'final_height': 293.0, 'final_x': 35.0, 'final_velocity': 11.23},
        {'acceleration': 0.9, 'time': 0.86, 'final_height': 292.0, 'final_x': 44.0, 'final_velocity': 12.0},
        {'acceleration': 1.8, 'time': 0.79, 'final_height': 290.0, 'final_x': 52.0, 'final_velocity': 13.42},
        {'acceleration': 6.3, 'time': 0.65, 'final_height': 283.0, 'final_x': 55.0, 'final_velocity': 17.5}], 1), 
    {'duration': 8.0, 'frames': [
        {'section': 0, 'distance': 0.0},
        {'section': 0, 'distance': 2.25},
        {'section': 0, 'distance': 9.0},
        {'section': 1, 'distance': 9.87},
        {'section': 3, 'distance': 2.19},
        {'section': 4, 'distance': 5.03},
        {'section': 5, 'distance': 6.66},
        {'section': 6, 'distance': 9.11}]}),
    (([
        {'acceleration': 4.5, 'time': 2.11, 'final_height': 295.0, 'final_x': 5.0, 'final_velocity': 9.49},
        {'acceleration': 3.6, 'time': 0.9, 'final_height': 291.0, 'final_x': 11.0, 'final_velocity': 12.73},
        {'acceleration': 0, 'time': 0.79, 'final_height': 291.0, 'final_x': 21.0, 'final_velocity': 12.73},
        {'acceleration': -0.9, 'time': 0.81, 'final_height': 292.0, 'final_x': 30.0, 'final_velocity': 12.0},
        {'acceleration': -1.8, 'time': 0.89, 'final_height': 294.0, 'final_x': 38.0, 'final_velocity': 10.39},
        {'acceleration': -2.7, 'time': 1.13, 'final_height': 297.0, 'final_x': 45.0, 'final_velocity': 7.35}], 1),
    {'duration': 7.0, 'frames': [
        {'section': 0, 'distance': 0.0},
        {'section': 0, 'distance': 2.25},
        {'section': 0, 'distance': 9.0},
        {'section': 1, 'distance': 9.87},
        {'section': 3, 'distance': 2.53},
        {'section': 4, 'distance': 4.54},
        {'section': 5, 'distance': 4.86}
        ]}),
    ]
tests3 = [
    (([-0.5, -0.4, 0.1, -0.2, 0.3, -0.1, -0.2, -0.7],), 'test-resources/1.gif'),
    (([-0.5, -0.4, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],), 'test-resources/2.gif'),
]

test(1, get_sections, tests1)
test(2, get_frames, tests2)
test(3, make_gif, tests3, 'gif')