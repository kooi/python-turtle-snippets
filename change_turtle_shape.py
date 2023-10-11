import turtle
tina = turtle.Turtle()

# exported from GIMP and set to tuple-poly format
wasp_polygon = ((136.67,197.33),(147.33,245.33),(147.33,245.33),(147.33,245.33),(95.33,276.67),(95.33,276.67),(95.33,276.67),(123.33,302.00),(123.33,302.00),(123.33,302.00),(112.00,320.00),(112.00,320.00),(112.00,320.00),(127.33,343.33),(128.00,343.33),(128.67,343.33),(134.67,278.00),(134.67,278.00),(134.67,278.00),(166.00,255.33),(166.00,255.33),(166.00,255.33),(205.33,271.33),(205.33,271.33),(205.33,271.33),(188.67,319.33),(188.67,319.33),(188.67,319.33),(157.33,365.33),(157.33,365.33),(157.33,365.33),(132.00,378.67),(132.00,378.67),(132.00,378.67),(164.00,370.67),(164.00,370.67),(164.00,370.67),(168.67,358.00),(168.67,358.00),(168.67,358.00),(195.33,341.33),(196.00,341.33),(196.67,341.33),(207.33,295.33),(207.33,295.33),(207.33,295.33),(220.67,274.00),(220.67,274.00),(220.67,274.00),(288.67,267.33),(288.67,267.33),(288.67,267.33),(294.67,316.00),(294.67,316.00),(294.67,316.00),(238.67,355.33),(238.67,355.33),(238.67,355.33),(211.33,362.00),(211.33,362.00),(211.33,362.00),(223.33,368.67),(223.33,368.67),(223.33,368.67),(301.33,328.67),(301.33,328.67),(301.33,328.67),(303.33,360.67),(303.33,360.67),(303.33,360.67),(233.33,415.33),(233.33,415.33),(233.33,415.33),(348.00,351.33),(348.00,351.33),(348.00,351.33),(316.00,334.00),(316.00,334.00),(316.00,334.00),(324.67,314.67),(324.67,314.67),(324.67,314.67),(366.67,361.33),(366.67,361.33),(366.67,361.33),(423.33,394.67),(423.33,394.67),(423.33,394.67),(452.00,342.67),(452.00,342.67),(452.00,342.67),(456.67,295.33),(456.67,295.33),(456.67,295.33),(442.00,250.67),(441.33,250.67),(440.67,250.67),(406.00,210.00),(406.00,210.00),(406.00,210.00),(357.33,183.33),(357.33,183.33),(357.33,183.33),(286.00,196.00),(286.00,196.00),(286.00,196.00),(224.00,147.33),(224.00,147.33),(224.00,147.33),(380.67,161.33),(380.67,161.33),(380.67,161.33),(496.67,132.67),(496.67,132.67),(496.67,132.67),(348.67,116.67),(348.67,116.67),(348.67,116.67),(249.33,133.33),(249.33,133.33),(249.33,133.33),(354.00,86.00),(354.00,86.00),(354.00,86.00),(424.00,19.33),(423.33,20.00),(422.67,20.67),(286.67,70.00),(286.67,70.00),(286.67,70.00),(216.00,137.33),(216.00,137.33),(216.00,137.33),(136.00,167.33),(136.00,167.33),(136.00,167.33),(126.67,147.33),(126.67,147.33),(126.67,147.33),(96.67,145.33),(96.67,145.33),(96.67,145.33),(80.67,174.67),(80.67,174.67),(80.67,174.67),(72.67,162.00),(72.67,162.00),(72.67,162.00),(20.00,130.67),(20.00,130.67),(20.00,130.67),(64.67,166.67),(64.67,166.67),(64.67,166.67),(70.67,178.67),(70.67,178.67),(70.67,178.67),(60.67,169.33),(60.67,169.33),(60.67,169.33),(8.67,165.33),(8.67,165.33),(8.67,165.33),(58.00,178.67),(58.00,178.67),(58.00,178.67),(64.67,189.33),(64.67,189.33),(64.67,189.33),(51.33,219.33),(51.33,219.33),(51.33,219.33),(58.67,240.67),(58.67,240.67),(58.67,240.67),(42.67,254.67),(42.67,254.67),(42.67,254.67),(45.33,265.33),(46.00,265.33),(46.67,265.33),(45.33,273.33),(45.33,273.33),(45.33,273.33),(51.33,270.00),(51.33,270.00),(51.33,270.00),(59.33,261.33),(58.67,261.33),(58.00,261.33),(116.00,238.00),(116.00,238.00))

# resize (turtlesize not implemented in Skulpt)
scale = 0.2
wasp_small_list = []
for v in wasp_polygon:
    wasp_small_list.append( (v[0]*scale, v[1]*scale) )
wasp_small_polygon = tuple(wasp_small_list)

# make the shape available
tina.getscreen().register_shape("wasp", wasp_small_polygon)

# set the new shape
tina.shape("wasp")
