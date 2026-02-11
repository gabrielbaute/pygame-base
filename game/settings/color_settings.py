from typing import Tuple

ColorRGB = Tuple[int, int, int]

class GameColors:
    """
    Biblioteca centralizada de colores del juego.
    Organizada por familias para un acceso jerárquico.
    """
    class Red:
        """
        Familia de colores rojo en formato RGB.
        """
        IndianRed: ColorRGB = (205, 92, 92)
        LightCoral: ColorRGB = (240, 128, 128)
        Salmon: ColorRGB = (250, 128, 114)
        DarkSalmon: ColorRGB = (233, 150, 122)
        LightSalmon: ColorRGB = (255, 160, 122)
        Crimson: ColorRGB = (220, 20, 60)
        Red: ColorRGB = (255, 0, 0)
        FireBrick: ColorRGB = (178, 34, 34)
        DarkRed: ColorRGB = (139, 0, 0)

    class Pink:
        """
        Familia de colores rosa en formato RGB.
        """
        LavenderBlush: ColorRGB = (255, 240, 245)
        Pink: ColorRGB = (255, 192, 203)
        LightPink: ColorRGB = (255, 182, 193)
        HotPink: ColorRGB = (255, 105, 180)
        DeepPink: ColorRGB = (255, 20, 147)
        MediumVioletRed: ColorRGB = (199, 21, 133)
        PaleVioletRed: ColorRGB = (219, 112, 147)

    class Orange:
        """
        Familia de colores naranja en formato RGB.
        """
        LightSalmon: ColorRGB = (255, 160, 122)
        Coral: ColorRGB = (255, 127, 80)
        Tomato: ColorRGB = (255, 99, 71)
        OrangeRed: ColorRGB = (255, 69, 0)
        DarkOrange: ColorRGB = (255, 140, 0)
        Orange: ColorRGB = (255, 165, 0)

    class Yellow:
        """
        Familia de colores amarillo en formato RGB.
        """
        Gold: ColorRGB = (255, 215, 0)
        Yellow: ColorRGB = (255, 255, 0)
        LightYellow: ColorRGB = (255, 255, 224)
        LemonChiffon: ColorRGB = (255, 250, 205)
        LightGoldenrodYellow: ColorRGB = (250, 250, 210)
        PapayaWhip: ColorRGB = (255, 239, 213)
        Moccasin: ColorRGB = (255, 228, 181)
        PeachPuff: ColorRGB = (255, 218, 185)
        PaleGoldenrod: ColorRGB = (238, 232, 170)
        Khaki: ColorRGB = (240, 230, 140)
        DarkKhaki: ColorRGB = (189, 183, 107)
    
    class Purple:
        """
        Familia de colores purpura en formato RGB.
        """
        Lavender: ColorRGB = (230, 230, 250)
        Thistle: ColorRGB = (216, 191, 216)
        Plum: ColorRGB = (221, 160, 221)
        Violet: ColorRGB = (238, 130, 238)
        Orchid: ColorRGB = (218, 112, 214)
        Fuchsia: ColorRGB = (255, 0, 255)
        Magenta: ColorRGB = (255, 0, 255)
        MediumOrchid: ColorRGB = (186, 85, 211)
        MediumPurple: ColorRGB = (147, 112, 219)
        RebeccaPurple: ColorRGB = (102, 51, 153)
        BlueViolet: ColorRGB = (138, 43, 226)
        DarkViolet: ColorRGB = (148, 0, 211)
        DarkOrchid: ColorRGB = (153, 50, 204)
        DarkMagenta: ColorRGB = (139, 0, 139)
        Purple: ColorRGB = (128, 0, 128)
        Indigo: ColorRGB = (75, 0, 130)
        SlateBlue: ColorRGB = (106, 90, 205)
        DarkSlateBlue: ColorRGB = (72, 61, 139)
        MediumSlateBlue: ColorRGB = (123, 104, 238)
        
    class Green:
        """
        Familia de colores verde en formato RGB.
        """
        GreenYellow: ColorRGB = (173, 255, 47)
        Chartreuse: ColorRGB = (127, 255, 0)
        LawnGreen: ColorRGB = (124, 252, 0)
        Lime: ColorRGB = (0, 255, 0)
        LimeGreen: ColorRGB = (50, 205, 50)
        PaleGreen: ColorRGB = (152, 251, 152)
        LightGreen: ColorRGB = (144, 238, 144)
        MediumSpringGreen: ColorRGB = (0, 250, 154)
        SpringGreen: ColorRGB = (0, 255, 127)
        MediumSeaGreen: ColorRGB = (60, 179, 113)
        SeaGreen: ColorRGB = (46, 139, 87)
        ForestGreen: ColorRGB = (34, 139, 34)
        Green: ColorRGB = (0, 128, 0)
        DarkGreen: ColorRGB = (0, 100, 0)
        YellowGreen: ColorRGB = (154, 205, 50)
        OliveDrab: ColorRGB = (107, 142, 35)
        Olive: ColorRGB = (128, 128, 0)
        DarkOliveGreen: ColorRGB = (85, 107, 47)
        MediumAquamarine: ColorRGB = (102, 205, 170)
        DarkSeaGreen: ColorRGB = (143, 188, 143)
        LightSeaGreen: ColorRGB = (32, 178, 170)
        DarkCyan: ColorRGB = (0, 139, 139)
        Teal: ColorRGB = (0, 128, 128)

    class Blue:
        """
        Familia de colores azul en formato RGB.
        """
        Aqua: ColorRGB = (0, 255, 255)
        Cyan: ColorRGB = (0, 255, 255)
        LightCyan: ColorRGB = (224, 255, 255)
        PaleTurquoise: ColorRGB = (175, 238, 238)
        Aquamarine: ColorRGB = (127, 255, 212)
        Turquoise: ColorRGB = (64, 224, 208)
        MediumTurquoise: ColorRGB = (72, 209, 204)
        DarkTurquoise: ColorRGB = (0, 206, 209)
        CadetBlue: ColorRGB = (95, 158, 160)
        SteelBlue: ColorRGB = (70, 130, 180)
        LightSteelBlue: ColorRGB = (176, 196, 222)
        PowderBlue: ColorRGB = (176, 224, 230)
        LightBlue: ColorRGB = (173, 216, 230)
        SkyBlue: ColorRGB = (135, 206, 235)
        LightSkyBlue: ColorRGB = (135, 236, 255)
        DeepSkyBlue: ColorRGB = (0, 191, 255)
        DodgerBlue: ColorRGB = (30, 144, 255)
        CornflowerBlue: ColorRGB = (100, 149, 237)
        MediumSlateBlue: ColorRGB = (123, 104, 238)
        RoyalBlue: ColorRGB = (65, 105, 225)
        Blue: ColorRGB = (0, 0, 255)
        MediumBlue: ColorRGB = (0, 0, 205)
        DarkBlue: ColorRGB = (0, 0, 139)
        Navy: ColorRGB = (0, 0, 128)
        MidnightBlue: ColorRGB = (25, 25, 112)
    
    class Brown:
        """
        Familia de colores marrón en formato RGB.
        """
        Cornsilk: ColorRGB = (255, 248, 220)
        BlanchedAlmond: ColorRGB = (255, 235, 205)
        Bisque: ColorRGB = (255, 228, 196)
        NavajoWhite: ColorRGB = (255, 222, 173)
        Wheat: ColorRGB = (245, 222, 179)
        BurlyWood: ColorRGB = (222, 184, 135)
        Tan: ColorRGB = (210, 180, 140)
        RosyBrown: ColorRGB = (188, 143, 143)
        SandyBrown: ColorRGB = (244, 164, 96)
        Goldenrod: ColorRGB = (218, 165, 32)
        DarkGoldenrod: ColorRGB = (184, 134, 11)
        Peru: ColorRGB = (205, 133, 63)
        Chocolate: ColorRGB = (210, 105, 30)
        SaddleBrown: ColorRGB = (139, 69, 19)
        Sienna: ColorRGB = (160, 82, 45)
        Brown: ColorRGB = (165, 42, 42)
        Maroon: ColorRGB = (128, 0, 0)
    
    class White:
        """
        Familia de colores blanco en formato RGB.
        """
        White: ColorRGB = (255, 255, 255)
        Snow: ColorRGB = (255, 250, 250)
        Honeydew: ColorRGB = (240, 255, 240)
        MintCream: ColorRGB = (245, 255, 250)
        Azure: ColorRGB = (240, 255, 255)
        AliceBlue: ColorRGB = (240, 248, 255)
        GhostWhite: ColorRGB = (248, 248, 255)
        WhiteSmoke: ColorRGB = (245, 245, 245)
        Seashell: ColorRGB = (255, 245, 238)
        Beige: ColorRGB = (245, 245, 220)
        OldLace: ColorRGB = (253, 245, 230)
        FloralWhite: ColorRGB = (255, 250, 240)
        Ivory: ColorRGB = (255, 255, 240)
        AntiqueWhite: ColorRGB = (250, 235, 215)
        Linen: ColorRGB = (250, 240, 230)
        LavenderBlush: ColorRGB = (255, 240, 245)
        MistyRose: ColorRGB = (255, 228, 225)
    
    class Gray:
        """
        Familia de colores gris en formato RGB.
        """
        Gainsboro: ColorRGB = (220, 220, 220)
        LightGray: ColorRGB = (211, 211, 211)
        Silver: ColorRGB = (192, 192, 192)
        DarkGray: ColorRGB = (169, 169, 169)
        Gray: ColorRGB = (128, 128, 128)
        DimGray: ColorRGB = (105, 105, 105)
        LightSlateGray: ColorRGB = (119, 136, 153)
        SlateGray: ColorRGB = (112, 128, 144)
        DarkSlateGray: ColorRGB = (47, 79, 79)
        Black: ColorRGB = (0, 0, 0)

    @classmethod
    def get_rgb_from_hex(cls, hex_code: str) -> ColorRGB:
        """
        Utilidad para convertir códigos hexadecimales a RGB de Pygame.
        
        Args:
            hex_code: String como '#FFFFFF' o 'FFFFFF'.
        """
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def adjust_brightness(color: ColorRGB, factor: float) -> ColorRGB:
        """
        Ajusta el brillo de un color.
        
        Args:
            color: Tupla RGB original.
            factor: Multiplicador (ej: 0.8 para -20%, 1.2 para +20%).
            
        Returns:
            Tupla RGB ajustada y clampada entre 0 y 255.
        """
        return tuple(max(0, min(255, int(c * factor))) for c in color)

    @staticmethod
    def lerp(color_a: ColorRGB, color_b: ColorRGB, t: float) -> ColorRGB:
        """
        Interpolación lineal entre dos colores.
        
        Args:
            color_a: Color inicial.
            color_b: Color final.
            t: Factor de mezcla (0.0 es color_a, 1.0 es color_b).
        """
        return tuple(
            int(a + (b - a) * t) for a, b in zip(color_a, color_b)
        )
    
    @staticmethod
    def with_alpha(color: ColorRGB, alpha: int) -> Tuple[int, int, int, int]:
        """
        Convierte RGB a RGBA.
        
        Args:
            color: el color sobre el que queremos agregar el alpha.
            alpha: el valor del alpha.
        
        Returns:
            el color con el alpha agregado.
        """
        return (*color, max(0, min(255, alpha)))