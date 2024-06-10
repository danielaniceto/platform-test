import folium
from db import isCoordenadas

class MostraMapas():
    def ismostramaps():
        coord = isCoordenadas.select_coordenadas
        maps = folium.Map(location=coord, zoom_start=9, control_scale=True)

        #adicionando todos os pontos no mapa
        for maps in coord:
            folium.Marker(coord, popup="<i>Localização</i>", tooltip="Localização").add_to(maps)

        maps.save("mostramapa.html")
