#!/usr/bin/env python3

import sys
import time
from render import FractalRenderer


def print_banner():
    print("\n" + "="*60)
    print("  🌀 MandelCLI - Terminal Fractal Explorer")
    print("="*60 + "\n")


def demo_mandelbrot():
    print("Rendering Mandelbrot Set...")
    renderer = FractalRenderer(80, 30, use_color=False)
    frame = renderer.render_mandelbrot(-2.5, 1.0, -1.25, 1.25, 50)
    
    for line in frame:
        print(''.join(char for char, _ in line))
    
    print(f"\nFPS: {renderer.get_fps():.1f}")


def demo_julia():
    print("\n\nRendering Julia Set (c = -0.7 + 0.27015i)...")
    renderer = FractalRenderer(80, 30, use_color=False)
    frame = renderer.render_julia(-2.0, 2.0, -1.5, 1.5, -0.7, 0.27015, 50)
    
    for line in frame:
        print(''.join(char for char, _ in line))
    
    print(f"\nFPS: {renderer.get_fps():.1f}")


def demo_zoom_sequence():
    print("\n\nZoom Animation (3 frames)...")
    renderer = FractalRenderer(60, 20, use_color=False)
    
    zoom_coords = [
        (-2.5, 1.0, -1.0, 1.0),
        (-1.5, 0.5, -0.5, 0.5),
        (-0.8, -0.4, -0.2, 0.2),
    ]
    
    for i, (x_min, x_max, y_min, y_max) in enumerate(zoom_coords):
        print(f"\nFrame {i+1}:")
        frame = renderer.render_mandelbrot(x_min, x_max, y_min, y_max, 50)
        for line in frame:
            print(''.join(char for char, _ in line))
        time.sleep(0.5)


def main():
    print_banner()
    
    print("This is a static demo. Run 'python3 main.py' for the interactive explorer!\n")
    
    demo_mandelbrot()
    demo_julia()
    demo_zoom_sequence()
    
    print("\n" + "="*60)
    print("  Run 'python3 main.py' to explore interactively!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()

