from PIL import Image, ImageDraw, ImageChops

def get_sections(slopes):
    sections = []
    return sections

def get_frames(sections, fps):
    frames = []
    return {'duration': 0, 'frames': frames}

def make_gif(slopes):
    images = []
    slope = 0
    wheel_radius = 4
    bike_long = 20
    front_wheel = (250, 250)
    rear_wheel = get_next_point(front_wheel, -bike_long, slope)
    p1 = get_next_point(rear_wheel, bike_long/2, slope)
    p0 = get_next_point(rear_wheel, bike_long/2, slope, True)
    p3 = get_next_point(p0, bike_long/4, slope)
    p4 = get_next_point(p3, bike_long/2, slope)
    driver = get_next_point(p4, bike_long/4, slope, True)
    seat = get_next_point(p3, bike_long/4, slope, True)
    return images

def get_next_point(pt, length, slope, orthogonal=False):
    slopex = 1 - abs(slope)
    if orthogonal:
        return (pt[0] - length * slope, pt[1] - length * slopex)
    return (pt[0] + length * slopex, pt[1] - length * slope)
