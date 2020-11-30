area_polygon=lambda v:round(abs(sum(v[i][0]*v[i-1][1]-v[i][1]*v[i-1][0]for i in range(len(v)))/2),1)
