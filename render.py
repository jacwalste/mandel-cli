import time
import curses


class FractalRenderer:
    
    ASCII_RAMP = " .:-=+*#%@"
    ASCII_RAMP_DETAILED = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    
    COLOR_PALETTES = {
        'classic': [16, 17, 18, 19, 20, 21, 27, 33, 39, 45, 51, 50, 49, 48, 47, 46,
                    82, 118, 154, 190, 226, 220, 214, 208, 202, 196, 160, 124, 88, 52],
        'fire': [16, 52, 88, 124, 160, 196, 202, 208, 214, 220, 226, 227, 228, 229, 230, 231],
        'ocean': [16, 17, 18, 19, 20, 21, 27, 33, 39, 45, 51, 87, 123, 159, 195, 231],
        'grayscale': [232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
    }
    
    def __init__(self, width, height, use_color=True, palette='classic', detailed=False):
        self.width = width
        self.height = height
        self.use_color = use_color
        self.palette = self.COLOR_PALETTES.get(palette, self.COLOR_PALETTES['classic'])
        self.ascii_ramp = self.ASCII_RAMP_DETAILED if detailed else self.ASCII_RAMP
        self.frame_times = []
        
    def mandelbrot(self, c, max_iter):
        z = 0
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter
    
    def julia(self, z, c, max_iter):
        for n in range(max_iter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return max_iter
    
    def map_to_char(self, iterations, max_iter):
        if iterations == max_iter:
            return self.ascii_ramp[-1], None
        
        ratio = iterations / max_iter
        char_index = int(ratio * (len(self.ascii_ramp) - 1))
        char = self.ascii_ramp[char_index]
        
        if self.use_color:
            try:
                if curses.has_colors():
                    color_index = int(ratio * (len(self.palette) - 1))
                    color = self.palette[color_index]
                    return char, color
            except:
                pass
        
        return char, None
    
    def smooth_iterations(self, z, n, max_iter):
        if n < max_iter:
            return n + 1 - (abs(z).bit_length() - 2) / 2.0
        return n
    
    def render_mandelbrot(self, x_min, x_max, y_min, y_max, max_iter):
        start_time = time.time()
        frame = []
        
        for row in range(self.height):
            line = []
            y = y_min + (y_max - y_min) * row / self.height
            
            for col in range(self.width):
                x = x_min + (x_max - x_min) * col / self.width
                c = complex(x, y)
                
                iterations = self.mandelbrot(c, max_iter)
                char, color = self.map_to_char(iterations, max_iter)
                line.append((char, color))
            
            frame.append(line)
        
        render_time = time.time() - start_time
        self.frame_times.append(render_time)
        if len(self.frame_times) > 30:
            self.frame_times.pop(0)
        
        return frame
    
    def render_julia(self, x_min, x_max, y_min, y_max, c_real, c_imag, max_iter):
        start_time = time.time()
        frame = []
        c = complex(c_real, c_imag)
        
        for row in range(self.height):
            line = []
            y = y_min + (y_max - y_min) * row / self.height
            
            for col in range(self.width):
                x = x_min + (x_max - x_min) * col / self.width
                z = complex(x, y)
                
                iterations = self.julia(z, c, max_iter)
                char, color = self.map_to_char(iterations, max_iter)
                line.append((char, color))
            
            frame.append(line)
        
        render_time = time.time() - start_time
        self.frame_times.append(render_time)
        if len(self.frame_times) > 30:
            self.frame_times.pop(0)
        
        return frame
    
    def get_fps(self):
        if not self.frame_times:
            return 0.0
        avg_time = sum(self.frame_times) / len(self.frame_times)
        return 1.0 / avg_time if avg_time > 0 else 0.0

