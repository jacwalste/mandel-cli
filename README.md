# MandelCLI

A terminal-based fractal explorer for the Mandelbrot and Julia sets.

Real-time ASCII visualization with keyboard navigation. Written in Python using curses for cross-platform terminal rendering.

```
                    .::::::::::.
                .::::::::::::::::::::.
              .::::::::::::::::::::::::::.
            .:::::::::::::::::::::::::::::::
           .:::::::::::::::::::::::::::::::::
          .:::::::@@@@@@@@@@@@@@@@@@::::::::.
         .:::::::@@@@@@@@@@@@@@@@@@@@@:::::::.
        .:::::::@@@@@@@@@@@@@@@@@@@@@@@:::::::.
        :::::::@@@@@@@@@@@@@@@@@@@@@@@@@@::::::
       .::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::
       ::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::
       :::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::
       :::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::
       :::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::
       ::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::
       .::::::@@@@@@@@@@@@@@@@@@@@@@@@@::::::
        :::::::@@@@@@@@@@@@@@@@@@@@@@@@::::::
        .:::::::@@@@@@@@@@@@@@@@@@@@@:::::::.
         .:::::::@@@@@@@@@@@@@@@@@@@:::::::.
          .:::::::@@@@@@@@@@@@@@@@::::::::.
           .:::::::::::::::::::::::::::::
            .:::::::::::::::::::::::::::
              .::::::::::::::::::::::.
                .::::::::::::::::::::.
                    .::::::::::.
```

## Features

- Interactive Mandelbrot and Julia set exploration
- Real-time panning, zooming, and parameter adjustment
- ASCII rendering with density-based character mapping
- 256-color terminal support with multiple palettes
- Live performance metrics (FPS, iterations, viewport)
- Bookmark system for interesting regions
- Export frames to text files
- Built on Python stdlib (curses only)

## Installation

```bash
git clone https://github.com/jacwalste/mandel-cli.git
cd mandel-cli
python3 main.py
```

No external dependencies required (except `windows-curses` on Windows).

## Keyboard Controls

| Key | Function |
|-----|----------|
| W/A/S/D | Pan viewport (up/left/down/right) |
| +/- | Zoom in/out |
| [/] | Decrease/increase max iterations |
| J | Toggle between Mandelbrot and Julia modes |
| I/K | Adjust Julia constant (real component) |
| U/M | Adjust Julia constant (imaginary component) |
| 1/2/3/4 | Jump to bookmarked regions |
| C | Cycle color palette |
| E | Export current frame to file |
| H | Show help screen |
| R | Reset view to defaults |
| Q | Quit |

### Preset Bookmarks

Available in Mandelbrot mode:

1. Full View - Standard overview of the complete set
2. Seahorse Valley - Intricate spiral structures
3. Spiral Detail - Fine recursive patterns
4. Elephant Valley - Characteristic bulbous formations

## Technical Implementation

### Fractal Algorithms

**Mandelbrot Set**: For each complex number c, iterate z(n+1) = z(n)^2 + c with z(0) = 0. 
Count iterations until |z| > 2 or max iterations reached.

**Julia Set**: For a fixed complex constant c, iterate z(n+1) = z(n)^2 + c with z(0) = pixel position.
Count iterations until escape or max iterations.

### Rendering Pipeline

1. Map screen coordinates to complex plane
2. Calculate escape-time iterations for each point
3. Map iteration count to ASCII character via gradient
4. Apply color based on iteration ratio and active palette
5. Render to terminal buffer using curses

### Performance

Typical frame rates: 100-300 FPS depending on terminal size and iteration count.
FPS averaging uses rolling 30-frame window for smooth metrics.

## Architecture

```
mandel-cli/
├── main.py          - Entry point and curses wrapper
├── render.py        - Fractal math and frame generation
├── controls.py      - Input handling and UI state
├── export.py        - File export utilities
├── test_fractals.py - Unit tests for fractal calculations
└── demo.py          - Non-interactive demo mode
```

## Color Palettes

- **classic**: Blue-to-red gradient (30 colors)
- **fire**: Warm spectrum, orange to yellow (16 colors)
- **ocean**: Cool spectrum, blue to white (16 colors)
- **grayscale**: Monochrome gradient (24 shades)

Cycle between palettes with the `C` key during runtime.

## Testing

Run the test suite:

```bash
python3 test_fractals.py
```

Validates:
- Mandelbrot iteration calculations
- Julia set iteration calculations
- Character mapping logic
- Frame dimension accuracy
- FPS calculation correctness

## Requirements

- Python 3.8 or higher
- Terminal supporting Unicode characters
- For color: 256-color terminal emulator recommended
- Windows: install `windows-curses` package

## Demo Mode

For non-interactive preview:

```bash
python3 demo.py
```

Renders sample Mandelbrot and Julia frames with zoom sequence.

## Export Format

Pressing `E` exports the current view to a timestamped text file:
- Format: `mandel_export_YYYYMMDD_HHMMSS.txt`
- Plain ASCII output (color info stripped)
- One line per terminal row

## License

MIT License. See LICENSE file for details.

---

Built for exploring infinite complexity in finite terminals.
