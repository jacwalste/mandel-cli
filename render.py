import time


class FractalRenderer:
    
    ASCII_RAMP = " .:-=+*#%@"
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
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
            return self.ASCII_RAMP[-1]
        
        ratio = iterations / max_iter
        index = int(ratio * (len(self.ASCII_RAMP) - 1))
        return self.ASCII_RAMP[index]
    
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
                char = self.map_to_char(iterations, max_iter)
                line.append(char)
            
            frame.append(''.join(line))
        
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
                char = self.map_to_char(iterations, max_iter)
                line.append(char)
            
            frame.append(''.join(line))
        
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

