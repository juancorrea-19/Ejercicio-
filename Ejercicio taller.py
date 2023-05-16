class dinero:
    
    def _init_(self, cantidadN,):
        self.cantidadN = cantidadN
        self.libros = 0
        self.boletos = 0
        self.diaMadre = 0
        self.transporte  = 0
       
        
    def calcular_libros (self):
        self.libros= (self.cantidadN*50)/100
        print("la cantidad destinada para libros es :",self.libros)
        
    def calcular_transporte  (self):
        
         self.transporte= (self.cantidadN*20)/100
         print("la cantidad destinada para tranpoete  es :",self.transporte )
         print("numero de boletos que puede comprar:",self.transporte/2)
         
    def calcular_boletoscine  (self):
        
         self.boletos= (self.cantidadN*20)/100
         print("la cantidad destinada para las boletas delcine es :",self.boletos )
         print("numero de boletos que puede comprar:",self.boletos/5)
         
    def calcular_DMadre (self):
        
         self.diaMadre= (self.cantidadN-(self.boletos + self.transporte + self.libros ))
         print("la cantidad destinada para el dia de la madre  es :",self.diaMadre) 
         
            
            
            
            
               
entrega1= dinero(1000000)

entrega1.calcular_libros()

entrega1.calcular_transporte()

entrega1.calcular_boletoscine()

entrega1.calcular_DMadre ()