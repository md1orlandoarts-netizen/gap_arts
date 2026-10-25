"""Tratamento de cor padrão GAP: saturação +32%, contraste +8%, leve reforço de azul no céu.
Uso: python3 grade.py entrada.jpg saida.jpg"""
import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB')
im=ImageEnhance.Color(im).enhance(1.32); im=ImageEnhance.Contrast(im).enhance(1.08)
r,g,b=im.split(); b=b.point(lambda v: min(255,int(v*1.05)) if v>120 else v)
Image.merge('RGB',(r,g,b)).save(sys.argv[2],quality=95)
