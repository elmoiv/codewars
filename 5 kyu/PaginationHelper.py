class PaginationHelper:
  def __init__(self, col, ipp):
      self.col, self.ipp = [col, ipp]

  def item_count(self):
      return len(self.col)
    
  def page_count(self):
      return -(-len(self.col)//self.ipp)
	
  def page_item_count(self,pi):
      return -1 if pi+1 > self.page_count() else self.ipp if pi+1 < self.page_count() else self.item_count()%self.ipp

  def page_index(self,ind):
      return int(ind/self.ipp) if ind in range(0,len(self.col)) else -1
