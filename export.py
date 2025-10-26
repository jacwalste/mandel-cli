import datetime
from render import FractalRenderer


class FractalExporter:
    
    def __init__(self):
        pass
    
    def export_to_txt(self, frame, filename=None):
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"mandel_export_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            for line in frame:
                row_str = ''.join(char for char, _ in line)
                f.write(row_str + '\n')
        
        return filename
    
    def export_to_ansi(self, frame, filename=None):
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"mandel_export_{timestamp}.ans"
        
        color_codes = {
            16: '\033[38;5;16m',
            17: '\033[38;5;17m',
            18: '\033[38;5;18m',
            19: '\033[38;5;19m',
            20: '\033[38;5;20m',
            21: '\033[38;5;21m',
            27: '\033[38;5;27m',
            33: '\033[38;5;33m',
            39: '\033[38;5;39m',
            45: '\033[38;5;45m',
            51: '\033[38;5;51m',
            52: '\033[38;5;52m',
            88: '\033[38;5;88m',
            124: '\033[38;5;124m',
            160: '\033[38;5;160m',
            196: '\033[38;5;196m',
        }
        
        reset = '\033[0m'
        
        with open(filename, 'w', encoding='utf-8') as f:
            for line in frame:
                for char, color in line:
                    if color and color in color_codes:
                        f.write(color_codes[color] + char)
                    else:
                        f.write(char)
                f.write(reset + '\n')
        
        return filename
    
    def export_current_view(self, renderer, x_min, x_max, y_min, y_max, 
                           max_iter, mode='mandelbrot', c_real=None, c_imag=None,
                           format='txt'):
        if mode == 'mandelbrot':
            frame = renderer.render_mandelbrot(x_min, x_max, y_min, y_max, max_iter)
        else:
            frame = renderer.render_julia(x_min, x_max, y_min, y_max, 
                                         c_real, c_imag, max_iter)
        
        if format == 'ansi':
            return self.export_to_ansi(frame)
        else:
            return self.export_to_txt(frame)

