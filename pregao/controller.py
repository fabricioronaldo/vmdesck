from pregao.views import PregaoView


class PregaoController():
  def __init__(self):
    self.views = PregaoView(self)
    
    
  def run(self):
    self.views.mainloop()
  
  
  