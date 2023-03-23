import cairo
import math
from vector import Vector2


width, height = 200, 200
with cairo.PDFSurface("example.pdf", width, height) as surface:
    context = cairo.Context(surface)

    context.scale(width, height)

    # Hexagonal lattice vectors.
    v0 = Vector2(0.5, 0.5)
    h0 = Vector2(1, 0) * 0.3
    h1 = Vector2(math.cos(math.pi / 3), math.sin(math.pi / 3)) * 0.3

    # Points
    p0 = v0
    p1 = v0 + h0
    p2 = v0 + (2 * h0)

    p3 = v0 + h1
    p4 = v0 + (h0 + h1)

    p5 = v0 + (2 * h1)
    p6 = v0 + (h0 + 2 * h1)

    # Points
    for p in [p0, p1, p2, p3, p4, p5, p6]:
        context.arc(p.x, p.y, 0.01, 0, 2 * math.pi)
        context.fill()

    # Edges
    context.set_line_width(0.007)
    for u, v in [
        (p0, p1),
        (p0, p3),
        (p3, p4),
        (p1, p4),
        (p3, p5),
        (p5, p6),
        (p5, p4),
        (p4, p6),
        (p4, p2),
    ]:
        context.move_to(u.x, u.y)
        context.line_to(v.x, v.y)
        context.stroke()
