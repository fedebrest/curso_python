class CabeceraPagina: 
    def inicializar(self,tit): 
      self.titulo=tit 

    def mostrar(self): 
        print (self.titulo )

cabecera=CabeceraPagina() 
cabecera.inicializar('Aprendiendo a progrmar en Python') 
cabecera.mostrar() 
