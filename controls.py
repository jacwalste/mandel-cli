import curses
from render import FractalRenderer


class MandelCLI:
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.setup_curses()
        
        self.mode = "mandelbrot"
        
        self.mandelbrot_x_min = -2.5
        self.mandelbrot_x_max = 1.0
        self.mandelbrot_y_min = -1.0
        self.mandelbrot_y_max = 1.0
        
        self.julia_x_min = -2.0
        self.julia_x_max = 2.0
        self.julia_y_min = -1.5
        self.julia_y_max = 1.5
        self.julia_c_real = -0.7
        self.julia_c_imag = 0.27015
        
        self.max_iter = 50
        self.running = True
        
        self.height, self.width = self.stdscr.getmaxyx()
        self.render_height = self.height - 3
        self.renderer = FractalRenderer(self.width, self.render_height)
        
    def setup_curses(self):
        curses.curs_set(0)
        self.stdscr.nodelay(True)
        self.stdscr.keypad(True)
        self.stdscr.timeout(0)
        
        if curses.has_colors():
            curses.start_color()
            curses.use_default_colors()
            for i in range(1, min(curses.COLORS, 256)):
                curses.init_pair(i, i, -1)
    
    def get_view_bounds(self):
        if self.mode == "mandelbrot":
            return (self.mandelbrot_x_min, self.mandelbrot_x_max,
                    self.mandelbrot_y_min, self.mandelbrot_y_max)
        else:
            return (self.julia_x_min, self.julia_x_max,
                    self.julia_y_min, self.julia_y_max)
    
    def set_view_bounds(self, x_min, x_max, y_min, y_max):
        if self.mode == "mandelbrot":
            self.mandelbrot_x_min = x_min
            self.mandelbrot_x_max = x_max
            self.mandelbrot_y_min = y_min
            self.mandelbrot_y_max = y_max
        else:
            self.julia_x_min = x_min
            self.julia_x_max = x_max
            self.julia_y_min = y_min
            self.julia_y_max = y_max
    
    def pan(self, dx, dy):
        x_min, x_max, y_min, y_max = self.get_view_bounds()
        x_range = x_max - x_min
        y_range = y_max - y_min
        
        x_shift = dx * x_range * 0.1
        y_shift = dy * y_range * 0.1
        
        self.set_view_bounds(
            x_min + x_shift, x_max + x_shift,
            y_min + y_shift, y_max + y_shift
        )
    
    def zoom(self, factor):
        x_min, x_max, y_min, y_max = self.get_view_bounds()
        
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        
        x_range = (x_max - x_min) * factor
        y_range = (y_max - y_min) * factor
        
        self.set_view_bounds(
            x_center - x_range / 2, x_center + x_range / 2,
            y_center - y_range / 2, y_center + y_range / 2
        )
    
    def reset_view(self):
        if self.mode == "mandelbrot":
            self.mandelbrot_x_min = -2.5
            self.mandelbrot_x_max = 1.0
            self.mandelbrot_y_min = -1.0
            self.mandelbrot_y_max = 1.0
        else:
            self.julia_x_min = -2.0
            self.julia_x_max = 2.0
            self.julia_y_min = -1.5
            self.julia_y_max = 1.5
        self.max_iter = 50
    
    def toggle_mode(self):
        self.mode = "julia" if self.mode == "mandelbrot" else "mandelbrot"
    
    def adjust_julia_constant(self, real_delta=0, imag_delta=0):
        self.julia_c_real += real_delta
        self.julia_c_imag += imag_delta
    
    def handle_input(self):
        try:
            key = self.stdscr.getch()
            
            if key == ord('q') or key == ord('Q'):
                self.running = False
            elif key == ord('w') or key == ord('W'):
                self.pan(0, -1)
            elif key == ord('s') or key == ord('S'):
                self.pan(0, 1)
            elif key == ord('a') or key == ord('A'):
                self.pan(-1, 0)
            elif key == ord('d') or key == ord('D'):
                self.pan(1, 0)
            elif key == ord('+') or key == ord('='):
                self.zoom(0.8)
            elif key == ord('-') or key == ord('_'):
                self.zoom(1.25)
            elif key == ord('['):
                self.max_iter = max(10, self.max_iter - 10)
            elif key == ord(']'):
                self.max_iter = min(500, self.max_iter + 10)
            elif key == ord('r') or key == ord('R'):
                self.reset_view()
            elif key == ord('j') or key == ord('J'):
                self.toggle_mode()
            elif key == ord('i') or key == ord('I'):
                self.adjust_julia_constant(real_delta=0.05)
            elif key == ord('k') or key == ord('K'):
                self.adjust_julia_constant(real_delta=-0.05)
            elif key == ord('u') or key == ord('U'):
                self.adjust_julia_constant(imag_delta=0.05)
            elif key == ord('m') or key == ord('M'):
                self.adjust_julia_constant(imag_delta=-0.05)
                
        except:
            pass
    
    def render_frame(self):
        x_min, x_max, y_min, y_max = self.get_view_bounds()
        
        if self.mode == "mandelbrot":
            frame = self.renderer.render_mandelbrot(
                x_min, x_max, y_min, y_max, self.max_iter
            )
        else:
            frame = self.renderer.render_julia(
                x_min, x_max, y_min, y_max,
                self.julia_c_real, self.julia_c_imag,
                self.max_iter
            )
        
        self.stdscr.clear()
        
        for i, line in enumerate(frame):
            if i < self.render_height:
                try:
                    self.stdscr.addstr(i, 0, line)
                except:
                    pass
        
        self.render_status_bar()
        self.stdscr.refresh()
    
    def render_status_bar(self):
        fps = self.renderer.get_fps()
        x_min, x_max, y_min, y_max = self.get_view_bounds()
        
        mode_text = f"Mode: {self.mode.upper()}"
        iter_text = f"Iter: {self.max_iter}"
        fps_text = f"FPS: {fps:.1f}"
        
        status_line_1 = f"{mode_text} | {iter_text} | {fps_text}"
        
        if self.mode == "julia":
            coord_text = f"c = {self.julia_c_real:.4f} + {self.julia_c_imag:.4f}i"
        else:
            coord_text = f"x:[{x_min:.4f}, {x_max:.4f}] y:[{y_min:.4f}, {y_max:.4f}]"
        
        status_line_2 = coord_text
        
        help_line = "Q:quit W/A/S/D:pan +/-:zoom [:]:iter J:mode R:reset"
        
        try:
            self.stdscr.addstr(self.render_height, 0, status_line_1[:self.width-1])
            self.stdscr.addstr(self.render_height + 1, 0, status_line_2[:self.width-1])
            self.stdscr.addstr(self.render_height + 2, 0, help_line[:self.width-1])
        except:
            pass
    
    def run(self):
        while self.running:
            self.handle_input()
            self.render_frame()

