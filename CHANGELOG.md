# Changelog

All notable changes to MandelCLI will be documented in this file.

## [1.0.0] - 2025-10-26

### Added
- Initial release of MandelCLI terminal fractal explorer
- Real-time Mandelbrot set rendering with ASCII art
- Real-time Julia set rendering with ASCII art
- Interactive navigation with keyboard controls (WASD for panning, +/- for zoom)
- Dynamic iteration adjustment with [ and ] keys
- Mode toggling between Mandelbrot and Julia sets (J key)
- Julia set parameter adjustment (I/K for real part, U/M for imaginary part)
- 256-color terminal support with vibrant gradient palettes
- Multiple color palette themes (classic, fire, ocean, grayscale)
- Real-time color palette cycling (C key)
- Performance metrics display (FPS, iteration count, viewport coordinates)
- Preset bookmark system for famous Mandelbrot regions
  - Full View (1)
  - Seahorse Valley (2)
  - Spiral Detail (3)
  - Elephant Valley (4)
- Interactive help screen (H key)
- Reset view command (R key)
- Comprehensive test suite for fractal calculations
- Standalone demo script for non-interactive showcases
- MIT License
- Complete documentation with setup guide and controls reference

### Technical Details
- Modular Python architecture (main.py, render.py, controls.py)
- Curses-based terminal UI for cross-platform compatibility
- Efficient escape-time algorithm for fractal computation
- Smooth ASCII character gradient mapping
- FPS tracking with rolling average over 30 frames
- Support for detailed ASCII ramp (70+ characters)
- Graceful color fallback for terminals without 256-color support

### Performance
- Typical performance: 100-300 FPS on modern hardware
- Optimized rendering pipeline with minimal overhead
- Real-time responsiveness for all navigation commands

