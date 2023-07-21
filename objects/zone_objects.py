from Classi.Zones import Lake, Mountain

descrizione = "Il Lago Mistico è avvolto da una fitta nebbia che conferisce un'aura misteriosa\n" \
              " e affascinante al suo paesaggio incantevole, dove la luce del sole filtra attraverso\n" \
              " gli alberi secolari e le leggende si intrecciano con le acque calme e oscure."


lago = Lake(name="Lago Mistico",
            descrizione=descrizione,
            pesci="Trota")

descrizione = "La montagna Picco glaciale è un luogo molto pericoloso e tutti gli abitandi di PyLand\n" \
              "si astengono dal visitarla... chi ci è andato, non è mai tornato.... però per sciare\n" \
              "è il T.O.P."

montagna = Mountain(name="Picco Glaciale",
                    descrizione=descrizione)
