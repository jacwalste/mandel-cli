#!/usr/bin/env python3

from render import FractalRenderer


def test_mandelbrot_basic():
    iterations = FractalRenderer(1, 1).mandelbrot(0, 100)
    assert iterations == 100, "Origin should not escape"
    
    iterations = FractalRenderer(1, 1).mandelbrot(complex(2, 2), 100)
    assert iterations < 100, "Point (2,2) should escape quickly"
    
    print("✓ Mandelbrot calculations work correctly")


def test_julia_basic():
    renderer = FractalRenderer(1, 1)
    iterations = renderer.julia(0, complex(-0.7, 0.27015), 100)
    assert iterations >= 0 and iterations <= 100, "Julia iteration count should be in range"
    
    print("✓ Julia calculations work correctly")


def test_char_mapping():
    renderer = FractalRenderer(1, 1, use_color=False)
    
    char, color = renderer.map_to_char(0, 100)
    assert char == renderer.ASCII_RAMP[0], "Low iterations should map to first char"
    
    char, color = renderer.map_to_char(100, 100)
    assert char == renderer.ASCII_RAMP[-1], "Max iterations should map to last char"
    
    print("✓ Character mapping works correctly")


def test_frame_rendering():
    renderer = FractalRenderer(20, 10, use_color=False)
    frame = renderer.render_mandelbrot(-2.5, 1.0, -1.0, 1.0, 50)
    
    assert len(frame) == 10, "Frame should have correct height"
    assert len(frame[0]) == 20, "Frame should have correct width"
    
    print("✓ Frame rendering produces correct dimensions")


def test_fps_calculation():
    renderer = FractalRenderer(10, 10)
    renderer.render_mandelbrot(-2.5, 1.0, -1.0, 1.0, 20)
    renderer.render_mandelbrot(-2.5, 1.0, -1.0, 1.0, 20)
    
    fps = renderer.get_fps()
    assert fps > 0, "FPS should be positive after rendering frames"
    
    print("✓ FPS calculation works correctly")


if __name__ == "__main__":
    print("Running MandelCLI tests...\n")
    
    test_mandelbrot_basic()
    test_julia_basic()
    test_char_mapping()
    test_frame_rendering()
    test_fps_calculation()
    
    print("\n🎉 All tests passed!")

