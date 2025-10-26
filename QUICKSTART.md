# 🚀 MandelCLI Quick Start Guide

Get exploring fractals in 60 seconds!

## Installation

No external dependencies needed - just Python 3.8+:

```bash
cd mandel-cli
python3 main.py
```

## First Launch

When you launch MandelCLI, you'll see the classic Mandelbrot set rendered in beautiful ASCII art with colors!

## Essential Controls

### Navigation (Most Used)
```
W A S D  → Pan around (up/left/down/right)
+ -      → Zoom in/out
H        → Help screen (see all controls)
Q        → Quit
```

### Exploration
```
J        → Switch between Mandelbrot and Julia sets
1 2 3 4  → Jump to famous regions (bookmarks)
C        → Cycle through color palettes
```

### Fine-Tuning
```
[ ]      → Decrease/increase detail (iterations)
R        → Reset to default view
E        → Export current view to file
```

## Try This Flow

1. **Launch:** `python3 main.py`
2. **Zoom in:** Press `+` a few times
3. **Pan around:** Use `W A S D` to explore
4. **Try a bookmark:** Press `2` for Seahorse Valley
5. **Change palette:** Press `C` for fire colors
6. **Toggle Julia:** Press `J` to see Julia set
7. **Get help:** Press `H` anytime
8. **Export:** Press `E` to save what you see

## Demo Mode

Want to see it without interaction?

```bash
python3 demo.py
```

This shows pre-rendered Mandelbrot, Julia, and zoom sequences.

## Tips

- **Zoom gradually** - The detail is infinite!
- **Try all bookmarks** - Each shows unique patterns
- **Increase iterations** (with `]`) when zoomed in deep
- **Julia mode** - Use `I K U M` to morph the pattern
- **Export often** - Save your favorite discoveries

## Keyboard Layout Reference

```
    [W]           Increase Iter: ]
  [A][S][D]       Decrease Iter: [
  
  Zoom: + -       Bookmarks: 1 2 3 4
  
  Mode: J         Palette: C
  Help: H         Export: E
  Reset: R        Quit: Q
```

## Troubleshooting

**No colors?**
- Your terminal may not support 256 colors
- Try iTerm2 (Mac), Windows Terminal, or GNOME Terminal

**Slow performance?**
- Decrease iterations with `[`
- Reduce terminal window size
- Typical: 100-300 FPS on modern hardware

**Windows?**
- Install windows-curses: `pip install windows-curses`

## What to Explore

Start with these journeys:

1. **The Bulb:** Default view, zoom into the main bulb
2. **Seahorse Valley:** Press `2`, zoom in slowly
3. **Julia Morph:** Press `J`, then hold `I` or `U`
4. **Deep Zoom:** Press `1`, then hold `+` and watch infinity unfold

## Next Steps

- Read `README.md` for full documentation
- Check `CHANGELOG.md` for version history
- Run `python3 test_fractals.py` to verify installation
- Explore and discover your own favorite regions!

---

**Happy Exploring!** 🌀

*Pro tip: Screenshots make great wallpapers and social media posts*

