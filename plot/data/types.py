
class Type(object):
    """
    This class represents a plot data info.
    It has a list of data(infos for coordinate)
    
    """

    def __init__(self):
    
        self.show = True
        self.fill = True
        
class Lines(Type):
    """
    """

    def __init__(self):   
        self.show = True
        self.fill = True 
        self.steps = False
                
class Points(Type):
    """
    """

    def __init__(self):   
        self.show = True
        self.fill = True 
        self.radius = None
        
        
class Bars(Type):
    """
    """

    def __init__(self):   
        self.show = True
        self.fill = True 
        self.barWidth = None
        self.align = None
        self.horizontal = None
        
