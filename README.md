# 🌀 MandelCLI

**A retro-hacker's terminal-based fractal explorer**

MandelCLI renders stunning ASCII visualizations of the Mandelbrot and Julia sets directly in your terminal. Navigate infinite mathematical beauty with real-time keyboard controls, smooth gradients, and vintage computing aesthetics.

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

## ✨ Features

- 🎨 **Interactive Exploration** — Navigate the Mandelbrot and Julia sets in real-time
- ⌨️ **Keyboard Controls** — Smooth panning, zooming, and parameter tweaking
- 🌈 **ASCII Art Rendering** — Beautiful density gradients using character ramps
- 📊 **Performance Metrics** — Live FPS counter, iteration count, and viewport info
- 🎭 **Dual Modes** — Toggle between Mandelbrot and Julia set visualizations
- 🎨 **Color Support** — Rich terminal colors for enhanced visual experience
- ⚡ **Lightweight** — Minimal dependencies, maximum performance

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python main.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `W` `A` `S` `D` | Pan view (up/left/down/right) |
| `+` `-` | Zoom in/out |
| `[` `]` | Decrease/increase iterations |
| `J` | Toggle Mandelbrot ↔ Julia mode |
| `I` `K` | Adjust Julia constant (real part) |
| `U` `M` | Adjust Julia constant (imaginary part) |
| `R` | Reset to default view |
| `Q` | Quit |

## 📦 Requirements

- Python 3.8+
- Terminal with Unicode support
- `curses` (included with Python on Unix/macOS)
- `windows-curses` (for Windows users)

## 🎯 Technical Details

MandelCLI uses escape-time algorithms to calculate fractal sets and maps iteration counts to ASCII characters for rendering. The application uses Python's curses library for terminal control and input handling.

**Mandelbrot Set:** For each pixel c in the complex plane, iterate z = z² + c starting from z = 0.

**Julia Set:** For a fixed constant c, iterate z = z² + c for each pixel position z.

## 🛠️ Project Structure

```
mandel-cli/
├── main.py          # Application entry point
├── render.py        # Fractal calculation and rendering
├── controls.py      # Input handling and UI logic
├── test_fractals.py # Test suite for fractal math
├── requirements.txt # Python dependencies
└── README.md       # This file
```

## 🧪 Testing

Run the test suite to verify fractal calculations:

```bash
python3 test_fractals.py
```

## 🎨 Showcase

Experience mathematical beauty in your terminal — from the iconic Mandelbrot bulb to morphing Julia sets. Perfect for demos, screencasts, or just zoning out while contemplating infinity.

## 📝 License

MIT License - Explore freely!

---

*Made with ❤️ for terminal enthusiasts and fractal lovers*

